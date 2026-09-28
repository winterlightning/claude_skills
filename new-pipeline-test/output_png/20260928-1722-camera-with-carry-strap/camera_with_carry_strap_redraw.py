"""camera with carry strap: a wide compact-camera body with a round lens and a
flash dot, and one arched carry strap standing on the body's top wall
(redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)); body and strap mirrored about
x=24, the lens set right of the axis like a compact camera.
- body: one closed polyline on the box sides and bottom, x 6..42, y 16..42,
  corners cut by 2 so the round joins read as soft corners.
- strap: one half-ellipse arc (rx 16, ry 10) from the body's top corners
  (8,16)-(40,16), apex on the box top y=6; it leaves the wall vertically and
  shares both endpoints with the body (connect declared).
- lens: circle r=5 at (27,29), exactly 8 from the body top and bottom walls.
- flash: one dot at (14,24), 8 from the top and left walls, 8.9 from the lens.

Keyshape: SQUARE instead of the suggested HRECT_L. Vertical budget: the strap
hole needs 10 on centerlines (6 hole + stroke 4) and a body that holds a
ring lens needs 26 (8 + 10 + 8), so 36 in total. HRECT_L is 32 tall; there
the strap hole collapses to 2 or the lens has to shrink to a dot.

Metric issues fixed by the rebuild:
- clearance e0/e4 (2.21) and e1/e4 (1.87), body walls vs lens: the lens sits
  8 from the top and bottom walls and 10 from the right wall.
- keyshape-short-axis (HRECT_L x 93%): on SQUARE the body touches x 6/42 and
  y 42 and the strap apex touches y 6, exact.
- loose-join e0/e3 (0.96 gap): the strap ends on the body's corner vertices
  and shares them exactly, with relate("connect").
- narrow-join e3/e1 (33.7 deg wedge): the strap leaves the wall at 90 degrees
  instead of sliding into an eyelet.
- stroke-width (2.46): drawn at the profile stroke 4, gaps budgeted for it.
Removed rather than repaired:
- clearance e1/e2, e2/e3, e2/e4 (shutter button vs body, eyelet, lens): the
  shutter button is dropped. On the top wall it would sit inside the strap's
  10-tall hole (needs 8 clear of the strap on both sides) or outside the
  strap feet, which already sit on the corners.
- the two eyelet rings: a ring needs r >= 5 for a 6 hole, bigger than the
  whole strap foot; the strap attaches straight to the body corners.
Added: the flash dot, because body + strap + centred ring read as a padlock
at 48 px; the off-axis lens and flash dot give the compact-camera face.
Corners are 2-unit chamfers, not arcs: with r=4 arc corners the exact-8
lens gap came back `review`.
Lucide: `camera` (rounded body with a circle lens) informed the body and lens;
its prism bump is replaced by the strap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "08e27f33-65ac-57d2-8a06-756b3779a004"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1722-camera-with-carry-strap/camera-with-carry-strap_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
BODY = (6, 16, 42, 42)     # centerline box of the body: SQUARE sides + bottom
CHAMFER = 2                # body corner cut; the strap stands on its top ends
STRAP_TOP = 6              # strap apex on the SQUARE top edge
LENS = (27, 29, 5)         # centre x, centre y, radius: 8 from top and bottom
FLASH = (14, 24)           # 8 from the top and left walls


class CameraWithCarryStrapRedraw(Solo48):
    icon_id = "camera-with-carry-strap-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ("camera strap", "strapped camera", "compact camera")
    keywords = ("camera", "strap", "photo", "photography", "lens", "travel", "tourist")

    def build(self) -> None:
        x0, y0, x1, y1 = BODY
        c = CHAMFER
        self.add_polyline(
            "body", (x0 + c, y0), (x1 - c, y0), (x1, y0 + c), (x1, y1 - c),
            (x1 - c, y1), (x0 + c, y1), (x0, y1 - c), (x0, y0 + c), closed=True,
        )

        self.add_arc(
            "strap", (x0 + c, y0), (x1 - c, y0),
            radius_x=AXIS - (x0 + c), radius_y=y0 - STRAP_TOP,
        )
        self.relate("connect", "strap", "body")

        cx, cy, r = LENS
        self.add_arc("lens-upper", (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc("lens-lower", (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour("lens", "lens-upper", "lens-lower", closed=True)

        self.add_dot("flash", FLASH)
