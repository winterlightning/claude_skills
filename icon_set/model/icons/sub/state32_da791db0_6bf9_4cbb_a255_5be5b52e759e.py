"""Independent 32px profile of state32-da791db0-6bf9-4cbb-a255-5be5b52e759e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'da791db0-6bf9-4cbb-a255-5be5b52e759e'
SOURCE_PATH = 'icon_set/assets/combination-state32/da791db0-6bf9-4cbb-a255-5be5b52e759e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('da791db0-6bf9-4cbb-a255-5be5b52e759e', 'icon_set/assets/combination-state32/da791db0-6bf9-4cbb-a255-5be5b52e759e.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '50f1a0ef2e77537f6ac6340497c7b852a5346b4dfd59df88f975b5c263f236ea'

class Drawing(Sub32):
    icon_id = 'state32-da791db0-6bf9-4cbb-a255-5be5b52e759e'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 10), (16, 16))
        self.add_line('p1-r1-2', (16, 16), (21, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (16, 16), (16, 22))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_line('p1-r3-1', (12, 17), (20, 17))
        self.add_contour('path-1-3', 'p1-r3-1', closed=False)
        self.add_line('p1-r4-1', (12, 20), (20, 20))
        self.add_contour('path-1-4', 'p1-r4-1', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p1-r2-1')
        self.relate("connect", 'p1-r1-2', 'p1-r2-1')
