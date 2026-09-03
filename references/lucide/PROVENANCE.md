# Lucide construction references

This is a local, offline reference snapshot copied on 2026-09-03 from the
user-provided sibling `analyze_lucide` dataset. It contains 1,798 original SVGs
and their 1,798 generated atomic-debug views. The upstream commit/version of
that dataset was not recorded; do not claim this is a version-pinned release or
the latest Lucide collection. Per-file SHA-256 hashes in `index.json` identify
the exact imported snapshot.

- `original/`: unchanged original icon geometry and source element grouping.
- `atomic-debug/`: generated colored LINE/ARC/QUAD/CUBIC segment views, copied
  unchanged. Use these to inspect construction, not as production SVGs.
- `index.json`: searchable names/keywords, paths, counts, and content hashes.
- `LICENSE`: Lucide's ISC notice and the Feather-derived icons' MIT notice,
  retrieved from https://raw.githubusercontent.com/lucide-icons/lucide/main/LICENSE
  on 2026-09-03. Retain these notices when distributing the reference corpus.

The debug decomposition is not a record of a designer's original workflow.
For example, its analyzer splits native circles into four quarter-arcs. Colors
are assigned sequentially within each icon, not by semantic meaning. Splitting
one contour into many debug paths does not improve the drawing or set a desired
part count. Original SVGs remain the appearance and grouping reference.

Read a few relevant pairs, not the whole corpus. Query the local index with
`python3 core/lucide_reference.py search 'subject or construction' --limit 6`,
then inspect an exact match with `python3 core/lucide_reference.py inspect house`.
The `--json` form includes original attributes and exact absolute segment paths.
Run `python3 core/lucide_reference.py index` only when intentionally refreshing
the index from this paired snapshot.

The source subject/brief remains authoritative. Lucide is a style/construction
reference, not permission to add an unrelated feature or substitute an icon.
See the maintained project workflow in `docs/shared/icon-pipeline.md` and the
official guide at https://lucide.dev/contribute/icon-design-guide.
