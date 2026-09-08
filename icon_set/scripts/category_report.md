# Category comparison reports

Run from the `claude_skills` repository root:

```sh
python3 icon_set/scripts/category_report.py computers --full-qa
```

Open `work/reports/computers/index.html`. The HTML contains its images, source
code, data, styles and interactions, and can be opened locally or shared as one
file. `report.json` is a compact inventory for other tools. Generating a report
does **not** change source images, Python models, or exported files.

## Other categories

```sh
python3 icon_set/scripts/category_report.py culture
python3 icon_set/scripts/category_report.py computers culture --out work/reports/selection
python3 icon_set/scripts/category_report.py --all
```

`--all` includes every directory under `pictographic-primitives`, including
categories with no authored icons. Large reports paginate their cards in the
browser. A category directory path can be used instead of a category name.
`--source-root`, `--dist` and `--out` override the source, export and output
folders. Defaults are anchored to the repository, so the script also works
when launched from another directory.

## What is compared

Each entry shows the complete original SVG, the SVG freshly rendered from its
Python model, and the current file in `icon_set/dist/<profile>/`. Original SVG
styles are retained during rasterization. Images use their full square canvas;
there is no silhouette fitting, stroke normalization, or automatic visual score.
Inspect mode includes an original/model opacity blend, native-size previews,
source paths, author notes, Python source, and SVG downloads.

Matching uses the exact `SOURCE_ICON_ID` first, then explicit duplicate IDs in
`SOURCE_REFERENCES`, then `SOURCE_PATH` and declared reference paths. A module
can reuse one drawing for several originals by recording
`SOURCE_REFERENCES = (("source-id", "source/path.svg"), ...)`. The report keeps
each original and its ID visible, labels reused drawings, and counts unique
drawings separately from source coverage. It never infers reuse from a title. A manifest's
exact `icon_id` is a fallback only for old models lacking both metadata fields.
A conflicting source ID is never overridden by a name. Duplicate copies of an
ID are grouped; differing contents are flagged. Multiple family drawings for
one source remain separate entries. Source totals count unique originals;
status totals count entries. Actual model families take precedence over old
manifest classifications.

## Check status

- **Ready:** current model validation passes, its exported SVG is byte-identical,
  and the export's manifest hash matches.
- **Needs attention:** a model check, source-copy conflict, missing export, stale
  export, or manifest mismatch needs attention.
- **Pending:** no matching Python model exists.
- **Error:** a source or model could not be inspected.

Default runs perform current model validation. `--full-qa` additionally runs the
library's hole/pinch checks; it takes longer. The page labels the check level.
These technical checks do not grant visual approval. The report never changes
validation rules or runs a family build to hide stale exports. Rebuild the
relevant family and rerun the report when appropriate.

## Human review

Filter by category, batch, checks, reused/primary mapping, or review decision; search names, IDs, and
keywords. Mark entries Approved or Rework and add notes in Inspect. Reviews are
saved to browser local storage and can be exported/imported as JSON. Export
reviews before moving the HTML to another browser or machine. Drawing hashes
keep an approval from silently carrying over when the Python drawing changes;
the entry becomes Drawing changed until reviewed again. Storage is browser-local,
not written back to the report or icon files.

The reusable presentation lives in `templates/category_report.html`; generator
logic and identity matching live in `category_report.py`. Neither contains
category-specific icon lists.
