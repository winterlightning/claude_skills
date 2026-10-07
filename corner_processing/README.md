# corner_processing — round and sharp corners for 48×48 stroke icons

The processing scripts only: no review pages, tools or 3D. (The full working folder with
reports, review locks and history is `../corner_rounding/`.)

```bash
pip install -r requirements.txt          # plus rsvg-convert (brew install librsvg)

python3 round_corner_processing.py       # every icon -> outputs/round/*.svg
python3 sharp_corner_processing.py       # every icon -> outputs/sharp/*.svg
python3 sharp_corner_processing.py --files add-tab.svg     # chosen icons
python3 sharp_corner_processing.py --sample 100            # random sample
python3 sharp_corner_processing.py --help                  # all options
python3 -m core.fetch                    # fetch the approved icon set again first
```

Input: `../solo-20261001/svg/` (change with `--input`). Output: `outputs/` — the SVGs,
`corners48.json` (detection), `toggle.json` (what was done per corner + the check),
`keyshapes.json`. Paths are set in `core/paths.py`.

## Rules (current defaults)

**Round output** — every corner with straight sides is made sharp, then re-rounded with a
whole-number radius by angle: ≤ 60° → r 1, < 75° → r 2, < 105° → r 4, < 180° → r 6. A drawn
round bigger than r 8 is a designed curve and keeps its shape; so does one with no room to re-round.

**Sharp output**
- Round corners with two straight sides up to r 6 become sharp; bigger ones (up to r 8) too when
  their sharp point sits within 1 u of the drawn curve (`--soft-gap`). Curved-side rounds stay.
- Mitre joins, limit 4 (full points down to 29°). Ink that leaves the keyshape is sliced flat
  along the keyshape edge (`--miter slice`); each side may reach as far as the input does there.
- Flat ends, lengthened up to 2 u (the reach of the round cap), never past the keyshape; ends
  on another stroke, a dot or a circle stay flush. Dots become 4×4 squares.
- A sharpened corner another stroke would cross stays round.

Every output is re-detected and compared with the input (`check` in `toggle.json`: ok /
contact / fail).

## core/

| file | does |
|---|---|
| `detect.py` | corner detection → `corners48.json` |
| `toggle.py` | the round and sharp outputs + the check → `round/`, `sharp/`, `toggle.json` |
| `keyshape.py` | each icon's keyshape from its ink (needs `../../claude_skills` for the declared one) |
| `keyshape_fit.py` | keyshape geometry the sharp output slices against |
| `pipeline.py` | the steps the two entry scripts run |
| `fetch.py` | re-download the approved icons from the review Worker (re-applies `input_fixes/`) |
| `locks.py` | review locks (`locks.json`, optional: `--ready` / `--reviewed`) |
| `svg_io.py`, `progress.py`, `paths.py` | SVG reading, progress lines, folders |
