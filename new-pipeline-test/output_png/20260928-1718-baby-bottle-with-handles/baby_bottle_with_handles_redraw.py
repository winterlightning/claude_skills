"""baby-bottle-with-handles (redraw of the new-pipeline traced SVG).

Plan: a trainer baby bottle, with a domed nipple on a straight body. A ring
line across the body marks the collar band, and an open curved handle
springs from each end of that ring. VRECT_L, centerline box (8,4)-(40,44):
nipple apex on y=4, handle drops on x=8 / x=40, body bottom on y=44. The
whole icon is mirrored about x=24.
- nipple: an arch 10 wide, a radius-5 dome about (24,9) on two short
  vertical sides standing on the body top at y=16 (opening 10x12).
- body: one closed contour, walls x=16 / x=32 from y=16 down to radius-5
  bottom corners on y=44. The top edge is split where the nipple lands, and
  the walls are split at the ring.
- collar: the ring line y=26 across the body closes a 16x10 collar band
  above a 16x18 bottle chamber.
- handles: one definition mirrored. A radius-8 quarter arc about (16,34)
  leaves the ring/wall junction horizontally and turns down to x=8, then a
  straight drop to an open end at y=38. The drop runs parallel to the wall
  exactly 8 away, and the open end stays 8 clear of the body.

Metric issues (baby-bottle-with-handles_metrics.json):
- clearance e1/e2, e1/e3 (handles 1.77 from the body): fixed. Each handle
  now starts on the body (shared endpoint, relate connect), and its open
  drop is 8 from the wall.
- clearance e1/e4, e1/e5, e2/e4, e2/e5, e3/e4, e3/e5 (nipple, collar,
  handles and body about 4 apart): fixed. They are one connected drawing,
  with every parallel run inside it at least 10 apart.
- loose-join e1/e2, e1/e3 (body 0.36 short of the handles): fixed, with
  exact shared endpoints and relate("connect").
- holes at (23.9,9.7), (14.8,20.4), (33.1,20.4), 1.2 wide: fixed. The
  slivers inside the nipple base and beside the shoulders are gone. Every
  enclosed opening is at least 10 on centerlines, 6 of ink at stroke 4.
- stroke-width (info): redrawn at stroke 4, with every gap budgeted for it.
- keyshape-short-axis (VRECT_M fills 84% of x): switched to VRECT_L. At
  stroke 4 the body (16) plus an 8 gap to each handle needs 32 units of
  width, which VRECT_M's 28 cannot hold. VRECT_L's box is filled exactly
  on all four sides.
Not kept:
- The inward curl of the traced C handles. A curled end would come back
  within 8 of the body wall. Closing it onto the wall instead would leave a
  handle opening only 8 wide (4 of ink) beside a 16-wide body, and making
  the handle openings 10 wide shrinks the body to 12. That was rendered and
  read as a padlock.
- A separate collar pill: the ring band takes its place.
- The nipple's pinched neck: a narrower tip would close its opening.
- A SQUARE fit with closed D handles was also rendered and rejected. It was
  squat and read as a bag.
No useful Lucide match: Lucide `milk` only informs the straight bottle body
with rounded bottom corners.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "46fff59c-84bf-4526-bd9b-33201133c81c"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1718-baby-bottle-with-handles/"
    "baby-bottle-with-handles_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP = 4                  # nipple apex
NIPPLE_R = 5             # nipple dome radius (half width)
SHOULDER = 16            # body top: the collar's top edge
RING = 26                # collar ring line across the body
BODY_HALF = 8            # body walls x 16..32
BOTTOM = 44
BODY_R = 5               # bottom corner radius
HANDLE_OUT = 8           # handle drop x
HANDLE_R = 8             # handle arc radius (wall to drop)
HANDLE_END = 38          # handle open end y


def mx(x):
    return 2 * AXIS - x


class BabyBottleWithHandlesRedraw(Solo48):
    icon_id = "baby-bottle-with-handles-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/baby"
    aliases = ("baby bottle", "sippy bottle", "trainer bottle", "feeding bottle")
    keywords = ("baby", "bottle", "milk", "feeding", "infant", "nipple", "handles", "formula")

    def handle(self, side: str, sign: int) -> None:
        """One open handle; sign=-1 left, +1 right (x mirrored about AXIS)."""
        def x(v):
            return v if sign < 0 else mx(v)
        sweep = sign > 0
        wall = AXIS - BODY_HALF
        self.add_arc(f"{side}-handle-bar", (x(wall), RING), (x(HANDLE_OUT), RING + HANDLE_R),
                     radius_x=HANDLE_R, sweep=sweep)
        self.add_line(f"{side}-handle-drop", (x(HANDLE_OUT), RING + HANDLE_R), (x(HANDLE_OUT), HANDLE_END))
        self.add_contour(f"{side}-handle", f"{side}-handle-bar", f"{side}-handle-drop")

    def build(self) -> None:
        nl, nr = AXIS - NIPPLE_R, AXIS + NIPPLE_R
        dome_y = TOP + NIPPLE_R
        bl, br = AXIS - BODY_HALF, AXIS + BODY_HALF
        foot = BOTTOM - BODY_R

        # Nipple: dome on two short sides, standing on the body top.
        self.add_line("nipple-left", (nl, SHOULDER), (nl, dome_y))
        self.add_arc("nipple-dome", (nl, dome_y), (nr, dome_y), radius_x=NIPPLE_R, sweep=True)
        self.add_line("nipple-right", (nr, dome_y), (nr, SHOULDER))
        self.add_contour("nipple", "nipple-left", "nipple-dome", "nipple-right")

        # Body outline, split where the nipple, ring and handles attach.
        self.add_line("body-top-left", (bl, SHOULDER), (nl, SHOULDER))
        self.add_line("body-top-mid", (nl, SHOULDER), (nr, SHOULDER))
        self.add_line("body-top-right", (nr, SHOULDER), (br, SHOULDER))
        self.add_line("body-right-upper", (br, SHOULDER), (br, RING))
        self.add_line("body-right-lower", (br, RING), (br, foot))
        self.add_arc("body-corner-right", (br, foot), (br - BODY_R, BOTTOM), radius_x=BODY_R, sweep=True)
        self.add_line("body-bottom", (br - BODY_R, BOTTOM), (bl + BODY_R, BOTTOM))
        self.add_arc("body-corner-left", (bl + BODY_R, BOTTOM), (bl, foot), radius_x=BODY_R, sweep=True)
        self.add_line("body-left-lower", (bl, foot), (bl, RING))
        self.add_line("body-left-upper", (bl, RING), (bl, SHOULDER))
        self.add_contour("body", "body-top-left", "body-top-mid", "body-top-right", "body-right-upper",
                         "body-right-lower", "body-corner-right", "body-bottom", "body-corner-left",
                         "body-left-lower", "body-left-upper", closed=True)

        # Collar ring line: closes the collar band across the body.
        self.add_line("ring", (bl, RING), (br, RING))

        self.handle("left", -1)
        self.handle("right", 1)

        for a, b in (("nipple-left", "body-top-left"), ("nipple-left", "body-top-mid"),
                     ("nipple-right", "body-top-mid"), ("nipple-right", "body-top-right")):
            self.relate("connect", a, b)
        for side, sign in (("left", -1), ("right", 1)):
            for part in (f"body-{side}-upper", f"body-{side}-lower", f"{side}-handle-bar"):
                self.relate("connect", "ring", part)
            self.relate("connect", f"{side}-handle-bar", f"body-{side}-upper")
            self.relate("connect", f"{side}-handle-bar", f"body-{side}-lower")
