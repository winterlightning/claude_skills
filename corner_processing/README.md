# corner_processing — round and sharp corners for 48×48 stroke icons

The processing scripts and their review pages; no tools or 3D. (The older working folder with
history is `../../corner_rouding_detection/corner_rounding/`.)

```bash
pip install -r requirements.txt          # plus rsvg-convert (brew install librsvg)

python3 round_corner_processing.py       # every icon -> outputs/round/*.svg
python3 sharp_corner_processing.py       # every icon -> outputs/sharp/*.svg
python3 sharp_corner_processing.py --files add-tab.svg     # chosen icons
python3 sharp_corner_processing.py --sample 100            # random sample
python3 sharp_corner_processing.py --help                  # all options
python3 -m core.fetch                    # fetch the approved solo icons again first -> input/solo48/
python3 -m core.apply_review             # write the corner review's sharp decisions into outputs/solo48/sharp
python3 -m core.publish --user jakes     # store the outputs as round / sharp icon records (review site)
```

Input: `input/solo48/svg/` (change with `--input`). Output: `outputs/` (whole-set runs use
`--out outputs/solo48`) — the SVGs,
`corners48.json` (detection), `toggle.json` (what was done per corner + the check),
`keyshapes.json`. Paths are set in `core/paths.py`. `input/` and `outputs/` are git-ignored.

**On the review site** each output is its own icon, `<key>--round` / `<key>--sharp`, with **Style** round or sharp
beside its family (the gallery's Style filter; every other icon is Normal). It starts Ready; an icon whose check
failed is in the Failed tab. `core/publish.py` sends only drawings that changed.

## Rules (current defaults)

**One decision per round corner** — round and sharp decide every drawn round corner together: it is
a corner in both (re-rounded / sharpened) or kept as drawn in both. A round corner either output keeps
(too large, no room to re-round, a sharp point crossing a stroke, no corner left after sharpening) is kept
in the other too (`process_icon` rebuilds both until neither finds another; `shared_keep` in
`toggle.json`). Every run therefore builds both outputs and writes the one asked for.

**Round output** — every corner with straight sides is made sharp, then re-rounded with a
whole-number radius by angle: ≤ 60° → r 1, < 75° → r 2, < 105° → r 4, < 180° → r 6. A drawn
round too large for a corner (the sharp output's rule below) keeps its shape; so does one with no room to re-round.

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

## Review pages

Every run ends by rebuilding two self-contained pages in its output folder (skip with `--no-report`):
`toggle48_report.html` (input → corner detect → all round → all sharp, one row per icon) and
`corner48_report.html` (detection only). Round and sharp are separate runs here, so an icon may
have only one output so far: its other plate says "not built yet" and the Round / Sharp not built
filters list them. Filled shapes (dots, arrowheads, backdrops) are drawn as the outputs copy them.

```bash
python3 reports/make_toggle48_report.py        # rebuild by hand (outputs/solo48 or outputs/, whichever ran last)
python3 reports/serve_report.py                # http://127.0.0.1:8748/toggle48_report.html; Lock in saves locks.json
python3 reports/serve_report.py --port 8749    # when the old folder's server already holds 8748
```

## core/

| file | does |
|---|---|
| `detect.py` | corner detection → `corners48.json` |
| `toggle.py` | the round and sharp outputs + the check → `round/`, `sharp/`, `toggle.json` |
| `keyshape.py` | each icon's keyshape from its ink (needs `../../claude_skills` for the declared one) |
| `keyshape_fit.py` | keyshape geometry the sharp output slices against |
| `pipeline.py` | the steps the two entry scripts run |
| `fetch.py` | re-download the approved icons from the review Worker (re-applies `input_fixes/`) |
| `apply_review.py` | the AI corner review's sharp fixes (review/decisions.jsonl) written into the sharp outputs; run after processing, before publish |
| `publish.py` | store the round / sharp outputs as icon records (Worker `POST /api/icons/styled`) |
| `locks.py` | review locks (`locks.json`, optional: `--ready` / `--reviewed`) |
| `svg_io.py`, `progress.py`, `paths.py` | SVG reading, progress lines, folders |
