"""A chromosome pair: a large X chromosome beside a small rod-shaped chromosome.

Symbol plan: the large chromosome is one closed X silhouette -- two chromatids crossing
at the centromere, drawn as four rounded arms mirrored about the centromere's vertical
and horizontal axes. Each arm is three cubics with integer knots: side notch -> outer
extreme (vertical tangent) -> arm end (horizontal tangent) -> top/bottom notch, so every
keyshape extreme lands on a knot and the sharp V notches are single joins. The small
chromosome is a rounded rod (r5 ends) with a band marking its centromere, bottom-aligned
with the large one, as the source's smaller chromosome sits low beside it.
Lucide construction: no chromosome glyph; the rod follows Lucide 'pill'/'capsule' r-end
construction, the X arms follow the rounded-lobe cubic construction of 'clover'.
Keyshape HRECT_L: centerline x 4..44 (X arms, rod side), y 8..40 (X arm ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f4c642c9-6ad8-4f73-b9c5-8eaa2f4bc29e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__chromosome-pair/20260925T093141Z-thuan-mac/reference/laboratory chromosome_f4c642c9-6ad8-4f73-b9c5-8eaa2f4bc29e.svg"
AUTHOR = "claude-opus-5-5"


class ChromosomePair(Solo48):
    icon_id = "chromosome-pair"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science/laboratory"
    aliases = ("laboratory-chromosome", "chromosomes", "x-chromosome", "xy-chromosomes")
    keywords = ("chromosome", "chromosomes", "dna", "gene", "genetics", "biology",
                "laboratory", "science", "xy")

    def build(self) -> None:
        # large X: centromere (14,24); notches 3 / 6 from it; outer extremes (+-10, +-9); arm ends (+-6, +-16)
        cx, cy = 14, 24
        notch_side, notch_end = 3, 6
        ex, ey, tx, ty = 10, 9, 6, 16
        ho, ht, k = 5, 2.5, 2
        segs = []
        for sx, sy, tag in ((-1, -1, "ul"), (1, -1, "ur"), (1, 1, "lr"), (-1, 1, "ll")):
            side = (cx + sx * notch_side, cy)
            end = (cx, cy + sy * notch_end)
            e = (cx + sx * ex, cy + sy * ey)
            t = (cx + sx * tx, cy + sy * ty)
            run = [("side", side, (side[0] + sx * k, side[1] + sy * k * 1.2), (e[0], e[1] - sy * ho), e),
                   ("round", e, (e[0], e[1] + sy * ho), (t[0] + sx * ht, t[1]), t),
                   ("inner", t, (t[0] - sx * ht, t[1]), (end[0] + sx * k * 0.6, end[1] + sy * k), end)]
            if tag in ("ur", "ll"):  # walk these arms the other way round the closed outline
                run = [(n, b, c2, c1, a) for n, a, c1, c2, b in reversed(run)]
            for n, a, c1, c2, b in run:
                self.add_bezier(f"x-{tag}-{n}", a, (c1, c2, b))
                segs.append(f"x-{tag}-{n}")
        self.add_contour("x-chromosome", *segs, closed=True)

        # small chromosome: a rod x 32..44 with rounded ends, pinched to a waist at its
        # centromere (y30) -- one short and one long arm, as a Y chromosome is drawn
        self.add_arc("rod-top", (32, 24), (44, 24), radius_x=6, sweep=True)
        self.add_bezier("rod-right-upper", (44, 24), ((44, 27), (43, 28), (43, 30)))
        self.add_bezier("rod-right-lower", (43, 30), ((43, 32), (44, 33), (44, 35)))
        self.add_arc("rod-bottom", (44, 35), (32, 35), radius_x=6, radius_y=5, sweep=True)
        self.add_bezier("rod-left-lower", (32, 35), ((32, 33), (33, 32), (33, 30)))
        self.add_bezier("rod-left-upper", (33, 30), ((33, 28), (32, 27), (32, 24)))
        self.add_contour("rod", "rod-top", "rod-right-upper", "rod-right-lower", "rod-bottom",
                         "rod-left-lower", "rod-left-upper", closed=True)
