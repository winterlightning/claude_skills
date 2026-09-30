"""couple-standing-with-hair (redraw of the new-pipeline traced SVG).

Plan: two frontal stick figures standing side by side on SQUARE
(centerline box (6,6)-(42,42)), mirrored about x 24, holding hands.
- man (axis x 14): short hair drawn as the head outline itself, the
  avatar "short-hair roof" construction: a flat top y 6 with r3 corners,
  short temples x 9 / 19, and a round r5 jaw about (14,11), bottom y 16.
- woman (axis x 34): a round r5 head about (34,11), top y 6, and long hair
  as two r10 strands that leave the head sides (29,11) / (39,11) with the
  head's vertical tangent and flick outward to (27,17) / (41,17).
- each body: torso x 14 / 34 from y 24 (exactly 8 below the head bottom,
  4 visible) to the hip y 34; legs from the hip to feet 5 either side on
  y 42.
- arms from the shoulder (torso top): the outer hands reach the box edge
  at (6,30) / (42,30); the inner arms meet at (24,30), the couple holding
  hands on the shared axis.
Lucide: `users` (two figures side by side) informed the pairing; its
busts are not stick figures, so only the layout was taken.
Human reference: icon_set/references/human_ref/full_body_ref.png (circle
heads, straight round-ended limbs); the short-hair roof follows the solo
avatar `man-with-short-hair-and-open-shoulders`.

Metric issues (couple-standing-with-hair_metrics.json) and how they were
handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- stroke-count (13 strokes, budget 6): reduced to 10 paths (per figure one
  head, torso, arm run and leg V, plus the woman's two hair strands). Not
  fully fixed: two full stick figures need at least 8 paths, so the budget
  of 6 cannot hold both people.
- keyshape-short-axis (SQUARE x fill 86%): fixed on the model, the outer
  hands reach x 6 and 42, the man's roof and the woman's head top y 6 and
  the feet y 42, so every SQUARE extreme is exact.
- clearance e0/e3, e1/e4, e2/e4 (floating hair 2-3 from the heads): the
  hair is no longer a detached arc. A detached hair arc 8 clear of an r5
  head needs a radius of 13 (26 wide) and 8 more height, which the square
  cannot hold for two figures, so the hair is part of each head: the man's
  flat roof and the woman's attached strands.
- clearance e3/e5, e3/e7, e3/e8, e4/e10, e4/e11, e4/e12 (heads 2.5-2.7
  above the shoulders): each head bottom is exactly 8 on centerlines above
  its torso top (4 visible), flagged with mark_human_figure.
- clearance e5/e6, e5/e7, e5/e8, e6/e7, e6/e8 and the matching right-figure
  pairs (arms and legs 5-7 from the torso): the torso and legs are now
  shared-endpoint joins, and each outer hand is 8 from its torso and about
  9 from its leg; the legs open 10 at the feet.
- clearance between the two figures' inner hands: resolved by joining the
  hands at (24,30) (connect), which also reads as a couple.
- holes 2.83 / 2.97 (heads): the heads are r5 (6 inscribed); the man's
  roof head is 10x10 inside, the woman's r5 circle 6 inscribed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8808cfa8-f297-4bd3-a099-3c4ba3f2b025"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1037-couple-standing-with-hair/couple-standing-with-hair_raw.svg"
AUTHOR = "claude-opus-5-5"

HAND_JOIN = (24, 30)       # shared axis of the pair: the held hands
HEAD_R = 5
HEAD_CY = 11               # heads span y 6..16
SHOULDER_Y = HEAD_CY + HEAD_R + 8   # 24: exactly 8 below the head outline
HIP_Y = 34
FOOT_Y = 42
FOOT_DX = 5                # feet 10 apart
HAND_Y = 30
OUTER_REACH = 8            # outer hand 8 out from the torso (x 6 / 42)
MAN_X, WOMAN_X = 14, 34    # mirrored about x 24
ROOF_R = 3                 # man's short-hair corners
STRAND_R = 10              # woman's hair flick radius
STRAND_END = (8, 6)        # strand end offset from its arc centre (3-4-5 x2)


class CoupleStandingWithHairRedraw(Solo48):
    icon_id = "couple-standing-with-hair-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/couple"
    aliases = ("couple", "man and woman", "two people", "pair holding hands")
    keywords = ("couple", "people", "man", "woman", "hair", "standing", "holding hands", "partners")

    def _body(self, name: str, x: int, outer: int) -> None:
        """Torso, arm run (outer hand -> shoulder -> held hand) and leg V."""
        self.add_line(f"{name}-torso", (x, SHOULDER_Y), (x, HIP_Y))
        self.add_polyline(
            f"{name}-arms",
            (x + outer * OUTER_REACH, HAND_Y), (x, SHOULDER_Y), HAND_JOIN,
        )
        self.add_polyline(
            f"{name}-legs",
            (x - FOOT_DX, FOOT_Y), (x, HIP_Y), (x + FOOT_DX, FOOT_Y),
        )
        self.relate("connect", f"{name}-torso", f"{name}-arms")
        self.relate("connect", f"{name}-torso", f"{name}-legs")

    def build(self) -> None:
        r, cy, k = HEAD_R, HEAD_CY, ROOF_R
        top = cy - r

        # Man: short-hair roof over a round jaw.
        x = MAN_X
        self.add_line("man-roof", (x - r + k, top), (x + r - k, top))
        self.add_arc("man-roof-r", (x + r - k, top), (x + r, top + k), radius_x=k)
        self.add_line("man-temple-r", (x + r, top + k), (x + r, cy))
        self.add_arc("man-jaw", (x + r, cy), (x - r, cy), radius_x=r)
        self.add_line("man-temple-l", (x - r, cy), (x - r, top + k))
        self.add_arc("man-roof-l", (x - r, top + k), (x - r + k, top), radius_x=k)
        self.add_contour(
            "man-head", "man-roof", "man-roof-r", "man-temple-r",
            "man-jaw", "man-temple-l", "man-roof-l", closed=True,
        )
        self._body("man", x, -1)
        self.mark_human_figure("man", head="man-head", torso="man-torso", torso_junction="start")

        # Woman: round head with two outward-flicking hair strands.
        x = WOMAN_X
        self.add_arc("woman-head-t", (x - r, cy), (x + r, cy), radius_x=r)
        self.add_arc("woman-head-b", (x + r, cy), (x - r, cy), radius_x=r)
        self.add_contour("woman-head", "woman-head-t", "woman-head-b", closed=True)
        dx, dy = STRAND_END
        left_c = x - r - STRAND_R
        right_c = x + r + STRAND_R
        self.add_arc("woman-hair-l", (x - r, cy), (left_c + dx, cy + dy), radius_x=STRAND_R)
        self.add_arc("woman-hair-r", (x + r, cy), (right_c - dx, cy + dy), radius_x=STRAND_R, sweep=False)
        self.relate("connect", "woman-head", "woman-hair-l")
        self.relate("connect", "woman-head", "woman-hair-r")
        self._body("woman", x, 1)
        self.mark_human_figure("woman", head="woman-head", torso="woman-torso", torso_junction="start")

        # The couple holds hands at the shared axis.
        self.relate("connect", "man-arms", "woman-arms")
