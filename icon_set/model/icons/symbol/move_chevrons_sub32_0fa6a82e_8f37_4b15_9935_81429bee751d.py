"""Independent 32px profile of move-chevrons.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0fa6a82e-8f37-4b15-9935-81429bee751d'
SOURCE_PATH = 'pictographic-primitives/symbol/move arrows_0fa6a82e-8f37-4b15-9935-81429bee751d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0fa6a82e-8f37-4b15-9935-81429bee751d', 'pictographic-primitives/symbol/move arrows_0fa6a82e-8f37-4b15-9935-81429bee751d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/move-chevrons',)
SOLO_SOURCE_ICON_IDS = ('move-chevrons',)
REFERENCE_EXPORT_SHA256 = 'afdf5591c10734a083af3034dee61b00dcaada398cf5291e5dbc3f9ba133ce72'

class Drawing(Sub32):
    icon_id = 'move-chevrons-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Move: four chevrons pointing out from the centre.
        self.add_polyline('up', (12, 6), (16, 2), (20, 6))
        self.add_polyline('right', (26, 12), (30, 16), (26, 20))
        self.add_polyline('down', (20, 26), (16, 30), (12, 26))
        self.add_polyline('left', (6, 20), (2, 16), (6, 12))
