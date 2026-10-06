# Pictographic letters: official set

The official stroke letters for the icon system: 26 capitals, 26 lowercase letters and 10 digits.
Every glyph is an SVG whose strokes are its centerlines.

| Folder | Glyphs | Canvas |
| --- | --- | --- |
| `uppercase/` | A to Z | 19 × 19 |
| `digits/` | 0 to 9 | 19 × 19 |
| `lowercase/` | a to z | 19 × 25 (m is 20 × 25) |

Capitals and lowercase are in separate folders because `A.svg` and `a.svg` cannot share a folder
on a case-insensitive file system. `Letters/new` stays the source that
`icon_set/scripts/build_typeface.py` reads for capitals and digits.

## Style

- Stroke 4, round caps and joins, one stroke weight everywhere.
- Rounded construction. Bowls are pills or D shapes (O, D, P, o, b, d, p, q), terminals are
  flat (C, c) or curved (f, t, l, j, a), and the sharp vertices of M, N, V and v end in small
  round tips built as circles on the centerline.
- Condensed proportions, close to DIN: H, n and the round letters are 12 units of ink wide.

## Guide lines

Centerline positions, measured against Arial Rounded Bold, Helvetica Bold, DIN Alternate Bold
and Arial Bold.

| Line | y | Fraction of cap height (ink) | Glyphs on it |
| --- | --- | --- | --- |
| Ascender and cap height | 2 | 1.00 | capitals, b d h k l f, the i and j dot |
| x-height | 7 | 0.74 | tops of o n x v w z s e c r u, bowls of a b d g p q, i and j stems, t and f crossbars |
| Baseline | 17 | 0 | every glyph |
| Descender | 22.5 | 0.29 below | g j p q y |

## Rules

- **4-unit rule.** Parallel strokes keep at least 4 units of white, 8 apart centre to centre.
  Diagonals meeting at a joint are not parallel and do not count.
- **Real-font widths.** I is the narrowest capital and W the widest, M is wider than N, 0 is
  narrower than O, 1 is the narrowest digit, m and w are the widest lowercase, and so on.
  `check_proportions.py` in the font-maker skill lists all of them.

## Known exceptions

The 19-unit capitals and the 5 units between x-height and ascender cannot hold every stacked shape
at stroke 4. These glyphs are as open as the space allows:

| Glyph | White between parallel strokes | Why |
| --- | --- | --- |
| B, E, 3, 5, 8 | 3.1 to 3.5 | Two stacked counters need 20 units; the cap is 19 |
| e | 0.9 | Top, bar and bottom need 16 units; the x-height is 10 |
| f | 1.0 | Hook and crossbar share the 5 units above the x-height |
| g | 1.4 | Hook sits on the descender line under a full bowl |
| i, j | 1.0 to the dot | Dot on the ascender line, stem on the x-height (not a parallel-stroke gap) |
| m | exactly 4 | Needs a 20-unit canvas for three stems 8 apart |

## Source

`source/lowercase.py` draws every lowercase glyph from its paths and the guide lines above.
Change a path or a metric there and rerun it rather than editing the SVGs by hand:

```
python3 Letters/official/source/lowercase.py
```

## Checking

From the repository root:

```
S=.claude/skills/font-maker/scripts
python3 $S/check_parallel.py --min-gap 4 Letters/official
python3 $S/measure_reference.py --out /tmp/reference.json
python3 $S/check_proportions.py --reference /tmp/reference.json Letters/official
python3 $S/render_sheet.py Letters/official --px 60 --lines 2 7 17 22.5 --out preview.png
```
