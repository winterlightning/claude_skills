"""Independent 32px profile of state32-7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2'
SOURCE_PATH = 'icon_set/assets/combination-state32/7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2', 'icon_set/assets/combination-state32/7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '185294ce9124a152d5e1bacc12fae8574dfc7ea30c44ebd0cff2ead3f4b2e0f5'

class Drawing(Sub32):
    icon_id = 'state32-7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (20, 11), (20, 21), radius_x=5, radius_y=6, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
