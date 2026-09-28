"""bunny-holding-easter-egg (redraw of the new-pipeline traced SVG).

Plan: VRECT_M (centerline box (10,4)-(38,44)), as suggested, mirrored about
x=24. The trace stacks ears, head, egg and two detached arms in 40 units; with
8-unit gaps that leaves an egg too short for its stripe. The bunny now peeks
from behind the egg, and its head sides wrap down onto the egg's shoulders.
Those two junctions stand in for the hugging arms.
- head: one open contour, after Lucide `rabbit`'s open U ear (legs + half-circle
  cap, open into the head). Flank from the egg shoulder (18,25), square to
  the shell, up to the outer ear leg x=10 (the x=10 extreme); ear cap r=4
  tops on y=4; inner leg x=18 down to y=14; crown arc r=12 across to x=30;
  mirrored ear (x=38 extreme). It ends on both egg shoulders (connect).
- egg: closed, in front. Apex (24,23), shoulder node (18,25), widest (14,34),
  base (24,44) (the y=44 extreme). Smooth tangents at every node.
- stripe: gentle S from widest node to widest node (point-symmetric halves),
  joined to the egg (connect).
Metric issues:
- stroke-width (trace 2.4 / fitted 2.65): redrawn at stroke 4.
- stroke-count (7 > 6): fixed, 3 strokes (head, egg, stripe).
- keyshape-short-axis (x filled 66%): fixed; ear legs on x=10/38, caps on
  y=4 and egg base on y=44 put all four VRECT_M extremes on the box.
- clearance e0-e4 (head/egg 1.03): fixed; the egg occludes the head and they
  meet at declared shoulder junctions instead of nearly touching.
- clearance e2-e3 (ears 2.68): fixed; the inner ear legs are 12 apart.
- clearance e1-e4 (egg/stripe 1.12): fixed; one egg contour, and the stripe
  joins it at the widest nodes. It keeps 8+ from the shell elsewhere.
- clearance e0/e1/e4 vs e5/e6 (arms 1.5-5.1): arms dropped (cannot fix as
  drawn). Detached arms need 8 on each side of the egg: 20 wide + 2x8 + arm
  width exceeds the 28-wide box. The head flanks hugging the egg carry "holding".
- holes: ear slits 1.0 wide: fixed, ears are open channels 8 wide into the
  head. Head 5.0: fixed, now 6.6 inscribed. Egg bands 3.8/4.2: fixed,
  6.9 above / 6.0 below the stripe (svg_metrics on the redraw reports no issues).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "606ec34e-20d1-525e-a765-4f3fca8d3c47"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1652-bunny-holding-easter-egg/bunny-holding-easter-egg_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
# Egg (in front): apex, shoulder node where the head meets it, widest point, base.
EGG_TOP, EGG_BOT = 23, 44
SHOULDER = (18, 25)
WIDE = (14, 34)
# Stripe S-wave handles (left half; the right half is the point reflection).
STRIPE_OUT, STRIPE_DIP = (18, 34), (20, 35.5)
# Ears: vertical U's, legs EAR_W apart, cap radius EAR_W / 2, tops on y=4.
EAR_OUT, EAR_W, EAR_CAP_Y = 10, 8, 8
NOTCH_Y = 14               # head top between the ears (arc ends)
CROWN_R = 12               # head-top arc radius
CHEEK_Y = 19               # outer ear leg turns into the head side here
# Head flank handles from the ear leg (vertical) to the egg shoulder (square to the shell).
CHEEK_C1, CHEEK_C2 = (EAR_OUT, 23), (15, 23.2)


def mx(p):
    return (2 * AXIS - p[0], p[1])


def flip(p):
    """Point reflection through the egg centre (AXIS, WIDE y): the S-wave's second half."""
    return (2 * AXIS - p[0], 2 * WIDE[1] - p[1])


class BunnyHoldingEasterEggRedraw(Solo48):
    icon_id = "bunny-holding-easter-egg-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ("easter bunny", "bunny with egg", "rabbit holding egg")
    keywords = ("easter", "bunny", "rabbit", "egg", "spring", "holiday", "hare")

    def build(self) -> None:
        top, base = (AXIS, EGG_TOP), (AXIS, EGG_BOT)
        # Egg outline: T -> shoulder -> widest -> base, mirrored.
        left = [
            ("dome", top, ((22.2, EGG_TOP), (19.8, 23.9), SHOULDER)),
            ("side", SHOULDER, ((16.2, 26.1), (WIDE[0], 29.5), WIDE)),
            ("base", WIDE, ((WIDE[0], 39.5), (18.5, EGG_BOT), base)),
        ]
        names = []
        for name, start, seg in left:
            self.add_bezier(f"egg-l-{name}", start, seg)
            names.append(f"egg-l-{name}")
        for name, start, seg in reversed(left):
            # reversed direction on the right half: end -> start
            c1, c2, end = seg
            self.add_bezier(f"egg-r-{name}", mx(end), (mx(c2), mx(c1), mx(start)))
            names.append(f"egg-r-{name}")
        self.add_contour("egg", *names, closed=True)

        # Stripe: gentle S from the left widest node to the right widest node.
        self.add_bezier("stripe", WIDE, (STRIPE_OUT, STRIPE_DIP, (AXIS, WIDE[1])),
                        (flip(STRIPE_DIP), flip(STRIPE_OUT), mx(WIDE)))
        self.relate("connect", "stripe", "egg")

        # Head + ears silhouette, hidden behind the egg below the shoulders.
        r = EAR_W // 2
        e_in = EAR_OUT + EAR_W
        self.add_bezier("head-l-side", SHOULDER,
                        (CHEEK_C2, CHEEK_C1, (EAR_OUT, CHEEK_Y)))
        self.add_line("ear-l-out", (EAR_OUT, CHEEK_Y), (EAR_OUT, EAR_CAP_Y))
        self.add_arc("ear-l-cap", (EAR_OUT, EAR_CAP_Y), (e_in, EAR_CAP_Y), radius_x=r, sweep=True)
        self.add_line("ear-l-in", (e_in, EAR_CAP_Y), (e_in, NOTCH_Y))
        self.add_arc("notch", (e_in, NOTCH_Y), mx((e_in, NOTCH_Y)), radius_x=CROWN_R, sweep=True)
        self.add_line("ear-r-in", mx((e_in, NOTCH_Y)), mx((e_in, EAR_CAP_Y)))
        self.add_arc("ear-r-cap", mx((e_in, EAR_CAP_Y)), mx((EAR_OUT, EAR_CAP_Y)), radius_x=r, sweep=True)
        self.add_line("ear-r-out", mx((EAR_OUT, EAR_CAP_Y)), mx((EAR_OUT, CHEEK_Y)))
        self.add_bezier("head-r-side", mx((EAR_OUT, CHEEK_Y)),
                        (mx(CHEEK_C1), mx(CHEEK_C2), mx(SHOULDER)))
        self.add_contour("head", "head-l-side", "ear-l-out", "ear-l-cap", "ear-l-in", "notch",
                         "ear-r-in", "ear-r-cap", "ear-r-out", "head-r-side")
        self.relate("connect", "head", "egg")
