"""camera image file: a document page with a clipped top-right corner and a
camera on it (redraw of the new-pipeline traced SVG).

Plan: VRECT_L (centerline box (8,4)-(40,44)), camera mirrored about x=24.
- page: one closed polyline on the four box extremes, top-right corner
  clipped by a 45-degree cut (32,4)-(40,12).
- camera: Lucide `camera` construction: body 16x16 (x 16..32, y 20..36)
  with a 1:2-sloped prism bump (20,20)-(22,16)-(26,16)-(28,20)
  in the same contour; exactly 8 from the page's left/right/bottom walls,
  12 from the top and >= 11 from the corner cut.
- lens: one dot at the body centre (24,28), 8 from every body wall.

Keyshape: VRECT_L instead of the suggested VRECT_M. VRECT_M's 28-wide box
leaves only 12 for the camera between the page walls (8 each side), too
narrow for any lens (a dot needs a 16-wide body); VRECT_L gives 16.

Metric issues fixed by the rebuild:
- clearance e0/e2 (page vs camera, 3.97) and e1/e2 (fold vs camera, 6.82):
  the camera sits exactly 8 from each page wall, 12 from the top, 11.3 from
  the corner cut.
- clearance e2/e3 (camera vs lens, 2.41): the lens is a dot 8 from every
  camera wall.
- holes at (30.7,24.9), (23.9,28.3), (14.1,39.0) (2.6 / 4.56 / 4.4): the
  page-camera band is 8 on centerlines everywhere and 12 above the camera,
  and the camera interior is 16 square around a single dot.
- hole at (32.5,10.6) (1.0, the fold-flap triangle): the flap lines are gone;
  the corner is a plain clipped cut.
- keyshape-short-axis (y 96%): page edges sit on x 8/40 and y 4/44, exact.
- stroke-width (2.55): drawn at the profile stroke 4, gaps budgeted for it.
Not kept, with reason:
- the folded flap (inner L under the cut): a right-triangle flap needs legs
  >= 17 to hold a 6-unit hole at stroke 4, which would eat the page top.
- the lens ring: a ring with a 6-unit hole needs r >= 5, and 8 clear to the
  body walls makes the body 26 wide, plus 16 for the page walls = 42 > 32.
Corners are square vertices softened by the round joins: with r=4 page / r=2
camera arcs every exact-8 gap (page-camera, camera-lens) came back `review`
(arc contours are not certified on the minimum), and there is no width to
give 9 (8+16+8 fills the 32-wide box exactly).
Lucide: `file` (page + corner) and `camera` (body + prism bump) informed the
construction; the flap and lens ring were reduced as above.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ed808041-ff02-4ca5-8f86-337d16e29436"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1717-camera-image-file/camera-image-file_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
PAGE = (8, 4, 40, 44)      # centerline box, VRECT_L
CUT = 8                    # clipped corner leg
BODY = (16, 20, 32, 36)    # camera body, 8 in from the page walls
BUMP_TOP = 16
BUMP_HALF = (4, 2)         # half width at the body, half width at the top


class CameraImageFileRedraw(Solo48):
    icon_id = "camera-image-file-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/file"
    aliases = ("camera file", "photo file", "image file")
    keywords = ("camera", "photo", "image", "file", "document", "picture")

    def build(self) -> None:
        x0, y0, x1, y1 = PAGE
        self.add_polyline(
            "page", (x0, y0), (x1 - CUT, y0), (x1, y0 + CUT), (x1, y1), (x0, y1),
            closed=True,
        )

        bx0, by0, bx1, by1 = BODY
        wide, narrow = BUMP_HALF
        self.add_polyline(
            "camera", (bx0, by0), (AXIS - wide, by0), (AXIS - narrow, BUMP_TOP),
            (AXIS + narrow, BUMP_TOP), (AXIS + wide, by0), (bx1, by0), (bx1, by1),
            (bx0, by1),
            closed=True,
        )

        self.add_dot("lens", (AXIS, (by0 + by1) // 2))
