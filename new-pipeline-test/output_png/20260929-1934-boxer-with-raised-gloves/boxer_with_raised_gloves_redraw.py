"""boxer with raised gloves (redraw of the new-pipeline traced SVG).

Plan: front-facing stick-figure boxer in guard on VRECT_L (centerline box
(8,4)-(40,44)), mirrored about the body axis x=24. Six strokes, as in the
generated image:
- head: two-half-arc circle, r5, centre (24,9); its top is the y=4 extreme.
- torso: vertical line from the neck (24,22) to the hip (24,32); the neck sits
  exactly 8 centerline units under the head outline (4-unit ink gap,
  human-reference.md), flagged with mark_human_figure.
- arms: one polyline glove -> elbow -> neck -> elbow -> glove; the upper arms
  drop from the neck to elbows at (10,28)/(38,28), the forearms rise straight
  up to the gloves.
- gloves: r2 circles centred (10,15)/(38,15); their outer sides are the
  x=8 and x=40 extremes. At stroke 4 an r2 ring paints as a solid 8-wide
  disc, so each glove reads as a bold fist with no hole.
  They sit beside the chin, 8.2 from the head outline on centerlines.
- legs: one inverted-V polyline from the hip to feet at (16,44)/(32,44).
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs). No useful Lucide match (Lucide has no
full-body figure); the 20260929-1929-boxer redraw set the stick-figure
vocabulary.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8 centerline.
- stroke-count (warn, 7): fixed; 6 strokes (head, torso, arms, legs, 2 gloves).
- keyshape-short-axis (warn, VRECT_M only 85% filled): fixed by choosing
  VRECT_L, whose 32-wide box the gloves reach exactly at x=8 and
  x=40; the head top is y=4 and the feet y=44. VRECT_M (28 wide) cannot hold
  two gloves beside a 10-wide head with 8-unit gaps.
- clearance e0 vs e1..e5 (head vs gloves, arms, torso, 2.7-3.2): fixed; the
  head is detached exactly 8 above the neck and the gloves are 8.2 from it.
- clearance e1/e3, e1/e4, e2/e4, e2/e5 (gloves vs arms/torso, 5.4-5.5):
  fixed; each glove joins only its own forearm end and is 14 from the torso.
- clearance e3/e4, e4/e5, e4/e6 (arms vs torso, legs vs torso, 7.5-7.7):
  fixed; arms and legs share the neck and hip endpoints with the torso
  (declared connections), elbows are 14 from the torso axis, and the hip is
  9.2 from the upper arms.
- hole (head interior 3.1 wide): fixed; the r5 head leaves a 6-wide opening.
- hole (glove interiors 1.8/2.0, arm-pit slivers 1.0/1.1): fixed; the gloves
  are solid discs with no hole, and the arms no longer cross the torso or the
  gloves, so no slivers are enclosed.
- no-head (warn): fixed; the head is an explicit circle flagged as the head.
Not kept: the glove thumb notches in the image. A hollow glove with a thumb
needs a >=10-wide centerline outline for its 6-unit opening, and two of those
beside the head need 46 units of width. A taller 2x3 ellipse glove was tried and came
back 7.75 from the head (mic error) with no visible gain; the solid disc keeps the "big fist"
read at 48 px.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7de26cb7-7475-4fc2-9562-2738e9bd49cd"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1934-boxer-with-raised-gloves/boxer-with-raised-gloves_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24            # body axis
HEAD_R = 5
HEAD_CY = 9        # centerline top at y=4
NECK = (AX, HEAD_CY + HEAD_R + 8)   # exact 8 head-to-torso centerline gap
HIP = (AX, 32)
ARM_DX = 14        # forearm axis; glove sides land on x=8 / x=40
ELBOW_Y = 28
GLOVE_R = 2
GLOVE_CY = 15
LEG_DX = 8
FOOT_Y = 44


class BoxerWithRaisedGlovesRedraw(Solo48):
    icon_id = "boxer-with-raised-gloves-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("boxing", "fighter", "boxing stance")
    keywords = ("boxer", "boxing", "gloves", "guard", "fight", "sport", "person")

    def _circle(self, name: str, cx: int, cy: int, r: int) -> None:
        # Two half arcs split at the sides.
        self.add_arc(f"{name}-top", (cx - r, cy), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-bottom", (cx + r, cy), (cx - r, cy), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-top", f"{name}-bottom", closed=True)

    def build(self) -> None:
        self._circle("head", AX, HEAD_CY, HEAD_R)

        self.add_line("torso", NECK, HIP)
        self.mark_human_figure("boxer", head="head", torso="torso", torso_junction="start")

        glove_bottom = GLOVE_CY + GLOVE_R
        self.add_polyline(
            "arms",
            (AX - ARM_DX, glove_bottom), (AX - ARM_DX, ELBOW_Y), NECK,
            (AX + ARM_DX, ELBOW_Y), (AX + ARM_DX, glove_bottom),
        )
        self.relate("connect", "arms", "torso")

        for side, sign in (("left", -1), ("right", 1)):
            name = f"{side}-glove"
            self._circle(name, AX + sign * ARM_DX, GLOVE_CY, GLOVE_R)
            self.relate("connect", name, "arms")

        self.add_polyline("legs", (AX - LEG_DX, FOOT_Y), HIP, (AX + LEG_DX, FOOT_Y))
        self.relate("connect", "legs", "torso")
