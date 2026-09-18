"""Independent 32px profile of state32-01ec16aa-50ee-4ece-addd-2a4b27425d93.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '01ec16aa-50ee-4ece-addd-2a4b27425d93'
SOURCE_PATH = 'icon_set/assets/combination-state32/01ec16aa-50ee-4ece-addd-2a4b27425d93.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('01ec16aa-50ee-4ece-addd-2a4b27425d93', 'icon_set/assets/combination-state32/01ec16aa-50ee-4ece-addd-2a4b27425d93.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'f1156e229d2021461974c0173d7d4b85d8bed8a04e55c56398421855fce641c3'

class Drawing(Sub32):
    icon_id = 'state32-01ec16aa-50ee-4ece-addd-2a4b27425d93'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 22), (22, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (11, 11), (11, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 22), (22, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p4-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
