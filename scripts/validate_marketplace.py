#!/usr/bin/env python3
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "marketplace.json"
SAFE_SEGMENT = re.compile(r"^[A-Za-z0-9._-]+$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def safe_local_path(value: str) -> Path:
    if not value.startswith("./"):
        fail(f"source.path must start with ./, got {value!r}")
    parts = Path(value[2:]).parts
    if not parts or any(part in ("", ".", "..") for part in parts):
        fail(f"unsafe source.path {value!r}")
    return ROOT.joinpath(*parts)


def safe_plugin_path(plugin_root: Path, value: str) -> Path:
    if not value.startswith("./"):
        fail(f"plugin relative path must start with ./, got {value!r}")
    parts = Path(value[2:]).parts
    if not parts or any(part in ("", ".", "..") for part in parts):
        fail(f"unsafe plugin relative path {value!r}")
    return plugin_root.joinpath(*parts)


def load_plugin_json(plugin_root: Path) -> dict:
    for rel in ("plugin.json", ".omiga-plugin/plugin.json", ".codex-plugin/plugin.json"):
        candidate = plugin_root / rel
        if candidate.is_file():
            return json.loads(candidate.read_text())
    fail(f"missing plugin manifest under {plugin_root.relative_to(ROOT)}")


def main() -> None:
    data = json.loads(MANIFEST.read_text())
    if not SAFE_SEGMENT.match(data.get("name", "")):
        fail("marketplace name must be a safe segment")
    seen: set[str] = set()
    for item in data.get("plugins", []):
        name = item.get("name", "")
        if not SAFE_SEGMENT.match(name):
            fail(f"plugin name is unsafe: {name!r}")
        if name in seen:
            fail(f"duplicate plugin entry: {name}")
        seen.add(name)
        source = item.get("source") or {}
        source_kind = source.get("source", "local")
        if source_kind not in ("", "local"):
            fail(f"unsupported source kind for static marketplace validation: {source_kind}")
        plugin_root = safe_local_path(source.get("path", ""))
        if not plugin_root.is_dir():
            fail(f"plugin source directory not found: {plugin_root.relative_to(ROOT)}")
        manifest = load_plugin_json(plugin_root)
        if manifest.get("name") != name:
            fail(f"plugin {name}: plugin.json name {manifest.get('name')!r} does not match marketplace entry")
        if not manifest.get("version"):
            print(f"WARN: plugin {name} has no version", file=sys.stderr)
        changelog = manifest.get("changelog")
        default_changelog = plugin_root / "CHANGELOG.md"
        if changelog:
            path = safe_plugin_path(plugin_root, changelog)
            if not path.is_file():
                fail(f"plugin {name}: declared changelog missing: {changelog}")
        elif default_changelog.is_file():
            print(f"WARN: plugin {name} has CHANGELOG.md but does not declare changelog", file=sys.stderr)
    print(f"OK: {len(seen)} plugins in {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
