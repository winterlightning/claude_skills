"""images (redraw of the new-pipeline traced SVG).

Plan: a photo stack. A rounded front photograph with a two-peak mountain
inside, and a second photograph behind it shown only by its top edge,
top-left corner and left edge, offset 8 up and 8 left. On HRECT_L
(centerline box (4,8)-(44,40)) instead of the suggested SQUARE: the trace
is 1.36 wide per unit high, SQUARE fills only 73% of its y axis and would
need a 1.36 vertical stretch that turns both photographs square; HRECT_L
(40x32) keeps the landscape proportion and gives the front frame the
widest interior.
- front: closed rect (13,17)-(44,40), r4 corners.
- back: one open stroke, (35,8) -> top-left r4 corner at (4,8) ->
  (4,31). Offset 9, not 8: an exact 8 between the two arc-bearing
  contours comes back `review`, so both ends stop 9 short of the front
  frame's extension (top edge y=17, left edge x=13).
- mountain: Lucide-image style, one polyline from the bottom-left corner
  node (17,40) up to a tall peak (27,26), a valley (32,31), a lower peak
  (35,28) and down into the right wall/corner node (44,36); both ends
  share the frame's nodes (`connect`). Peak and valley keep 9 from the top
  and bottom walls.

Metric issues fixed:
- clearance e0/e1 (2.84): the back photo's top-right hook that curled down
  onto the front frame is dropped; the top edge ends in a plain cap 9 above
  the front's top edge.
- clearance e0/e2 (6.05) and e1/e2 (2.96): the back photo's lower hook is
  dropped (its left edge ends 9 above the front's bottom), and the
  mountain no longer floats a few units off the frame: it is joined to the
  frame at shared corner nodes, as in Lucide `image`, which also gives it
  the room a free-floating mountain (8-9 in from every wall) did not have.
- hole (2.4 at (9.1,13.9)): the back corner is a clean r4 arc 9 clear of
  the front frame, so no pinched enclosure remains; the regions the
  mountain closes against the frame pass the 6-inscribed hole rule.
- keyshape-short-axis (warn): resolved by choosing HRECT_L, whose four
  extremes are hit exactly (x 4 / 44, y 8 / 40).
- stroke-width (info): redrawn at stroke 4 with every gap sized for it.

Dropped: a free-floating mountain. Tried first (band x 22..35, y 26..31);
it validated but the second peak blurred into a blob at 48 px.

Lucide: images (a front image rect with a second sheet shown by an offset
L-shaped corner) and image (mountain line inside a rounded frame) informed
the construction; the offset is top-left here, as in the generated image.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "94993cb5-32ce-48f8-ba6f-9fe516a4704d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1542-images/images_raw.svg"
AUTHOR = "claude-opus-5-5"

L, T, R, B = 13, 17, 44, 40   # front photo walls
CR = 4                        # corner radius, both photos
OFF = 9                       # back photo offset (up and left)
BL, BT = L - OFF, T - OFF     # back photo left wall / top edge
GAP = 9                       # peak/valley clearance from the front walls


class ImagesRedraw(Solo48):
    icon_id = "images-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "media"
    aliases = ("photos", "gallery", "pictures")
    keywords = ("images", "photos", "gallery", "pictures", "album",
                "media", "stack", "landscape")

    def build(self) -> None:
        # Front photograph, clockwise from the top-left corner.
        self.add_line("top", (L + CR, T), (R - CR, T))
        self.add_arc("tr", (R - CR, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("right", (R, T + CR), (R, B - CR))
        self.add_arc("br", (R, B - CR), (R - CR, B), radius_x=CR, sweep=True)
        self.add_line("bottom", (R - CR, B), (L + CR, B))
        self.add_arc("bl", (L + CR, B), (L, B - CR), radius_x=CR, sweep=True)
        self.add_line("left", (L, B - CR), (L, T + CR))
        self.add_arc("tl", (L, T + CR), (L + CR, T), radius_x=CR, sweep=True)
        self.add_contour("front", "top", "tr", "right", "br", "bottom",
                         "bl", "left", "tl", closed=True)

        # Back photograph: top edge, corner, left edge; both ends stop 9
        # short of the front frame.
        self.add_line("back-top", (R - OFF, BT), (BL + CR, BT))
        self.add_arc("back-corner", (BL + CR, BT), (BL, BT + CR),
                     radius_x=CR, sweep=False)
        self.add_line("back-left", (BL, BT + CR), (BL, B - OFF))
        self.add_contour("back", "back-top", "back-corner", "back-left")

        # Mountain, joined to the frame at the bottom-left and right corner nodes.
        self.add_polyline("mountain", (L + CR, B), (27, T + GAP),
                          (32, B - GAP), (35, 28), (R, B - CR))
        self.relate("connect", "mountain", "front")
