"""Rising Bar Graph. Retains three hollow bars; removes the tiny baseline overhangs to allocate 8-unit bar widths and gaps.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Supplied bar graph: three hollow bars, shared baseline and increasing height.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9eac7172-d6a3-4992-aaad-dd1cdbd21c70'
SOURCE_PATH = 'pictographic-primitives/symbol/bar graph_9eac7172-d6a3-4992-aaad-dd1cdbd21c70.svg'
AUTHOR = 'gpt-6'


class BarGraphRising(Solo48):
    icon_id = 'bar-graph-rising'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('bar-graph', 'growth', 'chart', 'statistics', 'increase', 'analytics', 'signal', 'bars')

    def build(self) -> None:
        self.add_polyline('baseline', (4, 40), (12, 40), (20, 40), (28, 40), (36, 40), (44, 40))
        self.add_polyline('bar-0', (4, 40), (4, 28), (12, 28), (12, 40))
        self.relate("connect", 'baseline', 'bar-0')
        self.add_polyline('bar-1', (20, 40), (20, 18), (28, 18), (28, 40))
        self.relate("connect", 'baseline', 'bar-1')
        self.add_polyline('bar-2', (36, 40), (36, 8), (44, 8), (44, 40))
        self.relate("connect", 'baseline', 'bar-2')
