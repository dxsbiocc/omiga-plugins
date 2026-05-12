# omiga-plugins

Curated Omiga plugin marketplace. This repository is intended to become the remote, independently versioned source of truth for domain plugins while the Omiga app keeps only a minimal bundled snapshot for offline bootstrap.

## Layout

```text
marketplace.json                 # local/static marketplace manifest
marketplace.remote.example.json  # GitHub remote metadata example
plugins/                         # plugin packages grouped by official domain
  analysis/
  bioinformatics/
  visualization/
  sources/
  tools/
source_runners/                  # shared retrieval/source runner code
schemas/                         # lightweight JSON schemas
scripts/                         # validation and sync helpers
docs/                            # marketplace operating notes
```

## Included initial plugins

Official plugins are grouped by physical domain folder while keeping stable plugin IDs from `marketplace.json`:

- `plugins/analysis/transcriptomics` — analysis templates for differential expression, PCA, enrichment
- `plugins/bioinformatics/ngs-alignment` — NGS alignment/post-alignment operators
- `plugins/bioinformatics/operator-seqtk` — FASTQ/FASTA subsampling operator
- `plugins/visualization/visualization-r` — R visualization templates
- `plugins/sources/source-ncbi` — aggregated NCBI source routes
- `plugins/sources/source-embl-ebi` — EMBL-EBI source routes
- `plugins/sources/retrieval-dataset-gtex`, `plugins/sources/retrieval-dataset-cbioportal`
- `plugins/sources/retrieval-literature-semantic-scholar`, `plugins/sources/retrieval-knowledge-uniprot`
- `plugins/tools/omiga-developer-tools` — developer skills such as plugin creation

`computer-use` intentionally remains in the Omiga app repository because it contains platform-specific automation binaries and tighter app/security coupling.

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
