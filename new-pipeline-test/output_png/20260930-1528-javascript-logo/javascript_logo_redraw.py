"""javascript-logo (redraw of the new-pipeline traced SVG).

Plan: the JavaScript "JS" monogram as two separate monoline letters on
HRECT_M (centerline box (4,10)-(44,38), ink (2,8)-(46,40)).
- Text rule: the letters are not traced. Both reuse the existing typeface v2
  grid-hinted size-32 glyphs (icon_set/typeface/glyphs-v2-sizes.json,
  letter-j-uppercase and letter-s-uppercase: 14 x 28 centerlines, stroke 4),
  translated only: J by (-5,+8) to x 4..18, S by (+21,+8) to x 30..44.
- Each letter is one smooth bezier run (straight glyph runs are written as
  collinear cubics) so every free end is an integer point: J from its stem
  top (18,10) down and round to its hook tip (4,29); S from its top bar
  end (44,10) to its bottom bar end (30,38).
- Layout: J left and S right share the 10..38 body band, so both letters
  touch the top and bottom of the box; J's hook and S's bottom bar reach
  x=4 and x=30, J stem and S spine reach x=18 and x=44.

Metric issues:
- clearance (error, e0/e1 7.27 apart): fixed. The closest pair is the J
  stem (x=18) to the S upper bowl (x=31) at y=16: 13 on centerlines.
- keyshape-short-axis (warn, HRECT_L x fill 92%): fixed by moving to
  HRECT_M. The 32-tall glyph pair cannot fill HRECT_L's 40-wide box with an
  8-unit gap (J stem to S bowl needs S at J+7, so 18+7+18 = 43 > 40); the
  size-32 pair fills HRECT_M exactly on both axes.
- stroke-width (info, trace 2.46): redrawn at stroke 4.
No useful Lucide match: Lucide has no JS monogram; the construction comes
from the project's own typeface.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c7e5eabf-e0c2-47d6-9a2b-23487329395b"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1528-javascript-logo/javascript-logo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# Typeface v2 size-32 centerlines (glyph coordinates, body band y 2..30).
J_SEGMENTS = (  # reversed from the glyph: stem top -> hook tip
    ((23, 9), (23, 16), (23, 22.73)),
    ((23, 27.3), (19.866, 30), (16, 30)),
    ((12.134, 30), (9, 27.3), (9, 21)),
)
J_START = (23, 2)
S_SEGMENTS = (
    ((20.707, 2), (18.414, 2), (16.121, 2)),
    ((12.288, 2), (10, 4.953), (10, 8.074)),
    ((10, 9.915), (10.796, 11.815), (12.542, 13.2)),
    ((14.928, 15.067), (17.314, 16.933), (19.7, 18.8)),
    ((21.941, 20.283), (23, 22.355), (23, 24.314)),
    ((23, 27.287), (20.562, 30), (16.121, 30)),
    ((13.747, 30), (11.374, 30), (9, 30)),
)
S_START = (23, 2)
J_OFFSET = (-5, 8)
S_OFFSET = (21, 8)


def shift(p, off):
    return (p[0] + off[0], p[1] + off[1])


def placed(segments, off):
    return tuple(tuple(shift(p, off) for p in seg) for seg in segments)


class JavascriptLogoRedraw(Solo48):
    icon_id = "javascript-logo-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("js-logo", "js")
    keywords = ("javascript", "js", "logo", "brand", "programming", "code",
                "language", "web", "developer")

    def build(self) -> None:
        self.add_bezier("letter-j", shift(J_START, J_OFFSET),
                        *placed(J_SEGMENTS, J_OFFSET))
        self.add_bezier("letter-s", shift(S_START, S_OFFSET),
                        *placed(S_SEGMENTS, S_OFFSET))
