"""Independent 32px profile of hairpin-turn-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3fe88fdd-16b8-494f-b26e-461659c58008'
SOURCE_PATH = 'pictographic-primitives/transportation/hairpin turn right_3fe88fdd-16b8-494f-b26e-461659c58008.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3fe88fdd-16b8-494f-b26e-461659c58008', 'pictographic-primitives/transportation/hairpin turn right_3fe88fdd-16b8-494f-b26e-461659c58008.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hairpin-turn-right',)
SOLO_SOURCE_ICON_IDS = ('hairpin-turn-right',)
REFERENCE_EXPORT_SHA256 = '1857ef5f72b9e24b5cb1768d986c1d83331ef5fe8615435393320a80f666c8a9'

class DrawingVariant2(Sub32):
    icon_id = 'hairpin-turn-right-sub32-v2'
    related_origin_icon_id = 'hairpin-turn-right-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('head-left', (20, 19), (24, 23))
        self.add_line('head-right', (24, 23), (28, 19))
        self.add_contour('head', 'head-left', 'head-right', closed=False)
        self.add_line('shaft-right', (24, 23), (24, 12))
        self.add_arc('turn', (24, 12), (4, 12), radius_x=10, radius_y=10, sweep=False)
        self.add_line('shaft-left', (4, 12), (4, 30))
        self.add_contour('shaft', 'shaft-right', 'turn', 'shaft-left', closed=False)
        self.relate('connect', 'head-left', 'shaft-right')
        self.relate('connect', 'head-right', 'shaft-right')
