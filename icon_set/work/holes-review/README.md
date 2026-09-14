# Opening repair review — original 65-icon batch

The user approved the first cathedral fix, then requested all 65 repairs before batch review. All 65 candidate models pass the negative-space check. 13 pass all blocking validation; 52 retain other findings. No original source module was edited. No candidate was applied to the production failure gallery.

Open review.html for the self-contained comparison. mapping.json links every original to its independent candidate. notes.json explains the changes. results.json stores full candidate measurements; baseline-validation.json stores original geometry errors and warnings. review-manifest.json records the review status. The variants were created with create_variant.py, and geometry was edited in Python, never in emitted SVG. All authorship/source metadata is retained.

The live gallery changed during this work from 1,035 failures / 65 hole icons to 1,462 failures / 88 hole icons. This batch remains the original 65 in queue.json; do not silently expand it or overwrite unrelated gallery changes.

After user review, apply approved repairs using the repository workflow, revalidate and regenerate the relevant build/report. A hole repair alone must not hide remaining bounds or spacing failures. Preserve the originals and avoid duplicate variant creation. The first cathedral repair was already approved. Check for source changes since this review before applying anything.

Validation: all candidate negative-space reports pass; no candidate has more spacing findings than its original under current validation. Native previews inspected in light and dark themes. Registry variant validation passes. The earlier full test run failed across the existing library (321 tests, 4,077 failures, 41 errors, 1 skipped); no clean full build is claimed.

## Latest user revisions

Nine selected icons have new independent candidates in revision-2-mapping.json; all nine now pass geometry validation and negative-space QA with zero errors or warnings. The user confirmed retaining the designs of Pisa, paw-print-v2, tuk-tuk, crawling-baby, and curled-raccoon while resolving the remaining rules. Pisa geometry is exactly unchanged; it now uses SQUARE. User-with-gear is excluded from the review via excluded.json, with its source preserved.

The current page defaults to Latest revisions (9), comparing previous drafts to the new candidates. The full batch now contains 64 icons: 22 fully pass and 42 retain other findings. Original batch JSON and HTML are preserved under revision-1/. No production failure gallery rebuild was requested or performed. Do not rerun repair_batch.py over these later revisions. The latest revision sources are authored by revise_selected.py, and the current review is emitted by make_gallery.py.

Visual QA: all nine inspected enlarged and at 48px in both themes. Browser refresh was unavailable because the browser tool blocks file URLs; the HTML itself was generated and checked locally.
