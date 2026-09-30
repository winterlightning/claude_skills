"""bubbling-magic-cauldron (redraw of the new-pipeline traced SVG).

Subject: a witch's cauldron -- a round-bellied pot with a flat open rim that
overhangs the belly, two short splayed feet, and one round bubble rising
above the mouth.

Plan (mirrored about x=24): VRECT_M, centerline box (10,4)-(38,44).
Extremes: y=4 bubble top, y=44 foot tips, x=10 / x=38 rim lip tips.
- bubble: full circle r=4 about (24,8), split at its cardinal points.
- belly: one closed contour -- the mouth line y=21 from (12,21) to (36,21)
  plus an r=13 circle about (24,26). The rim and foot joints are 5-12-13
  lattice points of that circle, so every knot is an integer point:
  (12,21)/(36,21) on the mouth, (19,38)/(29,38) where the feet leave.
- lip: two 2-unit stubs (10,21)-(12,21) / (36,21)-(38,21) continuing the
  mouth line past the belly, so the rim reads wider than the pot's neck.
- feet: one mirrored definition, (19,38)->(16,44) splayed 1:2 outward,
  meeting the belly at ~86 degrees.
The bubble clears the mouth line by 9 (curve against straight; exactly 8
comes back `review`).
References: generated PNG read for the subject only (belly, overhanging
rim, two splayed feet, one bubble); Lucide `cooking-pot` for the flat mouth
line with a lip past the walls. No trace coordinates copied.

Keyshape: the metrics suggested SQUARE (score 0.98) but its own fit numbers
show the subject fills only 73% of the square's width (stretch 1.37 needed);
VRECT_M fills x 100% / y 96% (score 0.96). The cauldron is taller than wide
(aspect 0.73), so VRECT_M is the better fit and needs no stretching.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8+.
- keyshape-short-axis (SQUARE x fills 73%): fixed by switching to VRECT_M;
  x runs exactly 10..38 (lip tips), y exactly 4..44 (bubble top, feet).
- clearance e0/e1 (bubble vs rim, 2.73): fixed; 9 on centerlines.
- clearance e3/e4 (foot vs belly/rim loop, 2.72): fixed; each foot now
  shares its endpoint with the belly (declared connect), no near-miss.
- hole [23.9,9.9] (bubble, 3.79 inscribed): fixed; the bubble is r=4
  (8 across on centerlines; a full circle, not a sliver).
- hole [22.6,19.1] (the thin rim ellipse, 1.2 inscribed): fixed by drawing
  the rim as a single mouth line, so there is no rim loop at all.
Not kept as drawn: the rim ellipse (an elliptical rim needs 10+ of height
for its hole plus 8 to the bubble, which the 40-unit height cannot give).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "72f64d5e-456e-45c1-80a8-12d9cbe19516"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1939-bubbling-magic-cauldron/bubbling-magic-cauldron_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                      # mirror axis
BUBBLE_Y, BUBBLE_R = 8, 4    # bubble centre y / radius
RIM_Y = 21                   # mouth line
LIP = 10                     # left lip tip; right mirrors to 38
BELLY_Y, BELLY_R = 26, 13    # belly circle centre y / radius
MOUTH_DX = 12                # 5-12-13 point on the mouth: (24-/+12, 21)
FOOT_DX, FOOT_Y = 5, 38      # 5-12-13 point where each foot leaves the belly
TOE_DX, TOE_Y = 8, 44        # foot tip (16,44) / (32,44)


class BubblingMagicCauldronRedraw(Solo48):
    icon_id = "bubbling-magic-cauldron-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/fantasy"
    aliases = ("magic cauldron", "witch cauldron", "bubbling pot", "potion pot")
    keywords = ("cauldron", "witch", "magic", "potion", "brew", "halloween", "bubble", "pot")

    def build(self) -> None:
        ml, mr = AX - MOUTH_DX, AX + MOUTH_DX
        fl, fr = AX - FOOT_DX, AX + FOOT_DX
        r = BELLY_R

        # Bubble: full circle above the mouth.
        self.add_arc("bubble-top", (AX - BUBBLE_R, BUBBLE_Y), (AX + BUBBLE_R, BUBBLE_Y), radius_x=BUBBLE_R, sweep=True)
        self.add_arc("bubble-bottom", (AX + BUBBLE_R, BUBBLE_Y), (AX - BUBBLE_R, BUBBLE_Y), radius_x=BUBBLE_R, sweep=True)
        self.add_contour("bubble", "bubble-top", "bubble-bottom", closed=True)

        # Belly: mouth line + r13 circle split at the foot joints.
        self.add_line("mouth", (ml, RIM_Y), (mr, RIM_Y))
        self.add_arc("belly-r", (mr, RIM_Y), (fr, FOOT_Y), radius_x=r, sweep=True)
        self.add_arc("belly-bottom", (fr, FOOT_Y), (fl, FOOT_Y), radius_x=r, sweep=True)
        self.add_arc("belly-l", (fl, FOOT_Y), (ml, RIM_Y), radius_x=r, sweep=True)
        self.add_contour("belly", "mouth", "belly-r", "belly-bottom", "belly-l", closed=True)

        # Rim lip stubs and feet: one mirrored definition each.
        for side, sgn, mouth_x, foot_x in (("l", -1, ml, fl), ("r", 1, mr, fr)):
            self.add_line(f"lip-{side}", (mouth_x, RIM_Y), (AX + sgn * (AX - LIP), RIM_Y))
            self.relate("connect", f"lip-{side}", "mouth")
            self.relate("connect", f"lip-{side}", f"belly-{side}")
            self.add_line(f"foot-{side}", (foot_x, FOOT_Y), (AX + sgn * TOE_DX, TOE_Y))
            self.relate("connect", f"foot-{side}", f"belly-{side}")
            self.relate("connect", f"foot-{side}", "belly-bottom")
