# Omiga plugin marketplace operation

## Repository role

This repo is the external marketplace source for Omiga plugins. The app repo may keep a stable bundled snapshot for offline bootstrap, but plugin development, changelogs, and release cadence should live here once the plugin API is stable enough.

## Marketplace naming

The manifest currently uses `omiga-curated` so plugin ids remain compatible with the bundled curated marketplace. For local side-by-side experiments, temporarily change `name` to `omiga-curated-dev`; do not publish that name unless you intentionally want separate plugin ids.

## Remote metadata

Use GitHub raw content first:

```json
{
  "remote": {
    "provider": "github",
    "url": "https://raw.githubusercontent.com/<owner>/omiga-plugins/main/marketplace.json",
    "repositoryUrl": "https://github.com/<owner>/omiga-plugins",
    "changelogUrl": "https://github.com/<owner>/omiga-plugins/releases"
  }
}
```

A static GitHub repository is enough while marketplace operations are: list, install from source, sync, force overwrite, changelog preview, and remote update check. Move to an independent service only when you need accounts, paid plugins, ratings, search ranking, signatures, telemetry, or compatibility APIs.

## Version policy

- Every plugin should declare `version` in `plugin.json`.
- Every non-trivial plugin should include `CHANGELOG.md` and expose it via `"changelog": "./CHANGELOG.md"`.
- Marketplace releases should be tagged after validation.

## Safety policy

- Keep plugins atomic: a plugin can bundle domain-related units, but each operator/template remains independently callable and toggleable.
- Avoid committing large biological data files; use fixtures only.
- Keep platform-specific app-control binaries in the Omiga app repo unless they become independently audited release artifacts.
- Environment files are declarative; conda/docker/singularity environments should be prepared lazily by Omiga on first use/test, not during marketplace install.
