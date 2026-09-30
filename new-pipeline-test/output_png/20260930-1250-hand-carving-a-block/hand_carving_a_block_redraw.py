"""hand-carving-a-block (redraw of the new-pipeline traced SVG).

Plan: three parts on SQUARE, centerline box (6,6)-(42,42).
- arm: one bent stroke, upper arm down the left edge x=6 from the shoulder
  (6,6), a radius-4 elbow, and a level forearm at y=18 that ends on the chisel
  handle (the hand grips the chisel). (6,6) is the x=6 and y=6 extreme.
- chisel on the 45 degree axis x - y = 9, pointing down-right at the notch:
  a hollow handle (half width (4,-4), 11.3 x 11.3 on centerlines, so its
  interior is a 7.2-wide ink hole) with its top corner (23,6) on the y=6 edge,
  and a single-stroke blade from the middle of the handle's lower end
  F=(27,18) to the tip (32,23). The forearm meets the handle's lower-left side
  at its midpoint (19,18), 45 degrees off the side, 8 from the blade root.
  The handle cannot be longer: its low corner (23,22) is exactly 8 above the
  block top and its top corner is on the y=6 edge, so a square handle is the
  longest one with a valid hole on SQUARE.
- block: one closed contour (10,30)-(42,42) with a V notch (27,30)-(32,35)-
  (37,30) under the chisel tip; (42,42) is the x=42 and y=42 extreme. The
  apex sits 7 above the bottom wall, so the block interior stays an open hole.
- tip clearance: the tip is 12 above the apex, so it is 8.49 from both notch
  walls (the blade runs parallel to the left wall at 8.49) and 8.6 from the
  notch rims.

Metric issues (hand-carving-a-block_metrics.json):
- stroke-width (trace 2.77 after fit): fixed, stroke 4 throughout, every gap
  between separate parts budgeted at >= 8 on centerlines.
- clearance e0/e1 (arm end 2.69 from the chisel): fixed by making the contact
  real: the forearm ends on the handle side and is declared `connect`, so the
  hand now holds the chisel instead of nearly touching it.
- clearance e1/e3 (chisel tip 3.13 from the block): fixed, tip 8.49 from the
  notch walls.
- hole at (19.9,18.2) (0.28 wide sliver between the handle and the ferrule
  arc): fixed, the traced ferrule arc and the narrow hollow blade became one
  single-stroke blade, so the only chisel hole is the handle interior (7.2).
- hole at (35.1,37.2) (block interior 5.6 wide under the notch): fixed, the
  notch apex is 7 above the bottom wall; the block hole is 8.0.
- no-head (human subject without a head): not applicable, not fixed. The
  subject is a hand/arm only, as the brief asked (one bent arm stroke); there
  is no full figure, so no head is drawn and no human-figure mark is made.
No useful Lucide match (Lucide has no chisel or carving icon); construction
follows Lucide's hollow-handle tools (e.g. `hammer`) with a single-line blade.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "11e91124-506f-4bc4-9aa0-511ff30e500c"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1250-hand-carving-a-block/hand-carving-a-block_raw.svg"
AUTHOR = "claude-opus-5-5"

# chisel on the axis x - y = 9
TIP = (32, 23)
FERRULE = (27, 18)            # middle of the handle's lower end
HALF_W = (4, -4)              # handle half width, perpendicular to the axis
HANDLE_LEN = 8                # along the axis, in (-1, -1) steps
GRIP = (19, 18)               # middle of the handle's lower-left side
# arm
SHOULDER = (6, 6)
ELBOW_R = 4
# block with the notch under the tip
BLOCK_X0, BLOCK_X1, BLOCK_TOP, BLOCK_BOTTOM = 10, 42, 30, 42
NOTCH_HALF, NOTCH_DEPTH = 5, 5


class HandCarvingABlockRedraw(Solo48):
    icon_id = "hand-carving-a-block-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("wood carving", "chiseling", "sculpting")
    keywords = ("hand", "chisel", "carve", "carving", "block", "wood", "sculpt", "craft")

    def build(self) -> None:
        fx, fy = FERRULE
        hx, hy = HALF_W
        low_r = (fx + hx, fy + hy)                      # (31, 14)
        low_l = (fx - hx, fy - hy)                      # (23, 22)
        top_r = (low_r[0] - HANDLE_LEN, low_r[1] - HANDLE_LEN)   # (23, 6)
        top_l = (low_l[0] - HANDLE_LEN, low_l[1] - HANDLE_LEN)   # (15, 14)
        # handle: vertices at the grip and the ferrule so both joins share endpoints
        self.add_polyline(
            "handle", top_l, top_r, low_r, FERRULE, low_l, GRIP, closed=True,
        )
        self.add_line("blade", FERRULE, TIP)
        self.relate("connect", "blade", "handle")

        sx, sy = SHOULDER
        gy = GRIP[1]
        self.add_line("upper-arm", SHOULDER, (sx, gy - ELBOW_R))
        self.add_arc("elbow", (sx, gy - ELBOW_R), (sx + ELBOW_R, gy),
                     radius_x=ELBOW_R, sweep=False)
        self.add_line("forearm", (sx + ELBOW_R, gy), GRIP)
        self.add_contour("arm", "upper-arm", "elbow", "forearm")
        self.relate("connect", "arm", "handle")

        ax, ay = TIP[0], BLOCK_TOP + NOTCH_DEPTH
        self.add_polyline(
            "block",
            (BLOCK_X0, BLOCK_TOP), (ax - NOTCH_HALF, BLOCK_TOP), (ax, ay),
            (ax + NOTCH_HALF, BLOCK_TOP), (BLOCK_X1, BLOCK_TOP),
            (BLOCK_X1, BLOCK_BOTTOM), (BLOCK_X0, BLOCK_BOTTOM),
            closed=True,
        )
