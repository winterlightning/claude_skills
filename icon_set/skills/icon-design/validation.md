# Validation and repair

```python
report = icon.validate_icon()
report.status      # "valid" | "invalid" | "review"
report.errors      # blocking
report.warnings    # uncertified -- also blocking for release
print(report.describe())
```

## The chain

Eight checks in a fixed order. Later checks still run after an earlier failure,
so one pass gives a complete picture, except where a failure makes a later
measurement meaningless.

| # | Check | What it proves |
|---|---|---|
| 1 | `schema/profile` | Required fields, valid enums, geometry present, `FREE` approved, **family owns the profile** (`sub`→SUB32, `solo`→SOLO48, `container`→CONTAINER64) |
| 2 | `style/grid` | Integer coordinates, stroke 4, round cap and join, grid 1 |
| 3 | `canvas/keyshape bounds` | Ink inside the canvas and matching its keyshape envelope |
| 4 | `mic` | Vector clearance between distinct parts meets 3 / 4 / 4 |
| 5 | `keyshape` | The token resolves by exact 1x / 1.5x / 2x arithmetic for SUB32 / SOLO48 / CONTAINER64 |
| 6 | `composition` | Roles, class template, child profiles and positions |
| 7 | `svg round-trip` | Exact viewBox, canonical style, no transform, reparses identically |
| 8 | `reproducibility` | Two renders of one model are byte-identical |

Every failure names the element id and the actual coordinates. Read those before
changing anything — the message tells you which part, and where.

## `review` is not `pass`

The clearance engine returns three verdicts. `review` means it could not certify
the result within its numerical bounds — usually a curve sitting exactly on the
minimum. It appears as a **warning**, and the corpus test asserts that no
shipped icon produces one.

Treat a warning as a failure. Give the geometry real margin.

## Small-circle hole exception

Build-time hole QA accepts complete circles whose **centerline diameter** is
exactly 4 or 6 units (4×4 or 6×6, radius 2 or 3), even if their enclosed hole
fails the usual minimum. This is a user-approved rule in
`icon_set/model/contracts/negative-space.v1.json`, not an author-created waiver.
It covers circular contours made of arcs as well as explicit SVG circles.
Reports preserve the measured failure and record the circle exception.

The exception applies only to a complete circular region: a small square,
ellipse, or fragment created by a stroke crossing a circle still fails.
Spacing, pinch, canvas, and keyshape checks are unaffected.

## The repair loop

1. Read the finding: which element, which coordinates, which check.
2. Repair the **model**, never the emitted SVG.
3. Re-run the whole chain. A repair that fixes clearance can break the keyshape,
   because every repair moves paint.
4. Look at it again at native size.

The ladder for a crowded region is in
[authoring.md](authoring.md#when-a-gap-is-too-small-give-it-room).

## Never do these

Not to make a check pass, not as a shortcut, not with a justification:

- change a profile constant, a keyshape dimension, or a tolerance;
- move an icon to another family's folder, or subclass another family's base,
  to get a bigger or smaller canvas — the registry refuses it, and if it did
  not, the validator would;
- raise `numeric_epsilon` — it absorbs float error, nothing else;
- edit a report, or describe a `review` as a pass;
- declare `connect` on a pair that is not genuinely connected, to silence a
  clearance failure;
- add a `FREE` record to escape a repair;
- patch the emitted SVG.

If an icon cannot be made to pass, say so, say which check and which element,
and stop. A reported blocker is a good outcome. A quietly weakened rule is not.

## Commands

```bash
python3 -m unittest discover -s icon_set/tests -t .
python3 icon_set/scripts/build.py                    # validate, then export every family
python3 icon_set/scripts/build.py --family solo      # one family only
python3 icon_set/scripts/contact_sheet.py --family solo --theme dark --png /tmp/solo.png
```

The build script validates before it exports, so nothing reaches `dist/` that
has not passed. Each family ships to its own folder with its own manifest —
`dist/sub32/`, `dist/solo48/`, `dist/container64/` — and a family's manifest
lists one profile only. It prunes outputs for icons that no longer exist, and
re-running it produces a byte-identical tree.
