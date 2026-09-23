"""A letter P badge overlays a pie chart with an upper-right quadrant.

Symbol plan: the pie outline is occluded at the badge's right wall;
orthogonal chart radii share its center. The badge contains an upright P.
Lucide chart-pie informed the quadrant construction. The left overlap is
deliberately asymmetric, as in the reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1a770dd1-2225-4204-b85f-81e18d91cca2"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/microsoft powerpoint logo_1a770dd1-2225-4204-b85f-81e18d91cca2.svg"
AUTHOR = "gpt-6"


class PresentationPieChartBadge(Solo48):
    icon_id = "presentation-pie-chart-badge"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/logos"
    aliases = ("powerpoint logo", "presentation badge")
    keywords = ("pie", "chart", "letter p", "slides")

    def build(self) -> None:
        self.add_arc("chart-upper-left", (25, 20), (34, 14), radius_x=9, radius_y=6, sweep=True)
        self.add_arc("chart-upper-right", (34, 14), (44, 24), radius_x=10, sweep=True)
        self.add_arc("chart-lower-right", (44, 24), (34, 34), radius_x=10, sweep=True)
        self.add_arc("chart-lower-left", (34, 34), (25, 28), radius_x=9, radius_y=6, sweep=True)
        self.add_contour("pie-outline", "chart-upper-left", "chart-upper-right", "chart-lower-right", "chart-lower-left")
        self.add_line("pie-vertical", (34, 14), (34, 24))
        self.add_line("pie-horizontal", (34, 24), (44, 24))
        self.relate("connect", "pie-vertical", "pie-horizontal")
        self.relate("connect", "pie-vertical", "chart-upper-left")
        self.relate("connect", "pie-vertical", "chart-upper-right")
        self.relate("connect", "pie-horizontal", "chart-upper-right")
        self.relate("connect", "pie-horizontal", "chart-lower-right")

        r = 4
        self.add_line("badge-top", (8, 8), (21, 8))
        self.add_arc("badge-ne", (21, 8), (25, 12), radius_x=r, sweep=True)
        self.add_line("badge-right-upper", (25, 12), (25, 20))
        self.add_line("badge-right-middle", (25, 20), (25, 28))
        self.add_line("badge-right-lower", (25, 28), (25, 36))
        self.add_arc("badge-se", (25, 36), (21, 40), radius_x=r, sweep=True)
        self.add_line("badge-bottom", (21, 40), (8, 40))
        self.add_arc("badge-sw", (8, 40), (4, 36), radius_x=r, sweep=True)
        self.add_line("badge-left", (4, 36), (4, 12))
        self.add_arc("badge-nw", (4, 12), (8, 8), radius_x=r, sweep=True)
        self.add_contour("letter-badge", "badge-top", "badge-ne", "badge-right-upper", "badge-right-middle", "badge-right-lower", "badge-se", "badge-bottom", "badge-sw", "badge-left", "badge-nw", closed=True)
        self.relate("connect", "chart-upper-left", "badge-right-upper")
        self.relate("connect", "chart-upper-left", "badge-right-middle")
        self.relate("connect", "chart-lower-left", "badge-right-middle")
        self.relate("connect", "chart-lower-left", "badge-right-lower")

        self.add_line("p-stem", (13, 17), (13, 31))
        self.add_arc("p-bowl-upper", (13, 17), (16, 21), radius_x=3, radius_y=4, sweep=True)
        self.add_arc("p-bowl-lower", (16, 21), (13, 25), radius_x=3, radius_y=4, sweep=True)
        self.add_contour("p-bowl", "p-bowl-upper", "p-bowl-lower")
        self.relate("connect", "p-stem", "p-bowl-upper")
        self.relate("connect", "p-stem", "p-bowl-lower")
