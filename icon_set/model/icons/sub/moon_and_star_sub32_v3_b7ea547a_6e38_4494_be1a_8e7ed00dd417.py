# Variant of moon-and-star-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of moon-and-star.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b7ea547a-6e38-4494-be1a-8e7ed00dd417'
SOURCE_PATH = 'pictographic-primitives/symbol/moon and star_b7ea547a-6e38-4494-be1a-8e7ed00dd417.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b7ea547a-6e38-4494-be1a-8e7ed00dd417', 'pictographic-primitives/symbol/moon and star_b7ea547a-6e38-4494-be1a-8e7ed00dd417.svg'),)
PROFILE_SOURCE_KEYS = ('solo/moon-and-star',)
SOLO_SOURCE_ICON_IDS = ('moon-and-star',)
REFERENCE_EXPORT_SHA256 = '43adbe4b281e6a9120867a13ea55b0aeb19d9eca4f1f209cdd75c834741f7c06'

class DrawingVariant3(Sub32):
    icon_id = 'moon-and-star-sub32-v3'
    variant_of = 'moon-and-star-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Give the crescent a fuller outer curve while retaining the separate five-point star.
        self.add_bezier('moon-upper',(14,4),((7,4),(2,9),(2,16)))
        self.add_bezier('moon-lower',(2,16),((2,23),(7,28),(14,28)))
        self.add_bezier('inner-lower',(14,28),((6,22),(6,10),(14,4)))
        self.add_contour('crescent','moon-upper','moon-lower','inner-lower',closed=True)
        self.add_polyline('star',(24,8),(27,13),(30,13),(27,17),(28,23),(24,20),(20,23),(21,17),(18,13),(21,13),closed=True)
