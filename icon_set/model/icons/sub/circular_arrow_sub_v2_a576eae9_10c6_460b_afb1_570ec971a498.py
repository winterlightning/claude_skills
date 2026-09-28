# Variant of circular-arrow-sub; parent file remains unchanged.
"""Circular Arrow: A long curved arrow follows most of a clockwise circle and ends at the upper right. Its head has horizontal and vertical arms, and a gap separates the tip from the tail.

Construction: Three equal-radius quadrants form a continuous clockwise sweep; the head shares its terminal point. The lower-right opening preserves clear separation.
Keyshape: SQUARE; centerline extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'pictographic-primitives/state/circular arrow_a576eae9-10c6-460b-afb1-570ec971a498.svg'
AUTHOR = 'gpt-6'

class CircularArrowSubVariant2(Sub32):
    icon_id = 'circular-arrow-sub-v2'
    variant_of = 'circular-arrow-sub'
    variant_label = 'Round continuous sweep'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('circular', 'arrow', 'long', 'curved', 'follows', 'most', 'clockwise', 'circle')

    def build(self):
        cx, cy, radius = 16, 16, 14
        tip = (cx + radius, cy)
        self.add_arc('lower-left', (cx, cy + radius), (cx - radius, cy), radius_x=radius)
        self.add_arc('upper-left', (cx - radius, cy), (cx, cy - radius), radius_x=radius)
        self.add_arc('upper-right', (cx, cy - radius), tip, radius_x=radius)
        self.add_contour('sweep', 'lower-left', 'upper-left', 'upper-right')
        self.add_polyline('head', (22, cy), tip, (30, 8))
        self.relate('connect', 'sweep', 'head')
