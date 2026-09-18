"""Independent 32px profile of navigation-left-3a696d74.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3a696d74-81e0-470e-a351-1cb140f2bdc7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation left_3a696d74-81e0-470e-a351-1cb140f2bdc7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3a696d74-81e0-470e-a351-1cb140f2bdc7', 'pictographic-primitives/interface-essential/navigation left_3a696d74-81e0-470e-a351-1cb140f2bdc7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/navigation-left-3a696d74',)
SOLO_SOURCE_ICON_IDS = ('navigation-left-3a696d74',)
REFERENCE_EXPORT_SHA256 = '51a7c02b32d3e42a453c96a2be87fcf4e1acb3c7866cb14e3dde1d075a65fcb9'

class DrawingVariant3(Sub32):
    icon_id = 'navigation-left-3a696d74-sub32-v3'
    related_origin_icon_id = 'navigation-left-3a696d74-sub32-v2'
    variant_label = 'Redraw shape and structural proportions'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('head', (6, 4), (2, 16), (14, 20))
        self.add_bezier('shaft', (2, 16), ((14, 10), (30, 8), (30, 28)))
        self.relate('connect', 'head', 'shaft')
