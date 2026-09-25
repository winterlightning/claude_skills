"""microsoft powerpoint logo: standalone repair of supplied reference.

Plan: P badge left of pie chart. Keyshape HRECT_L.
Reduction: Used squared badge and capital P counter; chart is narrower than reference to preserve legal openings.
Construction references: local Lucide originals and atomic-debug: chart-pie.

All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "1a770dd1-2225-4204-b85f-81e18d91cca2"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/microsoft powerpoint logo_1a770dd1-2225-4204-b85f-81e18d91cca2.svg"
AUTHOR = "gpt-6"


class PresentationPieChartBadge(Solo48):
    icon_id = 'presentation-pie-chart-badge'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("powerpoint logo", "presentation badge")
    keywords = ("pie", "chart", "letter p", "slides")

    def build(self) -> None:
        self.add_arc("chart-upper-left", (28, 20), (36, 12), radius_x=8, radius_y=8, sweep=True)
        self.add_arc("chart-upper-right", (36, 12), (44, 24), radius_x=8, radius_y=12, sweep=True)
        self.add_arc("chart-lower-right", (44, 24), (36, 36), radius_x=8, radius_y=12, sweep=True)
        self.add_arc("chart-lower-left", (36, 36), (28, 28), radius_x=8, radius_y=8, sweep=True)
        self.add_contour("pie-outline", "chart-upper-left", "chart-upper-right", "chart-lower-right", "chart-lower-left")
        self.add_line("pie-vertical", (36, 12), (36, 24))
        self.add_line("pie-horizontal", (36, 24), (44, 24))
        self.relate("connect", "pie-vertical", "pie-horizontal")
        self.relate("connect", "pie-vertical", "chart-upper-left")
        self.relate("connect", "pie-vertical", "chart-upper-right")
        self.relate("connect", "pie-horizontal", "chart-upper-right")
        self.relate("connect", "pie-horizontal", "chart-lower-right")

        self.add_polyline("letter-badge", (4,8),(28,8),(28,20),(28,28),(28,40),(4,40),closed=True)
        self.relate("connect", "chart-upper-left", "letter-badge")
        self.relate("connect", "chart-lower-left", "letter-badge")
        self.add_polyline("p-bowl", (12,17),(20,17),(20,25),(12,25),closed=True)
        self.add_line("p-stem", (12,25),(12,31))
        self.relate("connect", "p-stem", "p-bowl")
