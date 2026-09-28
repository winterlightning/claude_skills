"""bareheaded delivery rider on scooter (redraw of the new-pipeline traced SVG).

Plan: side view facing right on SQUARE (centerline box (6,6)-(42,42)). The
trace is square (aspect 1.00) and SQUARE fills it 1.0/1.0 with no stretch,
while the suggested HRECT_L needs a 1.25 x-stretch, so SQUARE is the better fit.
- wheels: two r5 rings of cardinal quarter arcs about (11,37) and (37,37);
  they set the x=6 / x=42 / y=42 extremes and keep a 6-wide hole.
- deck: axle-height line from the rear wheel's east node (16,37) to the front
  wheel's west node (32,37), split at the foot (24,37).
- steering column: 1:4 line from the front wheel's top node (37,32) up to the
  handlebar/hand H=(34,20).
- rider: bare r4 ring head about (27,10) (top = y=6 extreme); a vertical neck
  stub (27,22)-(27,24) sits exactly 8 under the head outline; the shoulder
  S=(27,24) branches an arm rising to H (8.2 clear of the head) and a
  forward-leaning torso back to the hip (24,30); one straight leg drops to
  the deck at (24,37), exactly 8 from both wheels.
- delivery box: 10x10 rounded box (6,14)-(16,24), r2 corners, on a rack
  stem from its bottom middle (11,24) to the rear wheel's top node (11,32).
Reference: icon_set/references/human_ref/full_body_ref.png (ring head,
single round-ended limbs); Lucide `package`/`box` only for the rounded box.
No Lucide scooter exists.
Metric issues fixed:
- keyshape-short-axis (HRECT_L 80% x fill): switched to SQUARE, every extreme
  sits on the box exactly.
- clearance e0/e5 (head vs body 2.65) and the human head gap: the head is a
  detached ring with an exact 8-unit centerline (4 ink) gap to a vertical neck.
- clearances e2/e3, e3/e4, e3/e5, e4/e5, e5/e6: the fender arc (e6) is dropped,
  the box hangs on a stem 8 above the rear wheel, the rider sits 8+ from box,
  wheels and column; touching parts share nodes and are declared connect.
- loose joins e4/e6, e6/e2, e6/e3 and narrow joins e6/e2, e6/e3: the fender
  wedge is gone; deck, stem and column end on wheel cardinal nodes.
- holes (2.0-5.8 wide): the wheel, box and rider openings are now >= 6.
  Not fixed: the r4 head ring keeps a 4-wide hole (the metrics ask for 6).
  An r5 head would need 2 more units of height, which the SQUARE budget
  (head + 8 gap + torso + leg above the deck) cannot spare. The validator
  accepts it, and r4 is the set's standard stick-figure head.
- stroke-count 7 > 6 and stroke width: rebuilt at stroke 4 with gaps sized
  for it.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9046ec78-1a6b-4029-a2e9-be0d10843436"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1729-bareheaded-delivery-rider-on-scooter/"
    "bareheaded-delivery-rider-on-scooter_raw.svg"
)
AUTHOR = "claude-opus-5-5"

WHEEL_R = 5
REAR_WHEEL = (11, 37)
FRONT_WHEEL = (37, 37)
FOOT = (24, 37)
HIP = (24, 30)
HEAD = (27, 10)
HEAD_R = 4
NECK = (27, 22)          # HEAD y + HEAD_R + 8
SHOULDER = (27, 24)
HAND = (34, 20)          # on the 1:4 column from the front wheel top
BOX = dict(left=6, top=14, right=16, bottom=24, r=2)


class BareheadedDeliveryRiderOnScooterRedraw(Solo48):
    icon_id = "bareheaded-delivery-rider-on-scooter-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport"
    aliases = ("delivery scooter", "courier on scooter")
    keywords = ("delivery", "courier", "rider", "scooter", "box", "food delivery", "transport")

    def ring(self, name: str, centre: tuple[int, int], r: int) -> None:
        cx, cy = centre
        pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
        for i in range(4):
            self.add_arc(f"{name}-{i + 1}", pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour(name, *(f"{name}-{i + 1}" for i in range(4)), closed=True)

    def build(self) -> None:
        self.ring("rear-wheel", REAR_WHEEL, WHEEL_R)
        self.ring("front-wheel", FRONT_WHEEL, WHEEL_R)

        rear_east = (REAR_WHEEL[0] + WHEEL_R, REAR_WHEEL[1])
        front_west = (FRONT_WHEEL[0] - WHEEL_R, FRONT_WHEEL[1])
        self.add_line("deck-rear", rear_east, FOOT)
        self.add_line("deck-front", FOOT, front_west)
        self.relate("connect", "deck-rear", "rear-wheel")
        self.relate("connect", "deck-front", "front-wheel")
        self.relate("connect", "deck-rear", "deck-front")

        front_top = (FRONT_WHEEL[0], FRONT_WHEEL[1] - WHEEL_R)
        self.add_line("column", front_top, HAND)
        self.relate("connect", "column", "front-wheel")

        self.ring("head", HEAD, HEAD_R)
        self.add_line("neck", NECK, SHOULDER)
        self.mark_human_figure("rider", head="head", torso="neck", torso_junction="start")
        self.add_line("torso", SHOULDER, HIP)
        self.add_line("arm", SHOULDER, HAND)
        self.add_line("leg", HIP, FOOT)
        self.relate("connect", "neck", "torso")
        self.relate("connect", "neck", "arm")
        self.relate("connect", "torso", "arm")
        self.relate("connect", "torso", "leg")
        self.relate("connect", "arm", "column")
        self.relate("connect", "leg", "deck-rear")
        self.relate("connect", "leg", "deck-front")

        L, T, R, B, r = BOX["left"], BOX["top"], BOX["right"], BOX["bottom"], BOX["r"]
        mid = ((L + R) // 2, B)
        self.add_line("box-bottom-r", mid, (R - r, B))
        self.add_arc("box-br", (R - r, B), (R, B - r), radius_x=r, sweep=False)
        self.add_line("box-right", (R, B - r), (R, T + r))
        self.add_arc("box-tr", (R, T + r), (R - r, T), radius_x=r, sweep=False)
        self.add_line("box-top", (R - r, T), (L + r, T))
        self.add_arc("box-tl", (L + r, T), (L, T + r), radius_x=r, sweep=False)
        self.add_line("box-left", (L, T + r), (L, B - r))
        self.add_arc("box-bl", (L, B - r), (L + r, B), radius_x=r, sweep=False)
        self.add_line("box-bottom-l", (L + r, B), mid)
        self.add_contour(
            "box", "box-bottom-r", "box-br", "box-right", "box-tr", "box-top",
            "box-tl", "box-left", "box-bl", "box-bottom-l", closed=True,
        )
        rear_top = (REAR_WHEEL[0], REAR_WHEEL[1] - WHEEL_R)
        self.add_line("stem", mid, rear_top)
        self.relate("connect", "stem", "box")
        self.relate("connect", "stem", "rear-wheel")
