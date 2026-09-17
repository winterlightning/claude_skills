"""Counterclockwise History: Two curved arrows form an open circular clock surround, with heads at the left and right. Inside, joined clock hands point upward and right from a shared corner.

Construction: Two counterclockwise return arcs surround joined clock hands; arrows share each arc endpoint.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ab913828-297d-4c94-ab76-5b92952287d3'
SOURCE_PATH = 'pictographic-primitives/state/watch hands_ab913828-297d-4c94-ab76-5b92952287d3.svg'
AUTHOR = 'gpt-6'


class CounterclockwiseHistory(Sub32):
    icon_id = 'counterclockwise-history'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('clockwise', 'history', 'curved', 'arrows', 'form', 'open', 'circular', 'clock')

    def build(self):
        self.add_arc("top",(30,10),(2,10),radius_x=14,radius_y=8,sweep=False)
        self.add_polyline("head-top",(2,2),(2,10),(8,10))
        self.relate("connect","top","head-top")
        self.add_arc("bottom",(2,22),(30,22),radius_x=14,radius_y=8,sweep=False)
        self.add_polyline("head-bottom",(24,22),(30,22),(30,30))
        self.relate("connect","bottom","head-bottom")
        self.add_polyline("hands",(16,10),(16,16),(20,16))
