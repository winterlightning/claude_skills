"""A zigzag trend rises inside L-shaped axes. SQUARE extremes (6,6)-(42,42). Lucide chart-line informs coherent axes and a three-segment trend. Preserve the left-axis attachment and deliberate rising asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23d36377-ce26-44df-bfe2-869045f1333f'
SOURCE_PATH = 'pictographic-primitives/symbol/graph 1_23d36377-ce26-44df-bfe2-869045f1333f.svg'
AUTHOR = 'gpt-6'


class LineGraphAxes(Solo48):
    icon_id = 'line-graph-axes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('graph', 'line-chart', 'chart', 'statistics', 'analytics', 'growth', 'trend', 'data')

    def build(self) -> None:
        self.add_polyline('axes',(6,6),(6,32),(6,42),(42,42))
        self.add_polyline('trend',(6,32),(16,20),(27,29),(40,12))
        self.relate('connect','axes','trend')
