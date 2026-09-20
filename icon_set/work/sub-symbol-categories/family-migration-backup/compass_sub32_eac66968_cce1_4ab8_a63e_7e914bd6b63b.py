"""Independent 32px profile of compass.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'eac66968-cce1-4ab8-a63e-7e914bd6b63b'
SOURCE_PATH = 'pictographic-primitives/navigation/compass_eac66968-cce1-4ab8-a63e-7e914bd6b63b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eac66968-cce1-4ab8-a63e-7e914bd6b63b', 'pictographic-primitives/navigation/compass_eac66968-cce1-4ab8-a63e-7e914bd6b63b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/compass',)
SOLO_SOURCE_ICON_IDS = ('compass',)
REFERENCE_EXPORT_SHA256 = 'b5fe8f38908c5ad005deb7e82bf7754a543ca96593c2c5683e629e6ea2c46cfb'

class Drawing(Sub32):
    icon_id = 'compass-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'navigation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (21, 21), (22, 20))
        self.add_line('p1-r1-2', (22, 20), (30, 2))
        self.add_line('p1-r1-3', (30, 2), (11, 11))
        self.add_line('p1-r1-4', (11, 11), (21, 21))
        self.add_line('p1-r1-5', (21, 21), (2, 30))
        self.add_line('p1-r1-6', (2, 30), (11, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
