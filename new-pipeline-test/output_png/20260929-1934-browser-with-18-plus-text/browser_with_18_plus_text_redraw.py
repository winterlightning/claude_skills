"""browser-with-18-plus-text (redraw of the new-pipeline traced SVG, run 20260929-1934).

Plan: a wide browser window on HRECT_L (centerline box (4,8)-(44,40)) with
one title bar and the age mark "18" centred in the page area.
- frame: one closed rounded rectangle, r4 corners, mirrored about x=24, on
  all four HRECT_L extremes (x 4/44, y 8/40). Both walls are split at y=13
  so the title bar shares their endpoints; the contact is declared.
- title bar: one line (4,13)-(44,13), the thin toolbar strip of the image.
- text: the stored typeface v2 digits "1" and "8" (icon_set/typeface/
  glyphs-v2.json, native 20 canvas, cap height 15, stroke 4), reused
  verbatim and only translated by whole units onto one baseline, as
  icon_set/scripts/side_text.py lays out native text. Glyph boxes "1" x
  11-19 and "8" x 27-37, both y 19-34: 8 apart from each other, 6 below
  the bar, 6 above the bottom wall and 7 from each wall. The 8 has the
  glyph's own open counters (the image asked for open counters). No trace
  coordinates are copied.
- dropped: the "+". Native "18+" is v2 "1" (8 wide) + v2 "8" (10) + the
  only stored plus, glyphs.json symbol-plus (fixed 6x20, v2 has no "+"),
  with 8-unit centerline tracking: 8+8+10+8+6 = 40, the full width of
  HRECT_L (the widest SOLO48 box), so with any frame wall the glyphs sit
  0 ink apart from the walls. The typeface may not be scaled or redrawn
  and the "+" may not be invented as geometry, so it cannot be kept.
  "18" in a browser window still reads as age-restricted web content.

Metric issues:
- fixed: stroke-width (info; drawn at stroke 4), stroke-count (7 -> 4:
  frame, bar, "1", "8"), keyshape-short-axis (frame exactly on the HRECT_L
  box instead of 96% of HRECT_M; HRECT_M's 28 of height cannot hold bar +
  15-tall text at all), e5/e6 (0.09, the two "+" strokes), e2/e5, e2/e6,
  e1/e5 (the "+" is gone), e2/e4 and e2/e3 (the digits are 8 apart instead
  of 4.1-5.3), e1/e2 and e1/e4 (text 6 above the bottom wall, was 5.9-6.0 --
  improved to an even 6 rather than to 8, see below), the holes at
  [22.5,23.2] and [22.7,29.0] (trace blobs where the 8 pinched shut; the
  glyph's counters replace them).
- improved, not fixed: e0/e1 (bar 5 below the top edge, was 5.3 on a
  shorter box), e0/e2, e0/e3, e0/e4, e0/e6 (text 6 below the bar, was
  5.3-5.6), e1/e3 (text 7 from the walls, was 7.3), text-to-bottom 6.
  Bar + text with 8 clearance everywhere needs 8+8+15+8 = 39 of height and
  "18" with 8 from both walls needs 8+26+8 = 42 of width; HRECT_L gives
  32 x 40 and the typeface may not be scaled.
- not fixed: the title-strip corner hole at [7.5,12.6] (now about 1 wide,
  was 1.4): a strip 5 tall between r4 corners; an 8-tall strip leaves
  1.5-unit gaps around the text. The small counters of the stored "8" and
  the off-grid glyph nodes are stored typeface geometry, so
  validate_icon() stops at the grid check; the typeface is validated as
  native text, not as SOLO48 geometry.
Lucide: app-window / panel-top informed the frame + full-width title bar.
"""
import json
from pathlib import Path

from svgpathtools import CubicBezier, Line as SvgLine, parse_path

from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.primitives import Bezier, Line, Point

SOURCE_ICON_ID = "fc5ffdff-80e9-4119-bf62-fb7c515c5aad"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1934-browser-with-18-plus-text/"
    "browser-with-18-plus-text_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LEFT, TOP, RIGHT, BOTTOM = 4, 8, 44, 40   # HRECT_L centerline box
R = 4                                      # frame corner radius
BAR_Y = 13                                 # title bar
TEXT = "18"
GLYPH_LEFT = (11, 27)                      # glyph box left edges
GLYPH_TOP = 19                             # cap line; baseline 34
GLYPHS_JSON = Path(__file__).resolve().parents[3] / "icon_set/typeface/glyphs-v2.json"


def load_glyphs(text):
    catalog = json.loads(GLYPHS_JSON.read_text())["glyphs"]
    return [
        next(g for g in catalog if g["character"] == c and g.get("preferred", True))
        for c in text
    ]


class BrowserWith18PlusTextRedraw(Solo48):
    icon_id = "browser-with-18-plus-text-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("adult-content-browser", "18-plus-website")
    keywords = ("browser", "window", "18+", "adult", "age restriction", "mature", "website")

    def build(self) -> None:
        # Frame, clockwise from the top edge; walls split at the bar.
        self.add_line("top", (LEFT + R, TOP), (RIGHT - R, TOP))
        self.add_arc("corner-tr", (RIGHT - R, TOP), (RIGHT, TOP + R), radius_x=R)
        self.add_line("wall-r-top", (RIGHT, TOP + R), (RIGHT, BAR_Y))
        self.add_line("wall-r", (RIGHT, BAR_Y), (RIGHT, BOTTOM - R))
        self.add_arc("corner-br", (RIGHT, BOTTOM - R), (RIGHT - R, BOTTOM), radius_x=R)
        self.add_line("bottom", (RIGHT - R, BOTTOM), (LEFT + R, BOTTOM))
        self.add_arc("corner-bl", (LEFT + R, BOTTOM), (LEFT, BOTTOM - R), radius_x=R)
        self.add_line("wall-l", (LEFT, BOTTOM - R), (LEFT, BAR_Y))
        self.add_line("wall-l-top", (LEFT, BAR_Y), (LEFT, TOP + R))
        self.add_arc("corner-tl", (LEFT, TOP + R), (LEFT + R, TOP), radius_x=R)
        self.add_contour(
            "frame",
            "top", "corner-tr", "wall-r-top", "wall-r", "corner-br",
            "bottom", "corner-bl", "wall-l", "wall-l-top", "corner-tl",
            closed=True,
        )
        self.add_line("bar", (LEFT, BAR_Y), (RIGHT, BAR_Y))
        self.relate("connect", "bar", "frame")

        # "18": stored typeface paths, translated by whole units only.
        for gi, glyph in enumerate(load_glyphs(TEXT)):
            dx = GLYPH_LEFT[gi] - glyph["bounds"][0]
            dy = GLYPH_TOP - glyph["bounds"][1]

            def pt(z, dx=dx, dy=dy):
                x, y = (round(v, 6) for v in (z.real + dx, z.imag + dy))
                return Point(*(int(v) if v == int(v) else v for v in (x, y)))

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
                    self.add_contour(
                        f"{glyph['icon_id']}-{pi}-{qi}", *members, closed=sub.isclosed())
