#!/usr/bin/env python3
from __future__ import annotations
import argparse
import shutil
from pathlib import Path

PLUGIN_NAMES = [
    "transcriptomics",
    "operator-seqtk",
    "visualization-r",
    "source-ncbi",
    "source-embl-ebi",
    "retrieval-dataset-gtex",
    "retrieval-dataset-cbioportal",
    "retrieval-literature-semantic-scholar",
    "retrieval-knowledge-uniprot",
    "omiga-developer-tools",
    "ngs-alignment",
]
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", "target", "node_modules")


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh this marketplace from a sibling Omiga checkout")
    parser.add_argument("--omiga", default="../omiga", help="Path to Omiga app repository")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    omiga = Path(args.omiga).resolve()
    bundled = omiga / "src-tauri" / "bundled_plugins"
    if not bundled.is_dir():
        raise SystemExit(f"not an Omiga bundled_plugins directory: {bundled}")
    for name in PLUGIN_NAMES:
        src = bundled / "plugins" / name
        dst = root / "plugins" / name
        if not src.is_dir():
            raise SystemExit(f"missing plugin: {src}")
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=IGNORE)
        print(f"synced plugins/{name}")
    source_runners = bundled / "source_runners"
    if source_runners.is_dir():
        dst = root / "source_runners"
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(source_runners, dst, ignore=IGNORE)
        print("synced source_runners")


if __name__ == "__main__":
    main()
