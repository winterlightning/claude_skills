"""browser-user-profile (redraw of the new-pipeline traced SVG).

Subject: a user's profile page in a browser window. It is a wide rounded
window with a top bar and a user bust (round head on a shoulder arch) in
the middle.

Plan: HRECT_L (centerline box (4,8)-(44,40)) instead of the suggested
HRECT_M. At stroke 4 the vertical budget is the constraint: the top wall,
the bar row (8), a head with a >= 6 inscribed hole (r5 = 10), the bust
contact (4) and a >= 6 inscribed shoulder opening (10) need 32 on centerlines.
HRECT_M's 28 cannot hold that. All four HRECT_L extremes are exact.
- window: one closed contour with r4 corners. The side walls are split at the
  bar row and the bottom wall where the shoulders land, so every
  attachment is a shared integer node with a scoped connect.
- top bar: drawn as two 8-long stubs off the side walls at y=16, stopping
  8 from the head ring. A full-width bar needs its own 10-deep band (a
  closed strip under the top wall must be >= 6 inscribed) plus 8 clearance
  above the head. That is 40 of height, more than any wide keyshape has. The
  head therefore sits in the bar row, like a profile-header avatar, and the
  stubs keep the browser chrome readable.
- bust: circular head r5 at (24,21) resting on an elliptical shoulder arch
  (centre (24,40), rx12 ry10) that lands on the bottom wall. The head and arch
  share the x=24 axis, with head bottom 26 and arch top 30 (ink touching).
  human_construction = "bust" plus connect certifies that contact
  (internal_spacing._avatar_tangent_contact).
References: icon_set/references/human_ref/user.svg (round head over a
shoulder arch) and Lucide square-user / app-window (shoulders landing on
the frame's bottom edge; window with a top-bar row).
Dropped: the detached head gap of the trace. A detached head needs 8 more
units of height, so the bust uses the certified touching avatar construction.

Metric issues fixed:
- clearance e0/e1 (bar 3.89 under the top wall): the bar stubs sit 8 below
  the top wall and are not closed into a strip.
- clearance e0/e2, e1/e2 (head crowding the bar and top wall): the head top
  is exactly 8 from the top wall, and the stubs end >= 8 from the ring.
- clearance e1/e3 (shoulders on the bottom wall, 3.87): the shoulder ends
  now land on the bottom wall as shared nodes with a scoped connect.
- clearance e2/e3 (head 1.62 above the shoulders): head and arch form the
  certified bust contact on one axis (exactly 4 on centerlines).
- holes 1.97 and 4.8 wide: the head ring is r5 (inscribed 6). The shoulder
  opening is 10 deep (inscribed >= 6). The build gate reports no hole findings.
- no-head: the head is a true circle (two semicircle arcs).
- keyshape-short-axis (y 84% of HRECT_M): HRECT_L with every extreme exact.
- stroke-width (2.63 trace): redrawn at stroke 4 with every gap budgeted.
Validation: validate_icon() valid, build_gate PASS (0 errors, 0 warnings).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3a3e4d85-115c-4ccb-82d1-46fd45222b3a"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1725-browser-user-profile/browser-user-profile_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, TOP, RIGHT, BOTTOM = 4, 8, 44, 40   # HRECT_L centerline box
CORNER = 4                                 # window corner radius
BAR_Y = 16                                 # top-bar row, 8 below the top wall
AXIS = 24                                  # shared figure axis
HEAD_R = 5
HEAD_CY = 21                               # head 16..26 (top 8 below the top wall)
SHOULDER_RX, SHOULDER_RY = 12, 10          # arch centre (24,40): top 30 = head bottom + 4
BAR_END = 12                               # stubs stop 8 short of the head ring


class BrowserUserProfileRedraw(Solo48):
    icon_id = "browser-user-profile-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "objects/web"
    aliases = ("browser profile", "web profile", "user profile page", "account page")
    keywords = ("browser", "window", "web", "user", "profile", "account", "person", "avatar", "page")

    def build(self) -> None:
        l, t, r, b, c = LEFT, TOP, RIGHT, BOTTOM, CORNER
        sl, sr = AXIS - SHOULDER_RX, AXIS + SHOULDER_RX
        self.add_arc("corner-tl", (l, t + c), (l + c, t), radius_x=c, sweep=True)
        self.add_line("top", (l + c, t), (r - c, t))
        self.add_arc("corner-tr", (r - c, t), (r, t + c), radius_x=c, sweep=True)
        self.add_line("right-upper", (r, t + c), (r, BAR_Y))
        self.add_line("right-lower", (r, BAR_Y), (r, b - c))
        self.add_arc("corner-br", (r, b - c), (r - c, b), radius_x=c, sweep=True)
        self.add_line("bottom-right", (r - c, b), (sr, b))
        self.add_line("bottom-mid", (sr, b), (sl, b))
        self.add_line("bottom-left", (sl, b), (l + c, b))
        self.add_arc("corner-bl", (l + c, b), (l, b - c), radius_x=c, sweep=True)
        self.add_line("left-lower", (l, b - c), (l, BAR_Y))
        self.add_line("left-upper", (l, BAR_Y), (l, t + c))
        self.add_contour(
            "window", "corner-tl", "top", "corner-tr", "right-upper", "right-lower",
            "corner-br", "bottom-right", "bottom-mid", "bottom-left", "corner-bl",
            "left-lower", "left-upper", closed=True,
        )

        # Top bar, split by the avatar head: two stubs off the side walls.
        self.add_line("bar-left", (l, BAR_Y), (BAR_END, BAR_Y))
        self.add_line("bar-right", (2 * AXIS - BAR_END, BAR_Y), (r, BAR_Y))
        self.relate("connect", "bar-left", "window")
        self.relate("connect", "bar-right", "window")

        # Bust: circular head resting on the shoulder arch (certified bust contact).
        hx, hy, hr = AXIS, HEAD_CY, HEAD_R
        self.add_arc("head-top", (hx - hr, hy), (hx + hr, hy), radius_x=hr, sweep=True)
        self.add_arc("jaw", (hx + hr, hy), (hx - hr, hy), radius_x=hr, sweep=True)
        self.add_contour("head", "head-top", "jaw", closed=True)
        self.add_arc("shoulders", (sl, b), (sr, b), radius_x=SHOULDER_RX, radius_y=SHOULDER_RY, sweep=True)
        self.relate("connect", "head", "shoulders")
        self.relate("connect", "shoulders", "window")
