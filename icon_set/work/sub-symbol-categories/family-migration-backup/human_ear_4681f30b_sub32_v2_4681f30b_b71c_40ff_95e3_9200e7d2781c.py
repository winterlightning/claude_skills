# Variant of human-ear-4681f30b-sub32; parent file remains unchanged.
"""Independent 32px profile of human-ear-4681f30b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4681f30b-b71c-40ff-95e3-9200e7d2781c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/hearing aid ear_4681f30b-b71c-40ff-95e3-9200e7d2781c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4681f30b-b71c-40ff-95e3-9200e7d2781c', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/hearing aid ear_4681f30b-b71c-40ff-95e3-9200e7d2781c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/human-ear-4681f30b',)
SOLO_SOURCE_ICON_IDS = ('human-ear-4681f30b',)
REFERENCE_EXPORT_SHA256 = '0b484902231c95560af1b4957cf08763534d351ffc88ba6c46b4de222a1ec188'

class DrawingVariant2(Sub32):
    icon_id = 'human-ear-4681f30b-sub32-v2'
    variant_of = 'human-ear-4681f30b-sub32'
    variant_label = 'Smooth ear lobe and inner fold tangents'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (6, 12), (26, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-2', (26,12), ((26,18),(23,21),(20,23)))
        self.add_bezier('p1-r1-3', (20,23), ((17,25),(18,30),(13,30)))
        self.add_arc('p1-r1-4', (13, 30), (6, 23), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (13,10), (17,14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (17, 14), (13, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
