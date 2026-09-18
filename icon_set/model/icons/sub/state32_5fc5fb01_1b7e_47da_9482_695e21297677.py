"""Independent 32px profile of state32-5fc5fb01-1b7e-47da-9482-695e21297677.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5fc5fb01-1b7e-47da-9482-695e21297677'
SOURCE_PATH = 'icon_set/assets/combination-state32/5fc5fb01-1b7e-47da-9482-695e21297677.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5fc5fb01-1b7e-47da-9482-695e21297677', 'icon_set/assets/combination-state32/5fc5fb01-1b7e-47da-9482-695e21297677.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'a2c7dcd893fb4c2faf0b94373a1b481ce13673afbe9d4d16cd826695ac13bf66'

class Drawing(Sub32):
    icon_id = 'state32-5fc5fb01-1b7e-47da-9482-695e21297677'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 12), (17, 12))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p1-r2-1', (14, 8), (14, 15))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_line('p2-r1-1', (17, 21), (22, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p3-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
