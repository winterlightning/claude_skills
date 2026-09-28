# Variant of flash-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of flash.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '482239ce-8075-436a-b065-ac0bc289a949'
SOURCE_PATH = 'pictographic-primitives/interface-essential/flash_482239ce-8075-436a-b065-ac0bc289a949.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('482239ce-8075-436a-b065-ac0bc289a949', 'pictographic-primitives/interface-essential/flash_482239ce-8075-436a-b065-ac0bc289a949.svg'), ('821a0fbf-70fd-4f18-bc5d-1a46c93ca7e9', 'pictographic-primitives/interface-essential/flash_821a0fbf-70fd-4f18-bc5d-1a46c93ca7e9.svg'), ('83a0452b-f452-49a0-a7c6-99e9bc8331a8', 'pictographic-primitives/interface-essential/flash_83a0452b-f452-49a0-a7c6-99e9bc8331a8.svg'))
PROFILE_SOURCE_KEYS = ('solo/flash', 'solo/flash-821a0fbf', 'solo/flash-83a0452b')
SOLO_SOURCE_ICON_IDS = ('flash', 'flash-821a0fbf', 'flash-83a0452b')
REFERENCE_EXPORT_SHA256 = 'ea3e7b7b798dd7be8870c146de47f6297d153e6469ef42e66ee3b8e98defc5b0'

class DrawingVariant3(Sub32):
    icon_id = 'flash-sub32-v3'
    variant_of = 'flash-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Lightning bolt with a taller silhouette and coherent horizontal shoulders.
        self.add_polyline('bolt',(15,2),(26,2),(17,13),(26,13),(9,30),(15,19),(6,19),closed=True)
