---
name: font-maker
description: Design, revise or check a stroke-based (monoline) font on any grid and set of conditions - capitals, lowercase and digits drawn as SVG centerline strokes with one stroke width, a minimum-gap rule between strokes, real-font proportions and typographic guide lines. Use when asked to make letters, digits or a typeface for icons or a grid, add lowercase to an existing set, rework glyphs to a spacing or style rule, round off sharp corners, or check glyphs against proportion, spacing and guide-line rules. Hand-authored; edit this file directly.
---

# Font maker

Build stroke fonts the way the official Pictographic letters were built (`Letters/official`):
fix the conditions, work out what the grid can hold, measure real fonts, draw centerlines,
check every glyph with the tools here, look at it at the real size, and test it in context.

Tools are in `scripts/` next to this file (Python 3 with `svgpathtools`, `numpy`, `Pillow`,
`scipy`; `rsvg-convert` for rendering). Construction techniques and the decisions behind the
Pictographic set are in `references/construction.md`; read it before drawing.

## 1. Fix the conditions

Get these from the request, the existing glyphs or the surrounding system. Ask only for what
changes the drawing and cannot be read from the material.

| Condition | Pictographic example | Notes |
| --- | --- | --- |
| Grid and canvas | 19 × 19 caps, 19 × 25 lowercase | Same width per glyph where possible |
| Stroke | 4, round caps and joins | One weight everywhere |
| Cap height | centerline y 2 to 17 | Ink adds half a stroke each side |
| Gap rule | 4 units of white between parallel strokes | Ask which strokes it covers; default parallel only |
| Character set | A-Z, a-z, 0-9 | Plus symbols if asked |
| Style | rounded, condensed, soft tips | From existing glyphs or a reference |
| Target size | 48 px icons | Every visual check happens at this size |

## 2. Work out the budget before drawing

Stroke fonts fail on stacking, so do the arithmetic first and tell the user which glyphs cannot
meet the rule at this size.

- `k` strokes stacked with the minimum gap need `k × stroke + (k - 1) × gap` units of ink.
  Two stems: 12 at stroke 4 and gap 4. Three bars (E, B, 3, 5, 8, e): 20.
- Compare with the cap height, the x-height and the space between x-height and ascender.
  At Pictographic size the cap ink is 19, so two stacked counters miss by 1 unit, and e misses
  by a lot in a 10-unit x-height.
- The narrowest glyph with two parallel sides is `2 × stroke + gap` wide. That floor can push
  digits and n wider than real fonts; report it as forced.
- An exception is a stated result, never a silent one. Split the space evenly so the shortfall is
  shared, and list every exception with its measured gap.

## 3. Measure real fonts

```
S=.claude/skills/font-maker/scripts
python3 $S/measure_reference.py --out /tmp/reference.json        # or --font path[:face] ...
```

Pick reference fonts close to the target: weight (stroke / cap height), rounded or not,
condensed or not. The JSON gives width ratios (to H or n) and guide lines as fractions of cap
height: x-height, ascender, descender, t and f crossbars, i stem top and dot, t top. Convert
those fractions to your grid and fix the lines before drawing lowercase.

## 4. Draw centerlines

- Coordinates are stroke centerlines. Ink extends half a stroke past them.
- Every glyph of a case shares a canvas and a baseline. Lowercase uses a taller canvas for
  descenders and keeps the capitals' baseline and cap line.
- Sit glyphs exactly on the guide lines: ascender, x-height, baseline and descender. t and f
  crossbars sit on the x-height. i and j stems start on the x-height, and the dot's top sits on
  the ascender line. g's bowl sits on the baseline like a and q.
- Build lowercase with the capitals' vocabulary: the same bowl shapes, terminal treatment and
  corner treatment. Compare each pair side by side (Oo, Cc, Dd, Ee, Ff, Tt).
- For soft vertices use `scripts/rounded.py`. It places a circle on the centerline so the inside
  of the corner rounds too, and keeps the letter's height when the circle touches the guide line.
- Draft in a script that writes every SVG, so a change to a metric regenerates the whole set.
  Back up the previous set before overwriting.

## 5. Check every glyph

```
python3 $S/check_parallel.py --min-gap 4 <glyph folder>
python3 $S/check_proportions.py --reference /tmp/reference.json <glyph folder>
python3 $S/render_sheet.py <glyph folder> --px 48 160 --lines 2 7 17 22.5 \
    --words "Hamburgefonstiv" "The quick brown fox" --out /tmp/sheet.png
```

- `check_parallel.py` reports the tightest parallel pair per glyph. Two identical curves exactly
  at the minimum can read a few hundredths short from sampling; confirm with `--angle 5` before
  calling it a failure.
- `check_proportions.py` prints each width against the reference range and the ordering rules
  every reference agrees on. It also prints each glyph's ink centre.
- Look at the sheet at the target size. Passing numbers do not prove a glyph reads; a blob with
  a 1-unit slit passes nothing and reads badly. Show options side by side when a fix has a style
  cost, and pick the one that reads.

## 6. Test in context

Lay words out with the gap rule between letters and put them where they will be used: inside
frames, beside icons, at the real size. Measure the white from letters to the frame as well as
between letters. In this repository:

- Real frames come from the icon model (`icon_set/model/icons/container`, `.../solo`). Strip their
  own content before placing text.
- Side pairs with text subs are built by the site's engine,
  `icon_set/scripts/templates/combine-side.js` (`CombineSide.render(row, request)` in Node), with
  rows from `published/gallery/experiment-combination.json`. Native text subs use
  `sizing_mode: 'typeface-native'`; rebuild one from the old glyphs first and confirm it matches
  production before comparing new glyphs.
- Wider glyphs can grow a pair's canvas past 64 and frames can be too small for full-height text.
  Report both; they are size limits, not letterform faults.

## 7. Deliver

- One folder with `uppercase/`, `lowercase/` and `digits/` subfolders. `A.svg` and `a.svg` collide
  on a case-insensitive file system.
- A README with the canvas, stroke, guide lines, rules and every exception with its measured gap,
  plus a preview sheet.
- For changes, a before and after view at the real size, and the previous files kept.
- Do not commit, publish or rebuild shared generated data unless asked. In this repository the
  capitals and digits feed `icon_set/typeface/glyphs-v2.json` through
  `icon_set/scripts/build_typeface.py` from `Letters/new`; it does not read lowercase.
