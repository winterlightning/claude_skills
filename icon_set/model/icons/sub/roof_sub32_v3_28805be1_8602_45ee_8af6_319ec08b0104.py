# Variant of roof-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of roof.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '28805be1-8602-45ee-8af6-319ec08b0104'
SOURCE_PATH = 'pictographic-primitives/state/roof_28805be1-8602-45ee-8af6-319ec08b0104.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('28805be1-8602-45ee-8af6-319ec08b0104', 'pictographic-primitives/state/roof_28805be1-8602-45ee-8af6-319ec08b0104.svg'), ('bc91dbd1-f3e2-55f8-8e78-7f10a6feba69', 'pictographic-primitives/arrows/arrow button top 1_bc91dbd1-f3e2-55f8-8e78-7f10a6feba69.svg'))
PROFILE_SOURCE_KEYS = ('solo/roof', 'solo/chevron-up-with-wide-arms')
SOLO_SOURCE_ICON_IDS = ('roof', 'chevron-up-with-wide-arms')
REFERENCE_EXPORT_SHA256 = '455bcfb74f37bf819404d9856d5b042f5518ef75989f65b5a4a1bf2659f2c628'

class DrawingVariant3(Sub32):
    icon_id = 'roof-sub32-v3'
    variant_of = 'roof-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Shallow roof pitch with equal straight slopes; restore a roof rather than a tall caret.
        self.add_polyline('roof',(2,22),(16,10),(30,22))
