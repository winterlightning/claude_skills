"""airbnb-logo (redraw of the new-pipeline traced SVG).

Plan: the Airbnb Belo, a rounded arch whose two feet curl into lobes and
cross into a teardrop loop, on SQUARE (centerline box (6,6)-(42,42), ink
(4,4)-(44,44)). Everything is mirrored about x=24.
- arch: one closed contour. Crown node (24,6) with a level tangent; each
  half is an r6 crown cubic into a straight 60-degree leg (19,9)-(8,28), a
  short cubic that turns the leg vertical at the side extreme (6,35), an r7
  quarter round the lobe to its bottom (13,42), and a cubic that leaves the
  bottom level and reaches the cusp (24,34) heading 45 degrees inward.
- loop: one closed teardrop contour. Its tip is the arch cusp (24,34); the
  flanks leave it at 45 degrees (continuing the lobe strands, so the cusp
  reads as the logo's crossing) and turn vertical at (19,27)/(29,27) into an
  r5 bowl whose top is (24,22). The loop shares the cusp with the arch and
  is declared connected there.
Keyshape: the metrics suggested VRECT_L (32 wide). With a stroke of 4 the
bowl cannot be narrower than r5 (6 opening), and in a 32-wide box the legs
then pass under 8 from the bowl unless they stand almost vertical, which
turns the arch into a bell. SQUARE (scored 0.87, y already 100%) gives the
4 extra units of width; the bowl centre is 8.3 from each leg on centerlines.
Traced shape: airbnb-logo_raw.svg (read for the subject only; nothing
copied from its coordinates).
Lucide: no Airbnb mark (brand icons are not in Lucide); the droplet
construction (round bowl + two flanks to a tip) informs the loop.

Metric issues:
- clearance (e0/e1 0.31 apart, need 8): fixed. The trace's two parts meet
  at the crossing because the logo is one self-crossing stroke. The redraw
  makes that a real junction: the loop tip and the arch cusp are the same
  node (24,34), declared with relate("connect"); no other point of the loop
  comes within 8 of the arch.
- keyshape-short-axis (VRECT_L y fills 92%): fixed by moving to SQUARE;
  crown y=6, lobe bottoms y=42, lobe sides x=6 and x=42 are exact nodes.
- stroke-width (info): drawn at stroke 4; every gap budgeted for 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "768363e4-ebe3-4f7b-acb9-1268ec362ebd"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1810-airbnb-logo/airbnb-logo_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24            # mirror axis
CROWN = (AX, 6)    # top extreme
LEG_TOP = (19, 9)  # r6 crown meets the leg
LEG_FOOT = (8, 28)
SIDE = (6, 35)     # side extreme, vertical tangent
LOBE_BOTTOM = (13, 42)
CUSP = (AX, 34)    # lobes meet, loop tip
BOWL_Y = 27
BR = 5             # bowl radius: 6 opening at stroke 4

K_CROWN = 2.14     # 60-degree arc handle for r6
K_LOBE = 3.87      # quarter-circle handle for r7
D45 = 0.7071


def mirror(p):
    return (2 * AX - p[0], p[1])


class AirbnbLogoRedraw(Solo48):
    icon_id = "airbnb-logo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("belo", "airbnb-belo")
    keywords = ("airbnb", "belo", "logo", "brand", "travel", "rental",
                "lodging", "vacation")

    def build(self) -> None:
        lx, ly = LEG_FOOT[0] - LEG_TOP[0], LEG_FOOT[1] - LEG_TOP[1]
        n = (lx * lx + ly * ly) ** 0.5
        ux, uy = lx / n, ly / n  # leg direction, downward

        # Left half of the arch, walked from the cusp up to the crown.
        left = [
            ("lobe-l-inner", CUSP, (
                (CUSP[0] - 3.54, CUSP[1] + 3.54),
                (LOBE_BOTTOM[0] + 5, LOBE_BOTTOM[1]),
                LOBE_BOTTOM)),
            ("lobe-l-outer", LOBE_BOTTOM, (
                (LOBE_BOTTOM[0] - K_LOBE, LOBE_BOTTOM[1]),
                (SIDE[0], SIDE[1] + K_LOBE),
                SIDE)),
            ("heel-l", SIDE, (
                (SIDE[0], SIDE[1] - 2.5),
                (LEG_FOOT[0] + 2 * ux, LEG_FOOT[1] + 2 * uy),
                LEG_FOOT)),
        ]
        for name, start, seg in left:
            self.add_bezier(name, start, seg)
        self.add_line("leg-l", LEG_FOOT, LEG_TOP)
        self.add_bezier("crown-l", LEG_TOP, (
            (LEG_TOP[0] - K_CROWN * ux, LEG_TOP[1] - K_CROWN * uy),
            (CROWN[0] - K_CROWN, CROWN[1]),
            CROWN))
        # Right half: mirrored, walked back down to the cusp.
        self.add_bezier("crown-r", CROWN, (
            (CROWN[0] + K_CROWN, CROWN[1]),
            mirror((LEG_TOP[0] - K_CROWN * ux, LEG_TOP[1] - K_CROWN * uy)),
            mirror(LEG_TOP)))
        self.add_line("leg-r", mirror(LEG_TOP), mirror(LEG_FOOT))
        right = []
        for name, start, (c1, c2, end) in reversed(left):
            rname = name.replace("-l", "-r")
            self.add_bezier(rname, mirror(end), (mirror(c2), mirror(c1), mirror(start)))
            right.append(rname)
        self.add_contour(
            "arch",
            *[n for n, *_ in left], "leg-l", "crown-l",
            "crown-r", "leg-r", *right,
            closed=True,
        )

        # Teardrop loop: tip at the cusp, flanks at 45 degrees into the bowl.
        bowl_r, bowl_l = (AX + BR, BOWL_Y), (AX - BR, BOWL_Y)
        c1 = (CUSP[0] + 4 * D45, CUSP[1] - 4 * D45)
        c2 = (bowl_r[0], BOWL_Y + 3)
        self.add_bezier("flank-r", CUSP, (c1, c2, bowl_r))
        self.add_arc("bowl", bowl_r, bowl_l, radius_x=BR, sweep=False)
        self.add_bezier("flank-l", bowl_l, (mirror(c2), mirror(c1), CUSP))
        self.add_contour("loop", "flank-r", "bowl", "flank-l", closed=True)
        self.relate("connect", "loop", "arch")
