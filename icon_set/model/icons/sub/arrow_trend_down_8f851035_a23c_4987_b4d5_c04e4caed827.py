"""Arrow Trend Down: A zigzag line descends overall from upper left to lower right, finishing in an open arrowhead after a central rise. Generate this component alone; exclude Circle Frame.

Construction: A continuous zigzag falls overall to an open lower-right head.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8f851035-a23c-4987-b4d5-c04e4caed827'
SOURCE_PATH = 'pictographic-primitives/state/circle downtrend arrow_8f851035-a23c-4987-b4d5-c04e4caed827.svg'
AUTHOR = 'gpt-6'


class ArrowTrendDown(Sub32):
    icon_id = 'arrow-trend-down'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'trend', 'down', 'zigzag', 'line', 'descends', 'overall', 'upper')

    def build(self):
        self.add_polyline('shaft',(2,4),(12,18),(20,10),(30,28))
        self.add_polyline('head',(18,28),(30,28),(30,16))
        self.relate('connect','shaft','head')
