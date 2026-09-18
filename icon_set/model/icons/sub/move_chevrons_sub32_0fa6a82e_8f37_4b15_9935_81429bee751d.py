"""Independent 32px profile of move-chevrons.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

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
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 7), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (21, 7))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (25, 11), (30, 16))
        self.add_line('p2-r1-2', (30, 16), (25, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (21, 25), (16, 30))
        self.add_line('p3-r1-2', (16, 30), (11, 25))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (7, 21), (2, 16))
        self.add_line('p4-r1-2', (2, 16), (7, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
