# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of open-scissors.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5e86dec7-74d3-4fe6-ac76-2a480a4de26a'
SOURCE_PATH = 'pictographic-primitives/tools/scissors_5e86dec7-74d3-4fe6-ac76-2a480a4de26a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e86dec7-74d3-4fe6-ac76-2a480a4de26a', 'pictographic-primitives/tools/scissors_5e86dec7-74d3-4fe6-ac76-2a480a4de26a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/open-scissors',)
SOLO_SOURCE_ICON_IDS = ('open-scissors',)
REFERENCE_EXPORT_SHA256 = 'fb3b9dee71b9ea3e73d7bb8e8fff14bd73408fbe4bd42eb5bb47b8fe6dfa63aa'

class DrawingVariant2(Sub32):
    icon_id = 'open-scissors-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/tools'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (short_low, 26), ((short_low, 25), (6, 23), (8, 23)))
        self.add_bezier('p1-r1-2', (8, 23), ((10, 23), (12, 25), (12, 26)))
        self.add_bezier('p1-r1-3', (12, 26), ((12, 28), (10, 30), (8, 30)))
        self.add_bezier('p1-r1-4', (8, 30), ((6, 30), (short_low, 28), (short_low, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (20, 26), ((20, 25), (22, 23), (24, 23)))
        self.add_bezier('p2-r1-2', (24, 23), ((26, 23), (short_high, 25), (short_high, 26)))
        self.add_bezier('p2-r1-3', (short_high, 26), ((short_high, 28), (26, 30), (24, 30)))
        self.add_bezier('p2-r1-4', (24, 30), ((22, 30), (20, 28), (20, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (8, 23), (16, 15))
        self.add_bezier('p3-r1-2', (16, 15), ((19, 12), (21, 12), (22, 10)))
        self.add_bezier('p3-r1-3', (22, 10), ((23, 8), (24, 5), (24, 3)))
        self.add_bezier('p3-r1-4', (24, 3), ((24, 2), (24, 2), (24, 2)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (24, 23), (16, 15))
        self.add_bezier('p4-r1-2', (16, 15), ((13, 12), (11, 12), (10, 10)))
        self.add_bezier('p4-r1-3', (10, 10), ((9, 8), (8, 5), (8, 3)))
        self.add_bezier('p4-r1-4', (8, 3), ((8, 2), (8, 2), (8, 2)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
