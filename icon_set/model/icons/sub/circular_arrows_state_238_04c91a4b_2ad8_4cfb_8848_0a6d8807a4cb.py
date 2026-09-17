"""Circular Arrows: Two broad curved arrows trace opposite halves of a circle with gaps between their ends. The upper arc points down-right and the lower arc points up-left, forming a clockwise cycle.

Construction: Two circular return arcs have opposed heads and two gaps; the arrowheads remain larger than the smaller circular sweep.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '04c91a4b-2ad8-4cfb-8848-0a6d8807a4cb'
SOURCE_PATH = 'pictographic-primitives/state/recycling_04c91a4b-2ad8-4cfb-8848-0a6d8807a4cb.svg'
AUTHOR = 'gpt-6'


class CircularArrowsState238(Sub32):
    icon_id = 'circular-arrows-state-238'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('circular', 'arrows', 'broad', 'curved', 'trace', 'opposite', 'halves', 'circle')

    def build(self):
        self.add_arc('upper',(4,11),(28,11),radius_x=13)
        self.add_arc('lower',(28,21),(4,21),radius_x=13)
        self.add_polyline('upper-head',(20,12),(28,11),(30,2))
        self.add_polyline('lower-head',(12,20),(4,21),(2,30))
        self.relate('connect','upper','upper-head')
        self.relate('connect','lower','lower-head')
