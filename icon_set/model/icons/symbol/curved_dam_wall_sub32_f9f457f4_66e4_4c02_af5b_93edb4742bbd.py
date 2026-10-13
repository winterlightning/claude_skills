"""Independent 32px profile of curved-dam-wall.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f9f457f4-66e4-4c02-af5b-93edb4742bbd'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/water dam_f9f457f4-66e4-4c02-af5b-93edb4742bbd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f9f457f4-66e4-4c02-af5b-93edb4742bbd', 'pictographic-primitives/landmarks/batch-07/water dam_f9f457f4-66e4-4c02-af5b-93edb4742bbd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/curved-dam-wall',)
SOLO_SOURCE_ICON_IDS = ('curved-dam-wall',)
REFERENCE_EXPORT_SHA256 = 'b0d2c5113c2684845fd8988039f0b1df801f9d95192d4fbc3e53ac3f9610117d'

class Drawing(Sub32):
    icon_id = 'curved-dam-wall-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 23), (2, 5))
        self.add_line('p1-r1-2', (2, 5), (9, 5))
        self.add_line('p1-r1-3', (9, 5), (9, 10))
        self.add_line('p1-r1-4', (9, 10), (23, 10))
        self.add_line('p1-r1-5', (23, 10), (23, 5))
        self.add_line('p1-r1-6', (23, 5), (30, 5))
        self.add_line('p1-r1-7', (30, 5), (30, 23))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_arc('p2-r1-1', (30, 23), (20, 23), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (20, 23), (12, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (12, 23), (2, 23), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
