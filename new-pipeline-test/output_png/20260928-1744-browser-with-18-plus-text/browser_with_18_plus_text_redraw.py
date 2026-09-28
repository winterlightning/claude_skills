"""browser-with-18-plus-text (redraw of the new-pipeline traced SVG).

Plan: a wide browser window on HRECT_L (centerline box (4,8)-(44,40)) with
one title bar, and the age mark "18" centred in the page area.
- frame: one closed rounded rectangle, r4 corners, mirrored about x=24.
  Both walls are split at y=13 so the title bar shares their endpoints and
  the contact is declared (the trace's bar already met the walls).
- title bar: one line (4,13)-(44,13), a thin strip as in the reference.
- text: the stored typeface digits "1" and "8" from
  icon_set/typeface/glyphs-v2.json (Letters/new, native 20 canvas, cap
  height 15, stroke 4), reused verbatim and only translated by whole units,
  on one shared baseline, the same way icon_set/scripts/side_text.py lays
  out native text. Glyph boxes: "1" x 11-19, "8" x 27-37, both y 19-34, so
  the text sits 6 below the bar and 6 above the bottom wall, 7 from each
  wall and 8 apart. The trace's own digit shapes are not copied.
- dropped: the "+". The only stored plus (glyphs.json symbol-plus) is a
  fixed 6x20 glyph; "18+" at the typeface's 4-unit tracking is 40 wide,
  the whole window interior, and a tight "18+" merged at 48 px (the plus
  read as a bar against the wall). "18" inside a browser still reads as
  age-restricted content; the "+" is not invented as a non-typeface mark.

Metric issues:
- fixed: stroke-count (7 -> 4: frame, bar, "1", "8"), stroke-width (stroke
  4), keyshape-short-axis (frame exactly on the HRECT_L box instead of 85%
  of HRECT_M), e5/e6 at 0.0 and e2/e6, e3/e6, e2/e5, e3/e5,
  e0/e5, e1/e5 (the traced "+" strokes are gone), e2/e4, e3/e4 (the
  digits are 8 apart instead of 3.6-4.1), e0/e4, e0/e2 (text now 6 from the
  bottom wall instead of 4.6-4.8).
- improved, not fixed: e0/e1 (bar 5 below the top edge, was 4.3; 8 would
  leave 3-unit gaps around the text), e1/e3, e1/e4 (text 6 below the bar,
  was 4.4-4.6) and text-to-bottom-wall 6 (need 8). The fixed digits are 15
  tall; bar + text with 8 clearance everywhere needs 8+8+15+8 = 39 of the
  32 available on HRECT_L, the tallest wide SOLO48 box, and the typeface
  may not be scaled.
- not fixed: the title-strip corner slivers (about 1 wide, was 0.4) -- a
  strip 5 tall between r4 corners; opening them to 6 means the bar at 16 and
  a 3-unit gap to the text, which merges at 48 px. The small counters inside
  the "8" (stored glyph geometry) and
  the off-grid glyph nodes (stored paths), so validate_icon() stops at the
  grid check; the typeface is validated as native text, not SOLO48 geometry.
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
    "new-pipeline-test/output_png/20260928-1744-browser-with-18-plus-text/"
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
