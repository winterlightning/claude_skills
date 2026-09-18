"""Independent 32px profile of peso-money.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bfac5a0c-eae9-420e-af5e-4ac03cb24f16'
SOURCE_PATH = 'pictographic-primitives/money/peso_bfac5a0c-eae9-420e-af5e-4ac03cb24f16.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bfac5a0c-eae9-420e-af5e-4ac03cb24f16', 'pictographic-primitives/money/peso_bfac5a0c-eae9-420e-af5e-4ac03cb24f16.svg'),)
PROFILE_SOURCE_KEYS = ('solo/peso-money',)
SOLO_SOURCE_ICON_IDS = ('peso-money',)
REFERENCE_EXPORT_SHA256 = 'c1b100f1ed6be998a6c85ac0a93bfe4e4dc3d2a2c78fe01509b7b9f0def3386c'

class Drawing(Sub32):
    icon_id = 'peso-money-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 30), (8, 2))
        self.add_line('p1-r1-2', (8, 2), (23, 2))
        self.add_arc('p1-r1-3', (23, 2), (23, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (23, 16), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
