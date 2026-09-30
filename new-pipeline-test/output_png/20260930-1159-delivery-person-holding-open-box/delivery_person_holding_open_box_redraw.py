"""delivery-person-holding-open-box (redraw of the new-pipeline traced SVG).

Plan: a person holding an open box against the chest, mirrored about x=24,
on SQUARE (centerline box (6,6)-(42,42)), the keyshape the metrics suggest.
- head: 4-cardinal-arc ring, r4, centre (24,10); its top is the top extreme.
- box: one closed square-cornered contour 20x20, walls x=14/34, rim y=22,
  bottom y=42 (the bottom extreme). The box covers the chest, so its rim is
  the torso line: split at the neck (24,22), exactly 8 under the head outline
  (4-unit ink gap), flagged with mark_human_figure (torso = rim-r, start).
- arms: from each rim corner an r8 shoulder arc out to x=6 / x=42 (the
  left/right extremes), a short upper arm down to the elbow (6,34), and a
  45 degree forearm in to the hand under the box's bottom corner (14,42).
- flaps: the two open flaps fold out from the rim corners at 2:1, up and out
  to (6,18)/(42,18), over the shoulders as in the generated image.
References: icon_set/references/human_ref/user.svg and full_body_ref.png (ring
head, round shoulders, single-stroke limbs); Lucide `package-open` for flaps
hinged on the box's top corners. Candidates tried and rejected at 48 px:
bust sides into the box with 45 degree flaps (read as raised arms), a V rim
(read as the letter M), flaps landing on the shoulder arcs (read as a gem),
and 45 degree flaps (read as antennae).

Metric issues:
- clearance e0/e1 (head 2.9 from the shoulders): the torso line is now 8 under
  the head outline.
- clearance e1/e2..e5 (shoulder ends 2-7 from the flaps, arms and box): the
  shoulders are now the start of the arms and meet the box at its rim
  corners (declared connections), so there are no loose ends to crowd.
- clearance e3/e5, e4/e5 (hands 1.9 from the box walls): the hands now join
  the box at its bottom corners (declared connections).
- holes at (19.1,28.2), (28.9,28.2), (11.2,32.7), (36.8,32.6) (slivers of 0.6-1)
  and (23.9,22.5) (4.4): the flap parallelograms are now single strokes. The
  only enclosed regions are the 20x20 box and the two arm loops (10 wide at
  the elbow), all well above the hole floor.
- hole at (24,10.7) (head 5.4): the ring is r4 (8 across on centerlines).
  build_gate's hole check passes it, and r5 does not fit: it needs 2 more
  units of height, which only the box could give up.
- keyshape-short-axis (x filled 86%): the elbows and flap tips reach x=6/42.
- no-head: the head is a true ring.
- stroke-width (trace 2.39): redrawn at stroke 4 with 8-unit gaps.
None left unrepaired. validate_icon() valid, build_gate.py PASS (0/0).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2cf7fe47-0bae-52b2-a6ad-0ac50b09764f"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1159-delivery-person-holding-open-box/delivery-person-holding-open-box_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                 # body axis
HEAD_R = 4
HEAD_CY = 10            # head top at y=6 (SQUARE top)
RIM_Y = HEAD_CY + HEAD_R + 8   # box top at the neck line, 8 under the head outline
BOX_HALF = 10           # box walls at x=14 and x=34
BOTTOM_Y = 42           # SQUARE bottom
SHOULDER_R = 8          # shoulder arc from the rim corner out to x=6 / x=42
ELBOW_Y = 34            # upper arm straight down to here, then 45 degrees to the box corner
FLAP = 8                # flaps fold open 2:1, up and out to x=6 / x=42


class DeliveryPersonHoldingOpenBoxRedraw(Solo48):
    icon_id = "delivery-person-holding-open-box-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/work"
    aliases = ("courier with open box", "person holding box", "unboxing")
    keywords = ("delivery", "courier", "parcel", "package", "box", "open box", "unboxing", "shipping")

    def build(self) -> None:
        r = HEAD_R
        self.add_arc("head-1", (AX, HEAD_CY - r), (AX + r, HEAD_CY), radius_x=r, sweep=True)
        self.add_arc("head-2", (AX + r, HEAD_CY), (AX, HEAD_CY + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (AX, HEAD_CY + r), (AX - r, HEAD_CY), radius_x=r, sweep=True)
        self.add_arc("head-4", (AX - r, HEAD_CY), (AX, HEAD_CY - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        left, right = AX - BOX_HALF, AX + BOX_HALF
        # Box held in front of the chest; the rim is split at the neck (24,22).
        self.add_line("rim-l", (left, RIM_Y), (AX, RIM_Y))
        self.add_line("rim-r", (AX, RIM_Y), (right, RIM_Y))
        self.add_line("wall-r", (right, RIM_Y), (right, BOTTOM_Y))
        self.add_line("bottom", (right, BOTTOM_Y), (left, BOTTOM_Y))
        self.add_line("wall-l", (left, BOTTOM_Y), (left, RIM_Y))
        self.add_contour(
            "box", "rim-l", "rim-r", "wall-r", "bottom", "wall-l", closed=True,
        )
        # The box stands in for the chest: the neck gap is measured to its rim.
        self.mark_human_figure("person", head="head", torso="rim-r", torso_junction="start")

        for side, s, x in (("l", -1, left), ("r", 1, right)):
            # Arms hug the box: round shoulder from the rim corner, upper arm down,
            # forearm in to the hand under the box's bottom corner.
            out = x + s * SHOULDER_R
            self.add_arc(f"arm-{side}-shoulder", (x, RIM_Y), (out, RIM_Y + SHOULDER_R),
                         radius_x=SHOULDER_R, sweep=(s > 0))
            self.add_line(f"arm-{side}-upper", (out, RIM_Y + SHOULDER_R), (out, ELBOW_Y))
            self.add_line(f"arm-{side}-fore", (out, ELBOW_Y), (x, BOTTOM_Y))
            self.add_contour(f"arm-{side}", f"arm-{side}-shoulder", f"arm-{side}-upper", f"arm-{side}-fore")
            # Flap folded open, up and out from the same corner.
            self.add_line(f"flap-{side}", (x, RIM_Y), (x + s * FLAP, RIM_Y - FLAP // 2))
            self.relate("connect", f"arm-{side}", "box")
            self.relate("connect", f"flap-{side}", "box")
            self.relate("connect", f"flap-{side}", f"arm-{side}")
