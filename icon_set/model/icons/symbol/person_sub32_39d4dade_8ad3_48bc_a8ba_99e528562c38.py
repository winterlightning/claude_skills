"""Independent 32px profile of person.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '39d4dade-8ad3-48bc-a8ba-99e528562c38'
SOURCE_PATH = 'pictographic-primitives/symbol/person_39d4dade-8ad3-48bc-a8ba-99e528562c38.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('39d4dade-8ad3-48bc-a8ba-99e528562c38', 'pictographic-primitives/symbol/person_39d4dade-8ad3-48bc-a8ba-99e528562c38.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person',)
SOLO_SOURCE_ICON_IDS = ('person',)
REFERENCE_EXPORT_SHA256 = 'b986509f4ef5b5b9af6f4f9241cc5294055d2dcfb215597c9c7bec06ae5091ce'

class Drawing(Sub32):
    icon_id = 'person-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (11, 7), (16, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (21, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (21, 7), (16, 12), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 12), (11, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (16, 17), ((12, 17), (8, 22), (5, 22)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (16, 17), ((20, 17), (24, 22), (27, 22)))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 17), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
