# Validation

```python
report = icon.validate_icon()   # .status: valid | invalid | review; .errors; .warnings
print(report.describe())
```

Eight checks, fixed order, all run: 1 schema/profile (family owns profile), 2 style/grid (integers, stroke 4, round caps and joins), 3 canvas and keyshape bounds, 4 MIC clearance (2 / 4 / 2 ink for SUB32 / SOLO48 / CONTAINER64), 5 keyshape token resolves, 6 composition, 7 SVG round-trip, 8 byte-identical re-render. Every failure names the element and coordinates.

**`review` is not a pass.** It means a curve sits so close to the minimum that the engine cannot certify it. It is a warning and blocks release. Give curves real margin. Exact axis separation of unrotated cardinal quarter or half ellipses and Bezier hulls can be certified; anything else needs slack.

**Whole-drawing parallel straight edges** must be 8 apart on centerlines (4 ink) in every family, including two runs inside one contour. Shared ink and `connect` do not exempt them. Curves and near-parallel edges stay advisory.

**Small-circle hole exception.** Complete circles of centerline diameter exactly 4 or 6 pass hole QA even if the hole is under minimum. Only full circles; not squares, ellipses or fragments.

**Repair loop.** Read the finding. Fix the model, never the SVG. Re-run the whole chain, since every repair moves paint and can break the keyshape. Look at native size. Crowding ladder: enlarge the opening, then rebalance, then remove the part. Never squeeze.

**Never:** change a profile constant, keyshape dimension, tolerance or `numeric_epsilon`; move to another family's folder or base; declare `connect` on parts that do not touch; add a `FREE` record to dodge a repair; edit a report; patch emitted SVG. If it cannot pass, name the check and element and stop.

```bash
python3 -m unittest discover -s icon_set/tests -t .
python3 icon_set/scripts/build.py --family solo            # validates then exports to dist/solo48/
python3 icon_set/scripts/contact_sheet.py --family solo --theme dark --png /tmp/solo.png
python3 icon_set/scripts/report_parallel_failures.py       # parallel-edge failures only
```
