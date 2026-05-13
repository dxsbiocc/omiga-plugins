# omiga-plugins

Curated Omiga plugin marketplace. This repository is intended to become the remote, independently versioned source of truth for domain plugins while the Omiga app keeps only a minimal bundled snapshot for offline bootstrap.

## Layout

```text
marketplace.json                 # local/static marketplace manifest
marketplace.remote.example.json  # GitHub remote metadata example
plugins/                         # plugin packages grouped by official domain
  bioinformatics/
  visualization/
  resources/
resource_runners/                  # shared retrieval resource runner code
schemas/                         # lightweight JSON schemas
scripts/                         # validation and sync helpers
docs/                            # marketplace operating notes
```

## Included initial plugins

Official plugins are grouped by physical domain folder while keeping stable plugin IDs from `marketplace.json`:

- `plugins/bioinformatics/transcriptomics` — transcriptomics analysis templates for differential expression, PCA, enrichment
- `plugins/bioinformatics/ngs-alignment` — NGS alignment/post-alignment operators
- `plugins/bioinformatics/operator-seqtk` — FASTQ/FASTA subsampling operator
- `plugins/visualization/visualization-r` — R visualization templates
- `plugins/resources/resource-ncbi` — aggregated NCBI retrieval resource routes
- `plugins/resources/resource-embl-ebi` — EMBL-EBI retrieval resource routes
- `plugins/resources/retrieval-dataset-gtex`, `plugins/resources/retrieval-dataset-cbioportal`
- `plugins/resources/retrieval-literature-semantic-scholar`, `plugins/resources/retrieval-knowledge-uniprot`

`computer-use` intentionally remains in the Omiga app repository because it contains platform-specific automation binaries and tighter app/security coupling. `plugin-creator`/developer tooling is also kept in the Omiga app as a built-in bootstrap skill rather than a marketplace plugin.

## Validate

```bash
python3 scripts/validate_marketplace.py
```

## Refresh this repo from a sibling Omiga checkout

```bash
python3 scripts/sync_from_omiga.py --omiga ../omiga
python3 scripts/validate_marketplace.py
```

## After uploading to GitHub

1. `marketplace.json` already points at `dxsbiocc/omiga-plugins`; adjust it only if you fork or transfer the repo.
2. Use the raw GitHub URL from the `remote` object for Omiga update checks.
3. Tag plugin-compatible releases, for example `marketplace-v0.1.0`.
4. Omiga can then run remote marketplace update checks against the raw GitHub URL.

See `docs/MARKETPLACE.md` for operating policy.
