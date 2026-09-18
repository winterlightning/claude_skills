"""Independent 32px profile of sailboat-curved-sail.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '74c318d1-397c-4a33-9a8b-1a68e1da926e'
SOURCE_PATH = 'pictographic-primitives/outdoors/sailing boat_74c318d1-397c-4a33-9a8b-1a68e1da926e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('74c318d1-397c-4a33-9a8b-1a68e1da926e', 'pictographic-primitives/outdoors/sailing boat_74c318d1-397c-4a33-9a8b-1a68e1da926e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sailboat-curved-sail',)
SOLO_SOURCE_ICON_IDS = ('sailboat-curved-sail',)
REFERENCE_EXPORT_SHA256 = 'ef21ccc08440acedb406ac347a55be43499739654adca5802dfb771d324d067b'

class Drawing(Sub32):
    icon_id = 'sailboat-curved-sail-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'outdoors'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (8, 2), (25, 17), radius_x=17, radius_y=15, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (25, 17), (8, 17))
        self.add_line('p1-r1-3', (8, 17), (8, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 24), (30, 24))
        self.add_line('p2-r1-2', (30, 24), (24, 30))
        self.add_line('p2-r1-3', (24, 30), (8, 30))
        self.add_line('p2-r1-4', (8, 30), (2, 24))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
