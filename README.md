# omiga-plugins

Curated Omiga plugin marketplace. This repository is intended to become the remote, independently versioned source of truth for domain plugins while the Omiga app keeps only a minimal bundled snapshot for offline bootstrap.

## Layout

```text
marketplace.json                 # local/static marketplace manifest
marketplace.remote.example.json  # GitHub remote metadata example
plugins/                         # plugin packages
source_runners/                  # shared retrieval/source runner code
schemas/                         # lightweight JSON schemas
scripts/                         # validation and sync helpers
docs/                            # marketplace operating notes
```

## Included initial plugins

- `transcriptomics` — analysis templates for differential expression, PCA, enrichment
- `ngs-alignment` — NGS alignment/post-alignment operators
- `source-ncbi` — aggregated NCBI source routes
- `source-embl-ebi` — EMBL-EBI source routes
- `visualization-r` — R visualization templates
- `operator-seqtk` — FASTQ/FASTA subsampling operator
- `retrieval-dataset-gtex`, `retrieval-dataset-cbioportal`
- `retrieval-literature-semantic-scholar`, `retrieval-knowledge-uniprot`
- `omiga-developer-tools` — developer skills such as plugin creation

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
