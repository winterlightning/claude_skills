"""Independent 32px profile of graduate-person.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0dc48bc0-54c9-4886-96f6-e51b9d1f618c'
SOURCE_PATH = 'pictographic-primitives/symbol/graduate_0dc48bc0-54c9-4886-96f6-e51b9d1f618c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0dc48bc0-54c9-4886-96f6-e51b9d1f618c', 'pictographic-primitives/symbol/graduate_0dc48bc0-54c9-4886-96f6-e51b9d1f618c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/graduate-person',)
SOLO_SOURCE_ICON_IDS = ('graduate-person',)
REFERENCE_EXPORT_SHA256 = '8d1fea01b8c18d2d3fe14f6b8546067d4bf88ae4270a9723e1c2645981901a39'

class Drawing(Sub32):
    icon_id = 'graduate-person-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 8), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (27, 8))
        self.add_line('p1-r1-3', (27, 8), (23, 10))
        self.add_line('p1-r1-4', (23, 10), (16, 13))
        self.add_line('p1-r1-5', (16, 13), (9, 10))
        self.add_line('p1-r1-6', (9, 10), (5, 8))
        self.add_line('p1-r1-7', (5, 8), (5, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_arc('p2-r1-1', (9, 10), (23, 10), radius_x=7, radius_y=9, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (5, 30), (27, 30), radius_x=11, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
