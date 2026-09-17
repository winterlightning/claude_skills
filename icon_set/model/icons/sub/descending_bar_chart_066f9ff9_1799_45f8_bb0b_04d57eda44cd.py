"""Descending Bar Chart: Three upright bars descend in height from left to right and meet a shared horizontal baseline projecting past the outer bars. Generate this component alone; exclude Speech Bubble.

Construction: Three descending vertical bars join one baseline, using a regular horizontal step.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '066f9ff9-1799-45f8-bb0b-04d57eda44cd'
SOURCE_PATH = 'pictographic-primitives/state/message bars_066f9ff9-1799-45f8-bb0b-04d57eda44cd.svg'
AUTHOR = 'gpt-6'


class DescendingBarChart(Sub32):
    icon_id = 'descending-bar-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('descending', 'bar', 'chart', 'upright', 'bars', 'descend', 'height', 'left')

    def build(self):
        self.add_polyline("base",(2,30),(6,30),(16,30),(26,30),(30,30))
        for i,top in enumerate((2,10,18)):
            x=6+10*i
            self.add_line(f"bar-{i}",(x,top),(x,30))
            self.relate("connect","base",f"bar-{i}")
