# Construction notes

Techniques and decisions from building the Pictographic letters (`Letters/official`). Use them
as defaults for a rounded monoline set; a different brief can overrule any of them.

## The gap rule

- It applies to parallel strokes: two stems, stacked bars, the top and bottom of a bowl, a bowl
  side and a stem. Measure centre to centre; white = distance - stroke.
- Diagonals meeting at a joint (N, M, V, K, A, W) leave thin wedges that do not count.
- A tail tangent to a bowl has only one parallel partner, the far side of the bowl a full
  bowl-width away, so it passes where a hooked tail under the bowl fails (used for 6 and 9).
- Curved corners near the minimum need margin: an oval bowl only reaches the full gap at one
  point (D was redrawn with a straight side for this).

## Shapes that worked

| Need | Construction |
| --- | --- |
| Round letters that match condensed caps | Pills and D shapes with straight sides (O, D, o, b, d, p, q), not circles or ellipses |
| Soft vertex | Circle on the centerline touching the guide line, radius 1 to 1.5 at stroke 4 (`rounded.py`). Larger reads as U, or breaks narrow letters |
| Terminals | Flat horizontal where the capital is flat (C, c); curved feet and hooks elsewhere (f, t, l, j) |
| a | Single storey, a full half-circle back; double storey cannot fit a small x-height |
| e | Horizontal bar; a diagonal bar was rejected by the user even though it read slightly better |
| g | Single storey with a hooked tail to the descender line |
| 1 | Flag and stem, no base: it must be the narrowest digit, and the flag tells it from I |
| 0 and O | O wider than 0, so they differ by proportion as in real fonts |
| l | Short curved foot so it differs from I and L |
| m | Needs `3 × stroke + 2 × gap` of ink; give it a wider canvas rather than squeeze the gaps |

## Proportions

Real-font ratios that held across Arial Rounded Bold, Helvetica Bold, DIN Alternate Bold and
Arial Bold: I narrowest capital, W widest, M wider than N, A, V and O at least H, E narrower than
H, F and L narrower than E and about equal, J narrower than H, 0 narrower than O, 1 narrowest
digit, digits about 0.85 of H; i narrowest lowercase, m and w widest (about 1.6 of n), o at least
n, f j r t narrower than n. The stroke-gap floor makes H, n and digits 12 units of ink at
stroke 4, which is wider than real fonts; that is forced, not a mistake.

## Guide lines (fraction of cap height, ink)

x-height 0.71 to 0.74; ascender 1.00; descender 0.27 to 0.30 below the baseline; t top 0.93 to
0.98; t and f crossbar top on the x-height; i stem top on the x-height, dot top on the
ascender. Round letters overshoot by 0.01 to 0.03 in real fonts; the Pictographic set sits exactly
on the lines like its capitals.

## Process lessons

- Show the user options at the real size when a fix trades a rule against legibility, and let
  them choose the trade. State shortfalls with numbers.
- Keep generated previews and scratch files out of the repository unless asked; `/tmp` can be
  cleared between sessions, so keep scripts that regenerate the set next to the glyphs.
- A width change ripples into word layouts and pair canvases; rerun the in-context test after
  every change to widths.
