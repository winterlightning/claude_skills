"""Financial Candlestick Chart.
Plan: Three equally wide hollow candles rise in order; wicks share split body edges. Extrema (4,8)-(44,40).
Reference: Supplied original; no useful exact local Lucide match. Shared axes and simple geometric construction.
Reduction: Body heights normalized to keep three open candles; progressive placement retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '577dcc28-a365-530d-9225-9bdf27cfc52f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/crypto market price candle graph_577dcc28-a365-530d-9225-9bdf27cfc52f.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'three-rising-candlesticks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ()
    keywords = ('financial', 'candlestick', 'chart')

    def build(self):

        for i,(x,y) in enumerate(((8,24),(24,18),(40,12))):
            self.add_polyline(f'body-{i}',(x-4,y),(x,y),(x+4,y),(x+4,y+8),(x,y+8),(x-4,y+8),(x-4,y))
            self.add_line(f'wick-top-{i}',(x,y-4),(x,y))
            self.add_line(f'wick-low-{i}',(x,y+8),(x,40 if i==0 else y+14))
            for n in (f'wick-top-{i}',f'wick-low-{i}'):self.relate('connect',f'body-{i}',n)
        self.add_polyline('baseline',(4,40),(8,40),(44,40));self.relate('connect','baseline','wick-low-0')
