"""Circular Arrows: Two broad curved arrows follow opposite halves of a circular path. Their open arrowheads sit at upper right and lower left, with gaps separating the two arcs.

Construction: Two mirrored elliptical return arcs with opposite open arrowheads; rotational symmetry.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'dde1b901-7c31-4ac2-a73b-c30026b91f62'
SOURCE_PATH = 'pictographic-primitives/state/arrows spin_dde1b901-7c31-4ac2-a73b-c30026b91f62.svg'
AUTHOR = 'gpt-6'

class CircularArrowsContainerSymbol(Sub32):
    icon_id = 'circular-arrows-symbol'
    related_origin_icon_id = 'circular-arrows'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/circular-arrows'
    counterpart_icon_id = 'circular-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('circular', 'arrows', 'broad', 'curved', 'follow', 'opposite', 'halves', 'path')

    def build(self):
        self.add_arc('upper', (2, 10), (30, 10), radius_x=14, radius_y=8)
        self.add_polyline('head-upper', (22, 10), (30, 10), (30, 2))
        self.relate('connect', 'upper', 'head-upper')
        self.add_arc('lower', (30, 22), (2, 22), radius_x=14, radius_y=8)
        self.add_polyline('head-lower', (10, 22), (2, 22), (2, 30))
        self.relate('connect', 'lower', 'head-lower')
