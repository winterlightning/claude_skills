"""hand-holding-megaphone (redraw of the new-pipeline traced SVG).

Plan (SQUARE, centerline box (6,6)-(42,42)):
- Megaphone mirrored about y = AXIS_Y: a rounded mouthpiece box on the left,
  a straight-sided cone flaring right to a flat rim on x = 42 (after Lucide
  `megaphone`: box + flared body closed by a straight end), one outline contour
  plus the box/cone divider.
- Handle hangs straight down from the box/cone bottom joint; a bent stick arm
  runs from the handle's foot down-left to the canvas corner (6,42).

Metric issues:
- stroke-width (info): rebuilt at stroke 4, every gap sized for it.
- clearance e2/e4 4.86 (error): fixed -- the traced elliptical bell rim is
  replaced by one flat rim line that is part of the cone outline.
- hole at [39.5,13.2] 1.0 wide (error): fixed -- that sliver was inside the
  ellipse rim, which is gone.
- hole at [18.8,15.8] 2.2 wide (error): fixed -- the mouthpiece box is 10x12
  on centerlines, a 6x8 ink opening.
- loose-join e0/e1, e0/e2, e0/e3 (info): fixed -- handle, box, cone and
  divider share the exact endpoint (HANDLE_X, BOX_B) and are related.
- no-head (warn): not applicable -- the subject is an arm holding the
  megaphone, not a stick figure, so no head is drawn.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5587cff6-d8d9-4045-b4e0-05bcb4c1a7bc"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1324-hand-holding-megaphone/hand-holding-megaphone_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS_Y = 17                        # megaphone mirror axis
BOX_L, HANDLE_X = 10, 20           # mouthpiece box; its right wall is the divider
BOX_T, BOX_B = AXIS_Y - 6, AXIS_Y + 6
BOX_RAD = 2
RIM_X, RIM_T, RIM_B = 42, AXIS_Y - 11, AXIS_Y + 11
FOOT = (HANDLE_X, 31)              # handle foot, where the hand grips
ELBOW, SHOULDER = (14, 38), (6, 42)


class HandHoldingMegaphoneRedraw(Solo48):
    icon_id = "hand-holding-megaphone-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication"
    aliases = ("megaphone-in-hand", "bullhorn-in-hand", "announcement")
    keywords = ("hand", "arm", "holding", "megaphone", "bullhorn", "loudspeaker", "announce", "marketing", "promotion")

    def build(self) -> None:
        r = BOX_RAD
        # Outline: box top -> rounded left side -> box bottom -> cone -> rim -> back.
        self.add_line("box-top", (HANDLE_X, BOX_T), (BOX_L + r, BOX_T))
        self.add_arc("box-tl", (BOX_L + r, BOX_T), (BOX_L, BOX_T + r), radius_x=r, sweep=False)
        self.add_line("box-left", (BOX_L, BOX_T + r), (BOX_L, BOX_B - r))
        self.add_arc("box-bl", (BOX_L, BOX_B - r), (BOX_L + r, BOX_B), radius_x=r, sweep=False)
        self.add_line("box-bottom", (BOX_L + r, BOX_B), (HANDLE_X, BOX_B))
        self.add_line("cone-bottom", (HANDLE_X, BOX_B), (RIM_X, RIM_B))
        self.add_line("rim", (RIM_X, RIM_B), (RIM_X, RIM_T))
        self.add_line("cone-top", (RIM_X, RIM_T), (HANDLE_X, BOX_T))
        self.add_contour(
            "megaphone", "box-top", "box-tl", "box-left", "box-bl", "box-bottom",
            "cone-bottom", "rim", "cone-top", closed=True,
        )
        self.add_line("divider", (HANDLE_X, BOX_T), (HANDLE_X, BOX_B))

        # Handle and the bent arm gripping its foot.
        self.add_line("handle", (HANDLE_X, BOX_B), FOOT)
        self.add_polyline("arm", FOOT, ELBOW, SHOULDER)

        self.relate("connect", "divider", "megaphone")
        self.relate("connect", "handle", "megaphone")
        self.relate("connect", "handle", "divider")
        self.relate("connect", "arm", "handle")
