"""A bust stands in front of the lower-left corner of a rectangular chart board. A curved hairline crosses the head, while the board shows three rising vertical bars joined by an upward curve.
Lucide chart-no-axes-combined and user construction. Presenter overlaps an open board corner. Three bars reduced to two with a rising connection; hairline and chest mark omitted.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd08e15ae-76b0-44d7-adad-5e061e50f2d8'
SOURCE_PATH = 'pictographic-primitives/work/workflow coaching chart_d08e15ae-76b0-44d7-adad-5e061e50f2d8.svg'
AUTHOR = 'gpt-6'


class PersonBesideRisingChart(Solo48):
    icon_id = 'person-beside-rising-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('person', 'chart', 'coaching', 'presentation', 'growth', 'board')

    def build(self) -> None:
        self.add_polyline('board', (16, 13), (16, 6), (42, 6), (42, 32), (26, 32), closed=False)
        self.add_arc('head-top', (10, 26), (18, 26), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (18, 26), (10, 26), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulder-left', (6, 42), (14, 39), radius_x=8, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('shoulder-right', (14, 39), (22, 42), radius_x=8, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('bust', 'shoulder-left', 'shoulder-right', closed=False)
        self.add_line('bar-left', (26, 23), (26, 20))
        self.add_line('rise', (26, 20), (34, 14))
        self.add_line('bar-right', (34, 14), (34, 23))
        self.add_contour('chart', 'bar-left', 'rise', 'bar-right', closed=False)
