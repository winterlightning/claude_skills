"""delivery-worker-beside-loaded-hand-truck (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)), the keyshape the metrics suggest.
- worker (left, facing right) on the axis x=HX: 4-arc circle head r5 whose top
  is the y=6 extreme; torso from the neck, exactly 8 centerline units under the
  head outline (4-unit ink gap, human-reference.md), through the shoulder to
  the hip; mirrored inverted-V legs whose left foot is the x=6 extreme and both
  feet the y=42 extreme.
- arm: one straight stroke from the shoulder (split point on the torso, 2 under
  the neck) up to the hand-truck handle; the shallow rise keeps it >8 from the head.
- hand truck: one L contour, upright from the handle down to the toe corner,
  toe plate out to the x=42 extreme, split at the axle point.
- wheel: r5 ring hung tangent under the toe plate at the axle point (shared
  endpoint, declared connect); its bottom is the y=42 extreme.
- parcel: hollow 11x11 square 8 right of the upright and 8 above the plate; its
  right wall is the x=42 extreme.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs). No useful Lucide hand-truck original; the
parcel follows Lucide's plain square construction, the wheel its 4-arc circle.
Deliberate asymmetry: a side-view scene, worker left, truck right.

Metric issues fixed:
- stroke-width 2.4 -> redrawn at stroke 4 with every gap budgeted for it.
- stroke-count 10 -> 7 grouped parts (head, torso, legs, arm, truck, wheel,
  parcel); no loose trace fragments.
- keyshape-short-axis: x now spans exactly 6..42 (rear foot to parcel/plate).
- clearance e0/e3, e0/e4, e0/e5 (head vs torso/arm): neck exactly 8 under the
  head outline; arm starts 2 lower and stays >8 from the head.
- clearance e1/e2 (legs): symmetric legs, >8 apart beyond the hip joint.
- clearance e3/e5, e4/e6, e5/e8, e6/e8, e6/e9, e7/e8, e7/e9, e8/e9 (arm,
  handle, upright, parcel, plate, wheel crowding): every distinct pair is >= 8
  on centerlines; the wheel now genuinely touches the plate (connect) instead
  of hovering 2 under it.
- hole 2.53 (head) and 5.6 (parcel): head r5 and wheel r5 holes are 6, the
  parcel hole 7, all at or above the 6 inscribed minimum.
- no-head: the head is a true circle, paired via mark_human_figure.
validate_icon(): valid, zero warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1259b062-7e36-4616-83b9-d5d1aa90e70f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1202-delivery-worker-beside-loaded-hand-truck/"
    "delivery-worker-beside-loaded-hand-truck_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 12            # worker axis
HEAD_R = 5
HEAD_CY = 11       # head top on y=6
NECK_Y = 24        # HEAD_CY + HEAD_R + 8
SHOULDER = (HX, 26)
HIP = (HX, 33)
LEG_SPREAD = 6
FOOT_Y = 42
UPRIGHT_X = 23
HANDLE = (UPRIGHT_X, 20)
PLATE_Y = 32
RIGHT = 42
BOX = dict(left=31, top=13, right=RIGHT, bottom=PLATE_Y - 8)
WHEEL_R = 5
WHEEL_CX = 31      # axle point on the plate; wheel bottom on y=42


def _circle(icon, element_id, cx, cy, r):
    icon.add_arc(f"{element_id}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
    icon.add_arc(f"{element_id}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
    icon.add_arc(f"{element_id}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
    icon.add_arc(f"{element_id}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
    icon.add_contour(element_id, *(f"{element_id}-{i}" for i in range(1, 5)), closed=True)


class DeliveryWorkerBesideLoadedHandTruckRedraw(Solo48):
    icon_id = "delivery-worker-beside-loaded-hand-truck-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/delivery"
    aliases = ("delivery person with hand truck", "courier with dolly")
    keywords = ("delivery", "worker", "courier", "hand truck", "dolly", "parcel", "box", "moving")

    def build(self) -> None:
        _circle(self, "head", HX, HEAD_CY, HEAD_R)

        self.add_line("torso", (HX, NECK_Y), SHOULDER)
        self.add_line("waist", SHOULDER, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("worker", head="head", torso="torso", torso_junction="start")

        self.add_line("rear-leg", HIP, (HX - LEG_SPREAD, FOOT_Y))
        self.add_line("front-leg", HIP, (HX + LEG_SPREAD, FOOT_Y))
        self.relate("connect", "rear-leg", "waist")
        self.relate("connect", "front-leg", "waist")
        self.relate("connect", "rear-leg", "front-leg")

        self.add_line("arm", SHOULDER, HANDLE)
        self.relate("connect", "arm", "torso")
        self.relate("connect", "arm", "waist")

        axle = (WHEEL_CX, PLATE_Y)
        self.add_polyline("truck", HANDLE, (UPRIGHT_X, PLATE_Y), axle, (RIGHT, PLATE_Y))
        self.relate("connect", "truck", "arm")

        _circle(self, "wheel", WHEEL_CX, PLATE_Y + WHEEL_R, WHEEL_R)
        self.relate("connect", "wheel", "truck")

        L, T, R, B = BOX["left"], BOX["top"], BOX["right"], BOX["bottom"]
        self.add_polyline("parcel", (L, T), (R, T), (R, B), (L, B), closed=True)
