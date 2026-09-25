"""Independent 32px profile of tooth.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9ec250e0-3b4c-4302-a78f-3f0f5baf59cb'
SOURCE_PATH = 'pictographic-primitives/health/tooth_9ec250e0-3b4c-4302-a78f-3f0f5baf59cb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9ec250e0-3b4c-4302-a78f-3f0f5baf59cb', 'pictographic-primitives/health/tooth_9ec250e0-3b4c-4302-a78f-3f0f5baf59cb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tooth',)
SOLO_SOURCE_ICON_IDS = ('tooth',)
REFERENCE_EXPORT_SHA256 = 'ea01b5c07e4e54bb0b379a4c92c6332cf3f82e8688152f3dc13479189a40fd81'

class Drawing(Sub32):
    icon_id = 'tooth-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    categories = ('health', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 4), ((19, 3), (20, 2), (22, 2)))
        self.add_bezier('p1-r1-2', (22, 2), ((26, 2), (27, 5), (27, 9)))
        self.add_bezier('p1-r1-3', (27, 9), ((27, 13), (24, 15), (24, 18)))
        self.add_bezier('p1-r1-4', (24, 18), ((24, 20), (24, 21), (24, 23)))
        self.add_bezier('p1-r1-5', (24, 23), ((24, 27), (24, 30), (22, 30)))
        self.add_bezier('p1-r1-6', (22, 30), ((18, 30), (20, 20), (16, 20)))
        self.add_bezier('p1-r1-7', (16, 20), ((12, 20), (14, 30), (10, 30)))
        self.add_bezier('p1-r1-8', (10, 30), ((8, 30), (8, 27), (8, 23)))
        self.add_bezier('p1-r1-9', (8, 23), ((8, 21), (8, 20), (8, 18)))
        self.add_bezier('p1-r1-10', (8, 18), ((8, 15), (5, 13), (5, 9)))
        self.add_bezier('p1-r1-11', (5, 9), ((5, 5), (6, 2), (10, 2)))
        self.add_bezier('p1-r1-12', (10, 2), ((12, 2), (13, 3), (16, 4)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
