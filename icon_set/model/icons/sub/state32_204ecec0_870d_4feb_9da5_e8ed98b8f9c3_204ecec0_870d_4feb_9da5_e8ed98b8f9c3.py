"""Independent 32px profile of state32-204ecec0-870d-4feb-9da5-e8ed98b8f9c3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '204ecec0-870d-4feb-9da5-e8ed98b8f9c3'
SOURCE_PATH = 'pictographic-primitives/state/circle equal_204ecec0-870d-4feb-9da5-e8ed98b8f9c3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('204ecec0-870d-4feb-9da5-e8ed98b8f9c3', 'pictographic-primitives/state/circle equal_204ecec0-870d-4feb-9da5-e8ed98b8f9c3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-equal',)
SOLO_SOURCE_ICON_IDS = ('circle-equal',)
REFERENCE_EXPORT_SHA256 = '917d6a6978003524e3c088523c09b23119e1083b3f0b97fbefcfb21cc7fa840b'

class Drawing(Sub32):
    icon_id = 'state32-204ecec0-870d-4feb-9da5-e8ed98b8f9c3'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 12), (23, 12))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (9, 20), (23, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p3-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
