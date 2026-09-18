"""Independent 32px profile of left-pointing-hand-with-raised-thumb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ea54b202-0f96-50db-97dc-1884a36b2fb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hand pointer left_ea54b202-0f96-50db-97dc-1884a36b2fb9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ea54b202-0f96-50db-97dc-1884a36b2fb9', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hand pointer left_ea54b202-0f96-50db-97dc-1884a36b2fb9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/left-pointing-hand-with-raised-thumb',)
SOLO_SOURCE_ICON_IDS = ('left-pointing-hand-with-raised-thumb',)
REFERENCE_EXPORT_SHA256 = '450f361bcf4114b68574b09bd2db4032edd9d4e337422557a2efbd3b03f631bc'

class Drawing(Sub32):
    icon_id = 'left-pointing-hand-with-raised-thumb-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (17, 8), (8, 8))
        self.add_arc('p1-r1-2', (8, 8), (8, 13), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (8, 13), (16, 13))
        self.add_arc('p1-r1-4', (16, 13), (16, 19), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (16, 19), (17, 19))
        self.add_arc('p1-r1-6', (17, 19), (17, 24), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-7', (17, 24), (19, 24))
        self.add_arc('p1-r1-8', (19, 24), (19, 30), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-9', (19, 30), (22, 30))
        self.add_bezier('p1-r1-10', (22, 30), ((26, 30), (27, 26), (27, 20)))
        self.add_line('p1-r1-11', (27, 20), (27, 16))
        self.add_bezier('p1-r1-12', (27, 16), ((27, 10), (25, 7), (23, 5)))
        self.add_bezier('p1-r1-13', (23, 5), ((22, 3), (20, 2), (18, 2)))
        self.add_arc('p1-r1-14', (18, 2), (15, 6), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-15', (15, 6), ((15, 6), (16, 7), (17, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', closed=False)
