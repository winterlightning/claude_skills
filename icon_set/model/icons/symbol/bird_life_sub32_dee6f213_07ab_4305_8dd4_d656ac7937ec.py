"""Independent 32px profile of bird-life.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'dee6f213-07ab-4305-8dd4-d656ac7937ec'
SOURCE_PATH = 'pictographic-primitives/transportation/bird life_dee6f213-07ab-4305-8dd4-d656ac7937ec.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dee6f213-07ab-4305-8dd4-d656ac7937ec', 'pictographic-primitives/transportation/bird life_dee6f213-07ab-4305-8dd4-d656ac7937ec.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bird-life',)
SOLO_SOURCE_ICON_IDS = ('bird-life',)
REFERENCE_EXPORT_SHA256 = 'c1c995fff76156cca4c41dd2dd6e09a0bad72312d0b9df43e5ec8cfdbee0077f'

class Drawing(Sub32):
    icon_id = 'bird-life-sub32'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 13), (10, 13))
        self.add_arc('p1-r1-2', (10, 13), (16, 19), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (16, 19), (22, 13), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (22, 13), (30, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
