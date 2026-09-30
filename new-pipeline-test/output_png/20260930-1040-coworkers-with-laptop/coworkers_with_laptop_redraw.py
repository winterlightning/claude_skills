"""coworkers-with-laptop (redraw of the new-pipeline traced SVG).

Plan: two user busts side by side behind one shared open laptop, mirrored
about x 24, on SQUARE (centerline box (6,6)-(42,42)).
- heads: r5 circles (four cardinal quarter arcs) about (12,11) / (36,11),
  tops on y 6.
- busts (user.svg construction): a flat crown x 11..13 / 35..37 on y 24,
  exactly 8 below the head outline (4 visible). The outer side is an r5
  corner into a straight side on x 6 / 42 down to y 42; the inner side is a
  matching r5 quarter that drops 5 into the screen's top corner (18,29) /
  (30,29): the laptop occludes the inner halves of both bodies. Both arcs
  are tangent to the crown.
- laptop: screen rectangle (18,29)-(30,42) seen from the front, with a base
  that projects 4 past each side on y 42.
Lucide: `laptop` (screen + wider base) and `users` (paired busts) informed
the parts; the base is joined to the screen bottom because a detached base
needs 8 more height than the keyshape leaves under two busts.
Human reference: icon_set/references/human_ref/user.svg (circle head over
rounded shoulders with an open bottom).

Metric issues (coworkers-with-laptop_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (HRECT_M, x fill 96%): keyshape changed to SQUARE.
  HRECT_M's 28 centerline height cannot stack head (10) + head gap (8) +
  a screen with a 6 hole (10). HRECT_L (32) fits only with the screen top
  2 below the shoulder crowns; at 48 px that reads as a face (two ring eyes
  over one toothed line). SQUARE's 36 lets the shoulders dome 5 above the
  screen. Every extreme is exact: head tops y 6, sides x 6 / 42, bottom y 42.
- clearance e0/e2, e1/e3 (heads 2.5 above the shoulders): each head outline
  is exactly 8 on centerlines above a standalone crown line, flagged with
  mark_human_figure.
- clearance e0/e4, e1/e4, e2/e4, e3/e4 (shoulders 2-8 from the screen):
  the shoulders now end on the screen's top corners (shared endpoints,
  declared connect): the bodies pass behind the laptop instead of hovering
  2 above it. The heads clear the screen by 13.
- clearance e2/e3 (the two inner shoulders 7.8 apart): they now end on the
  screen corners 12 apart.
- clearance e4/e5 (screen 2.4 above the detached base): the base is joined
  to the screen bottom corners; a detached base would need 8 more height.
- holes 4.8 / 4.87 (heads) and 4.8 (screen): heads are r5 (6 inscribed),
  the screen hole is 8 x 9.
- no-head (warn): both heads are real circles.
Not kept: the screen is 12 x 13 rather than landscape; its width is bounded
by the two busts' inner shoulders on the 36-wide square.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8d47f316-c40a-4959-bfb4-5b4ee2cac87e"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1040-coworkers-with-laptop/coworkers-with-laptop_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 12              # left figure axis; the right one mirrors about x 24
HEAD_R = 5
HEAD_CY = 11           # heads span y 6..16
CROWN_Y = HEAD_CY + HEAD_R + 8   # 24: exactly 8 below the head outline
CROWN_HALF = 1         # flat shoulder top x 11..13 under the head
SIDE_X = 6             # keyshape left edge
SHOULDER_R = 5         # outer corner and inner drop
SCREEN_TOP = CROWN_Y + SHOULDER_R          # 29
SCREEN_X0 = AXIS + CROWN_HALF + SHOULDER_R  # 18, where the inner shoulder lands
BOTTOM = 42            # keyshape bottom: bust sides and laptop base
BASE_EAR = 4           # base end stays 8 from the bust side


def mx(x: int) -> int:
    return 48 - x


class CoworkersWithLaptopRedraw(Solo48):
    icon_id = "coworkers-with-laptop-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/work"
    aliases = ("coworkers", "team at laptop", "colleagues with computer", "co-working")
    keywords = ("coworkers", "team", "laptop", "people", "office", "collaboration", "meeting", "work")

    def _bust(self, name: str, flip: bool) -> None:
        """Head, and a shoulder that runs from the outer side into the screen corner."""
        f = mx if flip else (lambda x: x)
        ax, r, cy = f(AXIS), HEAD_R, HEAD_CY
        quarters = ((ax - r, cy), (ax, cy - r), (ax + r, cy), (ax, cy + r))
        for i in range(4):
            self.add_arc(f"{name}-head-{i}", quarters[i], quarters[(i + 1) % 4], radius_x=r)
        self.add_contour(f"{name}-head", *(f"{name}-head-{i}" for i in range(4)), closed=True)

        crown_o, crown_i = f(AXIS - CROWN_HALF), f(AXIS + CROWN_HALF)
        side = f(SIDE_X)
        self.add_line(f"{name}-side", (side, BOTTOM), (side, SCREEN_TOP))
        self.add_arc(
            f"{name}-shoulder-o", (side, SCREEN_TOP), (crown_o, CROWN_Y),
            radius_x=SHOULDER_R, sweep=not flip,
        )
        self.add_contour(f"{name}-outer", f"{name}-side", f"{name}-shoulder-o")
        # The flat crown stands alone so the exact 8 head gap certifies.
        self.add_line(f"{name}-crown", (crown_o, CROWN_Y), (crown_i, CROWN_Y))
        self.add_arc(
            f"{name}-shoulder-i", (crown_i, CROWN_Y), (f(SCREEN_X0), SCREEN_TOP),
            radius_x=SHOULDER_R, sweep=not flip,
        )
        self.relate("connect", f"{name}-outer", f"{name}-crown")
        self.relate("connect", f"{name}-crown", f"{name}-shoulder-i")
        self.relate("connect", f"{name}-shoulder-i", "screen")
        self.mark_human_figure(
            name, head=f"{name}-head", torso=f"{name}-crown", torso_junction="start",
        )

    def build(self) -> None:
        x0, x1 = SCREEN_X0, mx(SCREEN_X0)
        self.add_polyline(
            "screen", (x0, SCREEN_TOP), (x1, SCREEN_TOP), (x1, BOTTOM), (x0, BOTTOM),
            closed=True,
        )
        self.add_line("base-l", (x0 - BASE_EAR, BOTTOM), (x0, BOTTOM))
        self.add_line("base-r", (x1, BOTTOM), (x1 + BASE_EAR, BOTTOM))
        self.relate("connect", "screen", "base-l")
        self.relate("connect", "screen", "base-r")

        self._bust("left", flip=False)
        self._bust("right", flip=True)
