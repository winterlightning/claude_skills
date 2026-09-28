"""Line Bar Chart. Keeps the source medium/tall/short height order and the baseline gap.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide chart-no-axes-column-increasing: an evenly spaced stroke series; supplied source sets its height order and detached baseline.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bb45fbb-182b-4dcd-92bf-ebd5c20fa96c'
SOURCE_PATH = 'pictographic-primitives/symbol/bar chart_3bb45fbb-182b-4dcd-92bf-ebd5c20fa96c.svg'
AUTHOR = 'gpt-6'


class BarChartLines(Solo48):
    icon_id = 'bar-chart-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('bar-chart', 'chart', 'statistics', 'graph', 'analytics', 'data', 'report', 'bars')

    def build(self) -> None:
        self.add_line('baseline', (6, 42), (42, 42))
        self.add_line('bar-0', (12, 18), (12, 34))
        self.add_line('bar-1', (24, 6), (24, 34))
        self.add_line('bar-2', (36, 26), (36, 34))
