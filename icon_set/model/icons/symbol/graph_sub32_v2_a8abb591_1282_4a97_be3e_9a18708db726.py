"""Independent 32px profile of graph.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a8abb591-1282-4a97-be3e-9a18708db726'
SOURCE_PATH = 'pictographic-primitives/arrows/graph_a8abb591-1282-4a97-be3e-9a18708db726.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a8abb591-1282-4a97-be3e-9a18708db726', 'pictographic-primitives/arrows/graph_a8abb591-1282-4a97-be3e-9a18708db726.svg'),)
PROFILE_SOURCE_KEYS = ('solo/graph',)
SOLO_SOURCE_ICON_IDS = ('graph',)
REFERENCE_EXPORT_SHA256 = '2d11a302432b15321d1b87775c61466d1c0076bdfebd72a93cca0392c5198a3b'

class DrawingVariant2(Sub32):
    icon_id = 'graph-sub32-v2'
    related_origin_icon_id = 'graph-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (24, short_low), (30, short_low))
        self.add_line('p1-r1-2', (30, short_low), (17, 21))
        self.add_line('p1-r1-3', (17, 21), (12, 15))
        self.add_line('p1-r1-4', (12, 15), (2, short_high))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (30, short_low), (30, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
