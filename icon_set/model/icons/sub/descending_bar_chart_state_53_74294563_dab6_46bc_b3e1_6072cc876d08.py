"""Descending Bar Chart: Three upright bars share a horizontal baseline and decrease in height from left to right. Generate this component alone; exclude Circle Frame.

Construction: Three regularly spaced descending bars attach to the source baseline.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '74294563-dab6-46bc-b3e1-6072cc876d08'
SOURCE_PATH = 'pictographic-primitives/state/circle bars_74294563-dab6-46bc-b3e1-6072cc876d08.svg'
AUTHOR = 'gpt-6'


class DescendingBarChartState53(Sub32):
    icon_id = 'descending-bar-chart-state-53'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('descending', 'bar', 'chart', 'upright', 'bars', 'share', 'horizontal', 'baseline')

    def build(self):
        self.add_polyline("base",(2,30),(6,30),(16,30),(26,30),(30,30))
        for i,top in enumerate((2,10,18)):
            x=6+10*i
            self.add_line(f"bar-{i}",(x,top),(x,30))
            self.relate("connect","base",f"bar-{i}")
