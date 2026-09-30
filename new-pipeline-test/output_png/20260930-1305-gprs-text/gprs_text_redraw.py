"""gprs-text (redraw of the new-pipeline traced SVG, run 20260930-1305).

Plan: the word "GPRS" set in the stored typeface, never traced letters.
- text: the typeface v2 capitals G, P, R, S (icon_set/typeface/glyphs-v2.json,
  native 20 canvas, cap height 15, centerline width 8 each, stroke 4),
  reused verbatim and only translated by whole units, as
  icon_set/scripts/side_text.py lays out native text: 4 ink (8 centerline)
  between neighbouring glyph boxes, 4 ink between lines.
- layout: one row cannot fit. 4 x 8 + 3 x 8 = 56 of centerline width against
  40 on the widest SOLO48 box (HRECT_M / HRECT_L), and the typeface may not be
  scaled or tracked tighter than its 4-unit ink gap. So the word is set in
  two lines, "GP" over "RS", read in order left to right, top to bottom.
  The block is 8 + 8 + 8 = 24 wide and 15 + 8 + 15 = 38 tall on
  centerlines, mirrored about (24,24): glyph columns x 12-20 and 28-36,
  rows y 5-20 and 28-43 (ink x 10-38, y 3-45).
- keyshape: VRECT_M (centerline box (10,4)-(38,44)) instead of the suggested
  HRECT_M; the two-line block is tall and narrow, and VRECT_M is the
  tightest box that contains it. It does not reach the box extremes exactly
  (2 short on x each side, 1 on y each side) because the glyphs cannot be
  stretched.
- dropped: nothing; all four letters stay.

Metric issues:
- fixed: stroke-width (info; glyphs are drawn at stroke 4), all six
  clearance errors (e0/e4, e0/e5, e1/e3, e1/e5, e2/e3, e2/e5: the traced
  letters were 2.8-6.3 apart; the glyphs are now 8 apart on centerlines in
  both directions), and the four enclosed holes at [8.9,21.1], [19.8,20.8],
  [29.7,20.9], [39.5,27.0] (trace blobs in the G, P, R and S; the P and R
  bowls are now the glyphs' own 8 x 8 counters, G and S are open).
  The P and R stems, bowls and leg meet at the glyphs' own shared nodes;
  those in-glyph contacts are declared with relate("connect").
- not fixed: keyshape-short-axis. The metric asks to stretch the trace by
  2.13 on y to fill HRECT_M; the typeface may not be scaled, and on VRECT_M
  the fixed-size block leaves x 2 and y 1 short of the box (rectangle fit
  tolerance is 0). The stored glyph nodes are also off the integer grid,
  so validate_icon() stops at the grid check; the typeface is validated as
  native text, not as SOLO48 geometry. One advisory remains: the R leg
  and the S are 8.0002 apart (stored R node x 12.9998), i.e. on the minimum.
Lucide: no useful match (Lucide has no lettering icons); typeface reuse only.
"""
import json
from pathlib import Path

from svgpathtools import CubicBezier, Line as SvgLine, parse_path

from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.primitives import Bezier, Line, Point

SOURCE_ICON_ID = "378a8b67-3065-5023-b054-9fccecc32c2c"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1305-gprs-text/gprs-text_raw.svg"
AUTHOR = "claude-opus-5-5"

LINES = ("GP", "RS")                       # "GPRS" in reading order
GLYPH_W, CAP = 8, 15                       # v2 centerline width / cap height
TRACK = 8                                  # centerline gap = 4 ink
COL_LEFT = (24 - TRACK // 2 - GLYPH_W, 24 + TRACK // 2)       # 12, 28
ROW_TOP = (24 - TRACK // 2 - CAP, 24 + TRACK // 2)            # 5, 28
GLYPHS_JSON = Path(__file__).resolve().parents[3] / "icon_set/typeface/glyphs-v2.json"


def load_glyph(character):
    catalog = json.loads(GLYPHS_JSON.read_text())["glyphs"]
    return next(g for g in catalog if g["character"] == character and g.get("preferred", True))


class GprsTextRedraw(Solo48):
    icon_id = "gprs-text-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "text"
    aliases = ("gprs", "gprs-label")
    keywords = ("gprs", "mobile data", "2g", "network", "cellular", "text")

    def build(self) -> None:
        # Stored typeface paths, translated by whole units only.
        for row, line in enumerate(LINES):
            for col, character in enumerate(line):
                glyph = load_glyph(character)
                dx = COL_LEFT[col] - round(glyph["bounds"][0])
                dy = ROW_TOP[row] - round(glyph["bounds"][1])

                def pt(z, dx=dx, dy=dy):
                    x, y = (round(v, 6) for v in (z.real + dx, z.imag + dy))
                    return Point(*(int(v) if v == int(v) else v for v in (x, y)))

                contours = []
                for pi, d in enumerate(glyph["paths"]):
                    for qi, sub in enumerate(parse_path(d).continuous_subpaths()):
                        members = []
                        for si, seg in enumerate(sub):
                            name = f"{glyph['icon_id']}-{pi}-{qi}-{si}"
                            a, b = pt(seg.start), pt(seg.end)
                            if isinstance(seg, SvgLine):
                                self.primitives.append(Line(name, a, b))
                            elif isinstance(seg, CubicBezier):
                                c1, c2 = pt(seg.control1), pt(seg.control2)
                                self.primitives.append(Bezier(
                                    name, a, b, ((c1.as_tuple(), c2.as_tuple(), b.as_tuple()),)))
                            else:
                                raise ValueError(f"unsupported glyph segment {type(seg)}")
                            members.append(name)
                        contours.append(f"{glyph['icon_id']}-{pi}-{qi}")
                        self.add_contour(contours[-1], *members, closed=sub.isclosed())
                # The stored strokes of one glyph (P and R stem, bowl, leg)
                # meet at shared nodes: declare those contacts, nothing else.
                for i, a in enumerate(contours):
                    for b in contours[i + 1:]:
                        self.relate("connect", a, b)
