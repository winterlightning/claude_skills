"""Ascending Bar Chart: Three vertical bars rise from a shared horizontal baseline, increasing in height from left to right. Generate this component alone; exclude Circle Frame.

Construction: Three regularly spaced bars increase in height across a shared baseline.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4'
SOURCE_PATH = 'pictographic-primitives/state/circle bar_e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4.svg'
AUTHOR = 'gpt-6'


class AscendingBarChart(Sub32):
    icon_id = 'ascending-bar-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('ascending', 'bar', 'chart', 'vertical', 'bars', 'rise', 'shared', 'horizontal')

    def build(self):
        self.add_line('base',(2,30),(30,30))
        for i,top in enumerate((18,10,2)):
            x=6+10*i
            self.add_line(f'bar-{i}',(x,top),(x,30))
            self.relate('connect','base',f'bar-{i}')
