"""customer-at-information-desk (redraw of the new-pipeline traced SVG).

Plan: two user busts on HRECT_L (centerline box (4,8)-(44,40)) -- a customer
standing on the left and an attendant behind a service counter on the right.
- One shared bust vocabulary (icon_set/references/human_ref/user.svg, Lucide
  `user`): head = 4-cardinal-arc circle r HEAD_R; shoulders = r4 rounded
  corners with a level top run, so the head outline sits exactly 8 above a
  straight run on the same axis (4 units of visible ink gap).
- Customer: shoulders drop into short straight sides (Lucide `user`), open
  at the bottom; the counter owns the bottom extreme.
- Attendant: same head and shoulder top, standing behind the counter: the
  counter's top edge rises over the shoulders, so counter and attendant are
  one closed panel (a separate shoulder arc on the counter would enclose a
  4-tall pocket, and there is no room to raise it).
- Counter: a closed rectangle on the right and bottom extremes, 10 tall so the
  panel keeps a 6-unit opening.
- Both heads share the top extreme; customer's left side is the left extreme.
- Human flags: each head is paired with its level shoulder run (torso).
- Lucide `user` informed the bust (circle head, rounded shoulders, open sides).

Metric issues repaired:
- stroke-width: redrawn at stroke 4; every gap re-budgeted for 4.
- keyshape-short-axis: HRECT_M was suggested at 85% y-fill; the r5 heads
  (needed for 6-unit head holes), the exact 8 head gap and a 10-tall counter
  need 32 units, so HRECT_L is used and every extreme lands on its box.
- clearance e0/e3 and e1/e2 (heads on shoulders) and human head gap: both
  heads sit exactly 8 on centerlines above a level shoulder run.
- clearance e2/e4 (customer to counter): the customer's side and the counter's
  wall are straight and parallel, a full 8 apart.
- clearance e3/e4 (attendant shoulders 2.3 above the counter): the shoulders
  become the counter's top edge in their span, so there is no gap to measure.
- holes: heads (3.4 -> r5 leaves 6 inside); the 2.0 pocket between the
  attendant's shoulders and the counter is gone (merged panel); the counter
  panel (3.8 -> 10 tall leaves 6 inside, more under the shoulders).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6c38d9c8-0e42-5dd8-a256-2b9b12046c18"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1040-customer-at-information-desk/"
    "customer-at-information-desk_raw.svg"
)
AUTHOR = "claude-opus-5-5"

TOP, BOTTOM, LEFT, RIGHT = 8, 40, 4, 44
HEAD_R = 5
GAP = 8                       # head outline -> shoulder run, on centerlines
CORNER = 4                    # shoulder corner radius
HALF = 6                      # shoulder half-width
HEAD_CY = TOP + HEAD_R
SHOULDER_Y = HEAD_CY + HEAD_R + GAP          # level shoulder run
SIDE_Y = SHOULDER_Y + CORNER                 # where the corners turn vertical
BUST_BOTTOM = SIDE_Y + 6                     # short Lucide-user sides

CUSTOMER_X = LEFT + HALF
COUNTER_L = CUSTOMER_X + HALF + 8            # parallel walls 8 apart
COUNTER_TOP = SIDE_Y
ATTENDANT_X = (COUNTER_L + RIGHT) // 2


class CustomerAtInformationDeskRedraw(Solo48):
    icon_id = "customer-at-information-desk-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/service"
    aliases = ("information desk", "help desk", "reception", "front desk")
    keywords = ("customer", "service", "desk", "counter", "reception",
                "information", "help", "attendant", "clerk", "support")

    def head(self, name: str, cx: int) -> None:
        cy, r = HEAD_CY, HEAD_R
        self.add_arc(f"{name}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc(f"{name}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", f"{name}-3", f"{name}-4",
                         closed=True)

    def shoulders(self, name: str, cx: int) -> list[str]:
        """Left corner, level run, right corner; returns member ids."""
        l, r = cx - HALF, cx + HALF
        self.add_arc(f"{name}-left", (l, SIDE_Y), (l + CORNER, SHOULDER_Y),
                     radius_x=CORNER, sweep=True)
        self.add_line(f"{name}-top", (l + CORNER, SHOULDER_Y), (r - CORNER, SHOULDER_Y))
        self.add_arc(f"{name}-right", (r - CORNER, SHOULDER_Y), (r, SIDE_Y),
                     radius_x=CORNER, sweep=True)
        return [f"{name}-left", f"{name}-top", f"{name}-right"]

    def build(self) -> None:
        # Customer: head over a Lucide-user bust reaching the bottom extreme.
        self.head("customer-head", CUSTOMER_X)
        l, r = CUSTOMER_X - HALF, CUSTOMER_X + HALF
        self.add_line("customer-side-left", (l, BUST_BOTTOM), (l, SIDE_Y))
        members = self.shoulders("customer-shoulders", CUSTOMER_X)
        self.add_line("customer-side-right", (r, SIDE_Y), (r, BUST_BOTTOM))
        self.add_contour("customer-body", "customer-side-left", *members,
                         "customer-side-right")
        self.mark_human_figure("customer", head="customer-head",
                               torso="customer-shoulders-top", torso_junction="start")

        # Counter + attendant: one closed panel whose top edge rises over the
        # attendant's shoulders, so the attendant stands behind the desk.
        self.head("attendant-head", ATTENDANT_X)
        al, ar = ATTENDANT_X - HALF, ATTENDANT_X + HALF
        self.add_line("counter-top-left", (COUNTER_L, COUNTER_TOP), (al, COUNTER_TOP))
        members = self.shoulders("attendant-shoulders", ATTENDANT_X)
        self.add_line("counter-top-right", (ar, COUNTER_TOP), (RIGHT, COUNTER_TOP))
        self.add_line("counter-right", (RIGHT, COUNTER_TOP), (RIGHT, BOTTOM))
        self.add_line("counter-bottom", (RIGHT, BOTTOM), (COUNTER_L, BOTTOM))
        self.add_line("counter-left", (COUNTER_L, BOTTOM), (COUNTER_L, COUNTER_TOP))
        self.add_contour("counter", "counter-top-left", *members, "counter-top-right",
                         "counter-right", "counter-bottom", "counter-left", closed=True)
        self.mark_human_figure("attendant", head="attendant-head",
                               torso="attendant-shoulders-top", torso_junction="start")
