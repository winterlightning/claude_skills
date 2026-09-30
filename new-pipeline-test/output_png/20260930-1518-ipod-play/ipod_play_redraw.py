"""ipod-play (redraw of the new-pipeline traced SVG).

Plan: a classic iPod on VRECT_M (centerline box (10,4)-(38,44)), the
suggested keyshape (score 1.10; VRECT_L's extra width buys nothing here).
- Body: rounded rectangle x 10..38, y 4..44, corner r6 (Lucide
  tablet/smartphone construction: straight sides, quarter-arc corners on
  integer centres). The side walls are split at y=16.
- Screen: the reference's screen-edge construction (the original source
  draws the screen as the body's upper cell under a full-width divider), a
  line y=16 from wall to wall, sharing endpoints with the split walls and
  declared `connect`. The upper cell is 12 tall (8-wide ink opening).
- Click wheel: ring r5 at (24,30), centred on the body axis and in the lower
  cell (16..44): 9 from the divider, the floor and both walls (exact 8 against
  the rounded body comes back `review`, so 9 is used). Ink hole 6.
The whole drawing is mirrored about x=24.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 9.
- keyshape-short-axis (x filled 85%): the body walls sit on x=10/38 and the
  top/bottom on y=4/44, so all four extremes are exactly on the VRECT_M box.
- clearance e0/e1 (2.84), e0/e2 (7.12), e1/e2 (3.61): the inset screen frame is
  replaced by a divider that shares the body walls (a real connection, not a
  gap), so no screen-to-body clearance exists.
- clearance e0/e3 (2.96), e1/e3 (3.04), e2/e3 (7.04): the wheel is 9 from the
  divider, the floor and both walls.
- holes at [17.9,10.0], [28.7,11.1], [23.3,15.6], [15.7,27.3], [32.2,27.3]:
  the pinched slivers between the screen frame, triangle and wheel are gone;
  the remaining openings are the screen cell (8 wide), the lower cell and the
  wheel hole (6).

Not fixed, and why: the play triangle is dropped. The build gate needs a
triangle hole with a centerline inradius of at least 3, so the smallest
triangle is 10x10. The body has 40 units of height, so screen + triangle +
wheel costs 9+10+9 (screen cell) + 9+10+9 (wheel cell) = 56. Screen + triangle
without a wheel (or triangle + wheel dot without a screen, the rejected gpt-6
drawing) both validate. They lose the screen-over-wheel silhouette that makes
the device an iPod. The reviewer rejected that drawing on meaning, so the iPod
identity is kept and "play" is carried only by the name and keywords.
No human head/body, so the head-gap rule does not apply.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "95b0fd3b-05a5-49bd-b7c9-29486aaf4857"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1518-ipod-play/ipod-play_raw.svg"
AUTHOR = "claude-opus-5-5"

L, R, T, B = 10, 38, 4, 44   # body on the VRECT_M centerline box
CR = 6                       # body corner radius
SCREEN_Y = 16                # screen edge (divider)
AXIS = 24
WHEEL_Y, WHEEL_R = 30, 5     # 9 clear of divider, floor and walls


class IpodPlayRedraw(Solo48):
    icon_id = "ipod-play-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("ipod", "ipod play", "mp3 player", "music player")
    keywords = ("ipod", "play", "music", "player", "click wheel", "mp3", "audio", "device")

    def build(self) -> None:
        # Body, clockwise from the top-left corner; walls split at the screen edge.
        self.add_arc("body-tl", (L, T + CR), (L + CR, T), radius_x=CR, sweep=True)
        self.add_line("body-top", (L + CR, T), (R - CR, T))
        self.add_arc("body-tr", (R - CR, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("body-right-up", (R, T + CR), (R, SCREEN_Y))
        self.add_line("body-right-down", (R, SCREEN_Y), (R, B - CR))
        self.add_arc("body-br", (R, B - CR), (R - CR, B), radius_x=CR, sweep=True)
        self.add_line("body-bottom", (R - CR, B), (L + CR, B))
        self.add_arc("body-bl", (L + CR, B), (L, B - CR), radius_x=CR, sweep=True)
        self.add_line("body-left-down", (L, B - CR), (L, SCREEN_Y))
        self.add_line("body-left-up", (L, SCREEN_Y), (L, T + CR))
        self.add_contour(
            "body", "body-tl", "body-top", "body-tr", "body-right-up",
            "body-right-down", "body-br", "body-bottom", "body-bl",
            "body-left-down", "body-left-up", closed=True,
        )

        # Screen: the upper cell under a wall-to-wall edge.
        self.add_line("screen-edge", (L, SCREEN_Y), (R, SCREEN_Y))
        self.relate("connect", "screen-edge", "body")

        # Click wheel: one ring on the axis, no centre button.
        self.add_arc("wheel-right", (AXIS, WHEEL_Y - WHEEL_R), (AXIS, WHEEL_Y + WHEEL_R),
                     radius_x=WHEEL_R, sweep=True)
        self.add_arc("wheel-left", (AXIS, WHEEL_Y + WHEEL_R), (AXIS, WHEEL_Y - WHEEL_R),
                     radius_x=WHEEL_R, sweep=True)
        self.add_contour("wheel", "wheel-right", "wheel-left", closed=True)
