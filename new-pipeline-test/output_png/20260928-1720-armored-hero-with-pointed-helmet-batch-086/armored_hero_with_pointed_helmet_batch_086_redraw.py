"""armored-hero-with-pointed-helmet (redraw of the new-pipeline traced SVG).

Plan: upright stick figure on VRECT_M (centerline box (10,4)-(38,44)), built
on the shared axis x=24 and mirrored left/right.
- helmeted head: one closed contour. The pointed helmet is a 45-degree roof
  from the peak (24,4) (the y=4 extreme) down to (18,10)/(30,10), then straight
  cheek guards to y=12 that run tangent into the r6 chin arc about (24,12).
  The helmet is worn, not floating: a floating helmet costs another 8-unit gap
  that the 40-unit height cannot pay. Interior inscribed radius 6 (ink hole 8).
- brim: short level flanges (14,12)-(18,12) and (30,12)-(34,12) at the rim
  where helmet meets face, sharing the contour's rim nodes, so the head reads
  as armour rather than a bare pointed head.
- torso: neck stub from (24,26), exactly 8 centerline units under the chin
  (4-unit ink gap, human-reference.md), shoulder node at (24,27), waist down
  to the hip at (24,36).
- arms: straight from the shoulder, angled outward and down to (10,33) and
  (38,33), the x=10 / x=38 extremes. The shoulder sits 9 above the hip so the
  arm-to-leg wedge keeps 8.27 on centerlines.
- legs: an inverted V from the hip to (16,44) and (32,44), the y=44 extreme.
Reference: icon_set/references/human_ref (round head, 4-unit head gap,
single-stroke round-ended limbs); the original source (megaman zero bust)
for a helmet worn on the head with the face below it. No useful Lucide
match; Lucide `person-standing` informed the straight-limb construction.

Keyshape: VRECT_M as suggested; arms reach both x extremes, helmet peak the
top, both feet the bottom.

Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap budgeted at 8 centerline.
- stroke-count (7 vs 6): the trace's separate helmet (e0 crest, e1 brow, e2
  shell) and head circle (e3) merged into one helmeted-head contour; the
  crest line and V brow were dropped (they sat 2-6 units from the shell).
- keyshape-short-axis: arm tips now reach x=10 and x=38 (x fills 100%).
- clearance e0/e1, e1/e3, e2/e3: helmet and head are one contour, so there
  is no inner crest/brow and no helmet-to-head gap to crowd.
- clearance e3/e4, e3/e6 (head to torso/arms): torso starts exactly 8 below
  the chin; the arms branch 1 lower at the shoulder node and diverge.
- clearance e4/e5 and the remaining arm/leg clearances: the hip moved 9 below
  the shoulder, giving 8.27 between each arm and leg.
- t-junction e5/e4, e6/e4: arms and legs share exact shoulder / hip nodes
  with the split torso, declared with relate("connect").
- human head gap: exactly 8 centerline, marked with mark_human_figure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ed5c437b-f1b7-5deb-8e7e-d0d95f2f6077"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1720-armored-hero-with-pointed-helmet-batch-086/"
    "armored-hero-with-pointed-helmet-batch-086_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24               # body axis
PEAK = (AX, 4)
HALF = 6              # half head width = chin radius
EAVE_Y = 10           # roof meets cheek guard (45-degree roof)
RIM_Y = 12            # cheek guard meets chin arc; also chin centre
BRIM = 4              # flange length outward from each cheek guard
NECK = (AX, RIM_Y + HALF + 8)
SHOULDER = (AX, NECK[1] + 1)
HIP = (AX, 36)
HAND_DX, HAND_Y = 14, 33
FOOT_DX, FOOT_Y = 8, 44
BRIM_ON = True


class ArmoredHeroWithPointedHelmetRedraw(Solo48):
    icon_id = "armored-hero-with-pointed-helmet-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ("armored hero", "knight", "helmeted warrior", "game hero")
    keywords = ("hero", "armor", "helmet", "knight", "warrior", "character", "game", "person")

    def build(self) -> None:
        l, r = AX - HALF, AX + HALF
        self.add_line("roof-r", PEAK, (r, EAVE_Y))
        self.add_line("guard-r", (r, EAVE_Y), (r, RIM_Y))
        self.add_arc("chin-r", (r, RIM_Y), (AX, RIM_Y + HALF), radius_x=HALF, sweep=True)
        self.add_arc("chin-l", (AX, RIM_Y + HALF), (l, RIM_Y), radius_x=HALF, sweep=True)
        self.add_line("guard-l", (l, RIM_Y), (l, EAVE_Y))
        self.add_line("roof-l", (l, EAVE_Y), PEAK)
        self.add_contour(
            "head", "roof-r", "guard-r", "chin-r", "chin-l", "guard-l", "roof-l", closed=True,
        )
        if BRIM_ON:
            self.add_line("brim-l", (l - BRIM, RIM_Y), (l, RIM_Y))
            self.add_line("brim-r", (r, RIM_Y), (r + BRIM, RIM_Y))
            self.relate("connect", "brim-l", "head")
            self.relate("connect", "brim-r", "head")

        self.add_line("torso", NECK, SHOULDER)
        self.add_line("waist", SHOULDER, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("hero", head="head", torso="torso", torso_junction="start")

        arms = {"arm-l": -1, "arm-r": 1}
        for name, side in arms.items():
            self.add_line(name, SHOULDER, (AX + side * HAND_DX, HAND_Y))
            self.relate("connect", name, "torso")
            self.relate("connect", name, "waist")
        self.relate("connect", "arm-l", "arm-r")

        legs = {"leg-l": -1, "leg-r": 1}
        for name, side in legs.items():
            self.add_line(name, HIP, (AX + side * FOOT_DX, FOOT_Y))
            self.relate("connect", name, "waist")
        self.relate("connect", "leg-l", "leg-r")
