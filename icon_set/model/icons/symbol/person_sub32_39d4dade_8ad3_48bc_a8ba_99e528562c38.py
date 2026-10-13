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
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Person: head, arms curving out from the shoulders, body line.
        self.add_arc('head-1', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-2', (20, 6), (12, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_bezier('arm-l', (16, 18), ((12, 18), (8, 24), (4, 24)))
        self.add_bezier('arm-r', (16, 18), ((20, 18), (24, 24), (28, 24)))
        self.add_line('body', (16, 18), (16, 30))
        self.relate('connect', 'arm-l', 'body')
        self.relate('connect', 'arm-r', 'body')
        self.relate('connect', 'arm-l', 'arm-r')
