"""Independent 32px profile of state32-f587e9fa-2c98-4afb-8edc-fcfcb1437a91.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f587e9fa-2c98-4afb-8edc-fcfcb1437a91'
SOURCE_PATH = 'icon_set/assets/combination-state32/f587e9fa-2c98-4afb-8edc-fcfcb1437a91.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f587e9fa-2c98-4afb-8edc-fcfcb1437a91', 'icon_set/assets/combination-state32/f587e9fa-2c98-4afb-8edc-fcfcb1437a91.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '5c75023c4de3500f1cd0bdbac397de975a80e4fa52904644517a5cb5c558fd94'

class Drawing(Sub32):
    icon_id = 'state32-f587e9fa-2c98-4afb-8edc-fcfcb1437a91'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 12), (15, 16))
        self.add_line('p1-r1-2', (15, 16), (10, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (16, 12), (21, 16))
        self.add_line('p1-r2-2', (21, 16), (16, 20))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
