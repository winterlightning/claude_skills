"""Independent 32px profile of handshake.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '533cf846-1648-4bd0-a7f9-03a05d166f40'
SOURCE_PATH = 'pictographic-primitives/symbol/handshake_533cf846-1648-4bd0-a7f9-03a05d166f40.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('533cf846-1648-4bd0-a7f9-03a05d166f40', 'pictographic-primitives/symbol/handshake_533cf846-1648-4bd0-a7f9-03a05d166f40.svg'),)
PROFILE_SOURCE_KEYS = ('solo/handshake',)
SOLO_SOURCE_ICON_IDS = ('handshake',)
REFERENCE_EXPORT_SHA256 = '077c4f9d384671bb3528d64eee4262f2fd44507b57afb4c65bedd634b7fc51c5'

class Drawing(Sub32):
    icon_id = 'handshake-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Handshake (original drawing, spaced to the 4-unit rule): clasped hands between two sleeve cuffs.
        # The cuff brackets draw the hands' sides; the inner finger line sits at x 18 and its curl moved right
        # so every gap keeps 4 units.
        self.add_polyline('cuff-l', (2, 8), (6, 8), (6, 22), (2, 22))
        self.add_polyline('cuff-r', (30, 8), (26, 8), (26, 22), (30, 22))
        self.add_polyline('hands-top', (6, 9), (10, 4), (20, 4), (26, 9))
        self.add_polyline('hands-bottom', (26, 20), (18, 24), (17, 28), (14, 28), (6, 20))
        self.add_line('finger-1', (20, 4), (16, 10))
        self.add_arc('finger-2', (16, 10), (18, 14), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('finger-3', (18, 14), (18, 24))
        self.add_contour('finger', 'finger-1', 'finger-2', 'finger-3', closed=False)
        for a, b in (('cuff-l', 'hands-top'), ('cuff-l', 'hands-bottom'), ('cuff-r', 'hands-top'), ('cuff-r', 'hands-bottom'),
                     ('hands-top', 'finger'), ('hands-bottom', 'finger')):
            self.relate('connect', a, b)
