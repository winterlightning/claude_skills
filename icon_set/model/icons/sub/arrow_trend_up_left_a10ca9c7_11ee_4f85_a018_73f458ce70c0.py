"""Arrow Trend Up Left: An angular zigzag arrow descends from the upper right to a central valley, then rises toward an open upper-left arrowhead. Generate this component alone; exclude Circle Frame.

Construction: A descending and rising zigzag ends at an upper-left head.
Keyshape: HRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a10ca9c7-11ee-4f85-a018-73f458ce70c0'
SOURCE_PATH = 'pictographic-primitives/state/circle arrow_a10ca9c7-11ee-4f85-a018-73f458ce70c0.svg'
AUTHOR = 'gpt-6'


class ArrowTrendUpLeft(Sub32):
    icon_id = 'arrow-trend-up-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('arrow', 'trend', 'up', 'left', 'angular', 'zigzag', 'descends', 'upper')

    def build(self):
        self.add_polyline('shaft',(30,6),(16,26),(2,6))
        self.add_polyline('head',(2,18),(2,6),(14,6))
        self.relate('connect','shaft','head')
