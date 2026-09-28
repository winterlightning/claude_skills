"""A clogged air filter: four wavy airflow lines; the middle two are stopped by a filter
band while the outer two flow past.

Symbol plan: four identical wavy lines, in phase, at x0 = 8, 19, 29, 40 (10-11 apart):
each is a smooth cubic run through knots at y = 6, 13, 20, 24, 28, 35, 42 swinging
0, +2, 0, -2, 0, +2, 0 about x0. The outer lines run the full height. The middle lines
stop at the filter band: its top edge (y=20) and bottom edge (y=28) join lines 2 and 3,
so the band is 10 wide and 8 tall, as in the reference.
Lucide construction: 'waves' - repeated smooth wave strokes; straight band edges.
Keyshape SQUARE: centerline x 6..42 (wave swings), y 6..42 (line ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ffa030ac-f9a1-4fc5-a89e-6b3daaedbf28"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__clogged-air-filter/20260926T044250Z-thuan-mac/reference/clogged air filter_ffa030ac-f9a1-4fc5-a89e-6b3daaedbf28.svg"
AUTHOR = "claude-opus-5-5"

YS = (6, 13, 20, 24, 28, 35, 42)
OFFSETS = (0, 2, 0, -2, 0, 2, 0)


class CloggedAirFilter(Solo48):
    icon_id = "clogged-air-filter"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "home/appliances"
    aliases = ("air-filter", "dirty-filter", "filter-clogged")
    keywords = ("filter", "air", "clogged", "dirty", "hvac", "airflow", "ventilation", "maintenance")

    def _wave(self, name, x0, broken=False):
        pts = [(x0 + o, y) for y, o in zip(YS, OFFSETS)]
        # knots at the swing extremes have vertical tangents; middle knots use the chord slope
        tang = []
        for i, p in enumerate(pts):
            a = pts[max(i - 1, 0)]
            b = pts[min(i + 1, len(pts) - 1)]
            tang.append(((b[0] - a[0]) / 2, (b[1] - a[1]) / 2))
        segs = []
        for i in range(1, len(pts)):
            p0, p1 = pts[i - 1], pts[i]
            t0, t1 = tang[i - 1], tang[i]
            segs.append(((round(p0[0] + t0[0] / 3, 3), round(p0[1] + t0[1] / 3, 3)),
                         (round(p1[0] - t1[0] / 3, 3), round(p1[1] - t1[1] / 3, 3)), p1))
        if broken:  # stop at the band edges (knots 2 and 4)
            self.add_bezier(f"{name}-upper", pts[0], *segs[:2])
            self.add_bezier(f"{name}-lower", pts[4], *segs[4:])
        else:
            self.add_bezier(name, pts[0], *segs)

    def build(self) -> None:
        xs = (8, 19, 29, 40)
        self._wave("air-1", xs[0])
        self._wave("air-2", xs[1], broken=True)
        self._wave("air-3", xs[2], broken=True)
        self._wave("air-4", xs[3])
        self.add_line("band-top", (xs[1], 20), (xs[2], 20))
        self.add_line("band-bottom", (xs[1], 28), (xs[2], 28))
        for edge, part in (("band-top", "upper"), ("band-bottom", "lower")):
            self.relate("connect", edge, f"air-2-{part}")
            self.relate("connect", edge, f"air-3-{part}")
