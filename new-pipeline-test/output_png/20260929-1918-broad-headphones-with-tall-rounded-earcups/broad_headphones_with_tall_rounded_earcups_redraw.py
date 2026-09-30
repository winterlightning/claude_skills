"""broad-headphones-with-tall-rounded-earcups (redraw of the new-pipeline traced SVG).

Plan: front view of over-ear headphones on HRECT_L (centerline box (4,8)-(44,40)),
symmetric about x=24.
- cups: two closed capsules, 10 wide and 16 tall (x 4-14 and 34-44, y 24-40).
  Each is a top semicircle r5 about (cx,29), straight sides from y=29 to y=35 and
  a bottom semicircle r5 about (cx,35). The top semicircle is split at its apex
  (cx,24), where the band lands.
- band: two elliptical quarter arcs, rx 15 / ry 16 about (24,24), from the left cup
  apex (9,24) over the top (24,8) to the right cup apex (39,24). The ends are
  vertical, so the band drops straight onto each cup like the generated image.
  Contact is declared with relate("connect") on the shared apex only.
- extremes: cup outer sides x=4/44, band top y=8, cup bottoms y=40.
Dropped from the image: the short straight stems between the arch and the cups.
At 48 px they would be 1-2 units long, so the arch runs straight into the cups.
Lucide `headphones` informed the construction: an arched band whose ends fall
vertically onto paired rounded cups. Its cups are open "D" shapes; here they are
closed capsules because the brief asks for tall hollow earcups.

Metric issues (broad-headphones-with-tall-rounded-earcups_metrics.json):
- hole [9.2, 27.5] and [38.6, 27.5] (3.6 wide): fixed. The cups are 10 wide on
  centerlines, so each opening is 6 x 12 in ink, meeting the 6 inscribed floor.
- keyshape-short-axis (x fill 92%): fixed without stretching the trace. The cups
  sit on x=4 and x=44, and the band top sits on y=8.
- stroke-width (trace 2.47): redrawn at stroke 4. The gap between the cups is 20
  on centerlines, and the band clears the cups by more than 8 away from the joint.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b737e5e2-78be-44b5-be8e-53fa1fe642af"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1918-broad-headphones-with-tall-rounded-earcups/broad-headphones-with-tall-rounded-earcups_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
CUP_R = 5                       # capsule end radius; cup width is 2 * CUP_R
CUP_TOP, CUP_BOTTOM = 24, 40
CUP_CX = (4 + CUP_R, 44 - CUP_R)
BAND_TOP = 8


class BroadHeadphonesWithTallRoundedEarcupsRedraw(Solo48):
    icon_id = "broad-headphones-with-tall-rounded-earcups-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("over-ear headphones", "headset")
    keywords = ("headphones", "earcups", "headband", "audio", "listening", "music", "sound")

    def _cup(self, name: str, cx: int) -> None:
        r, top, bottom = CUP_R, CUP_TOP, CUP_BOTTOM
        l, rr = cx - r, cx + r
        y1, y2 = top + r, bottom - r
        self.add_arc(f"{name}-top-right", (cx, top), (rr, y1), radius_x=r, sweep=True)
        self.add_line(f"{name}-right", (rr, y1), (rr, y2))
        self.add_arc(f"{name}-bottom", (rr, y2), (l, y2), radius_x=r, sweep=True)
        self.add_line(f"{name}-left", (l, y2), (l, y1))
        self.add_arc(f"{name}-top-left", (l, y1), (cx, top), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-top-right", f"{name}-right", f"{name}-bottom",
                         f"{name}-left", f"{name}-top-left", closed=True)

    def build(self) -> None:
        self._cup("cup-left", CUP_CX[0])
        self._cup("cup-right", CUP_CX[1])

        rx, ry = AXIS - CUP_CX[0], CUP_TOP - BAND_TOP
        self.add_arc("band-left", (CUP_CX[0], CUP_TOP), (AXIS, BAND_TOP), radius_x=rx, radius_y=ry, sweep=True)
        self.add_arc("band-right", (AXIS, BAND_TOP), (CUP_CX[1], CUP_TOP), radius_x=rx, radius_y=ry, sweep=True)
        self.add_contour("band", "band-left", "band-right")

        self.relate("connect", "band", "cup-left")
        self.relate("connect", "band", "cup-right")
