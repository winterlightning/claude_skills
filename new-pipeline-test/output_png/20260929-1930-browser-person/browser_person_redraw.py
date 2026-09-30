"""browser-person (redraw of the new-pipeline traced SVG).

Plan: a rounded browser window with a toolbar divider and a detached-head
user bust in the content area (Lucide `square-user` / `app-window`).
- window: rounded rectangle on the whole SQUARE centerline box (6,6)-(42,42),
  corner radius 4; side walls split at the toolbar so the divider shares
  their nodes (declared connect).
- toolbar divider: y=14, exactly 8 below the top wall.
- head: 4-cardinal-arc circle r3 at (24,25); its top (y=22) sits 8 below the
  divider.
- bust: two quarter-ellipse arcs (rx 10, ry 6) from the bottom wall at x=14 up
  to the apex (24,36) and back down to x=34 (8 from the side walls), landing
  on split nodes of the bottom wall (Lucide square-user bust meeting the
  frame). The apex is 8 below the head
  outline (4-unit ink gap, human-reference.md, `user.svg`).
Vertical budget: 8 toolbar + 8 clear + 6 head + 8 neck gap + 6 bust = 36.
Keyshape: metrics suggested HRECT_M (28 tall) with HRECT_L (32) next, but that
budget needs 36 on the vertical axis, so SQUARE (36x36) is used; the window
still reads as a browser, only less wide than the trace (aspect 1.37 -> 1).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
- keyshape-short-axis: all four extremes on the SQUARE box exactly.
- clearance e0/e1 (divider 5.6 under the top wall): divider now 8 below it.
- clearance e0/e2 (divider vs head 3.6): head top 8 below the divider.
- clearance e1/e3 (bust ends 4.2 above the bottom wall): the bust now lands on
  the bottom wall on shared nodes (declared connect) instead of hovering.
- clearance e2/e3 (head vs shoulders 2.0): exact 8 centerline head gap.
- hole at the toolbar corner (1.6): toolbar band is 8 tall with r4 corners.
- hole inside the head (2.4): head is an r3 ring (exempt 6 circle).
- no-head: head drawn as a true circle and flagged with mark_human_figure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3a3e4d85-115c-4ccb-82d1-46fd45222b3a"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1930-browser-person/browser-person_raw.svg"
AUTHOR = "claude-opus-5-5"

L, T, R, B = 6, 6, 42, 42   # window centerline box
CR = 4                      # window corner radius
BAR_Y = T + 8               # toolbar divider
AX = 24                     # figure axis
HEAD_R = 3
HEAD_CY = BAR_Y + 8 + HEAD_R
BUST_TOP = HEAD_CY + HEAD_R + 8
BUST_RX, BUST_RY = 10, B - BUST_TOP


class BrowserPersonRedraw(Solo48):
    icon_id = "browser-person-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("web profile", "user page", "account window")
    keywords = ("browser", "window", "person", "user", "profile", "account", "web")

    def build(self) -> None:
        bl, br = AX - BUST_RX, AX + BUST_RX
        self.add_line("top", (L + CR, T), (R - CR, T))
        self.add_arc("c-tr", (R - CR, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("right-bar", (R, T + CR), (R, BAR_Y))
        self.add_line("right", (R, BAR_Y), (R, B - CR))
        self.add_arc("c-br", (R, B - CR), (R - CR, B), radius_x=CR, sweep=True)
        self.add_line("bottom-r", (R - CR, B), (br, B))
        self.add_line("bottom-m", (br, B), (bl, B))
        self.add_line("bottom-l", (bl, B), (L + CR, B))
        self.add_arc("c-bl", (L + CR, B), (L, B - CR), radius_x=CR, sweep=True)
        self.add_line("left", (L, B - CR), (L, BAR_Y))
        self.add_line("left-bar", (L, BAR_Y), (L, T + CR))
        self.add_arc("c-tl", (L, T + CR), (L + CR, T), radius_x=CR, sweep=True)
        self.add_contour(
            "window", "top", "c-tr", "right-bar", "right", "c-br", "bottom-r",
            "bottom-m", "bottom-l", "c-bl", "left", "left-bar", "c-tl", closed=True,
        )

        self.add_line("toolbar", (L, BAR_Y), (R, BAR_Y))
        self.relate("connect", "toolbar", "window")

        cx, cy, r = AX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        apex = (AX, BUST_TOP)
        self.add_arc("bust-l", (bl, B), apex, radius_x=BUST_RX, radius_y=BUST_RY, sweep=True)
        self.add_arc("bust-r", apex, (br, B), radius_x=BUST_RX, radius_y=BUST_RY, sweep=True)
        self.add_contour("bust", "bust-l", "bust-r")
        self.relate("connect", "bust", "window")
        self.mark_human_figure("person", head="head", torso="bust-l", torso_junction="end")
