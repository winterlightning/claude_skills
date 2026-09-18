"""Independent 32px profile of menstrual-cup-c49f8cf3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c49f8cf3-366f-4dc7-9efb-40dc06f8b70c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/menstrual cup_c49f8cf3-366f-4dc7-9efb-40dc06f8b70c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c49f8cf3-366f-4dc7-9efb-40dc06f8b70c', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/menstrual cup_c49f8cf3-366f-4dc7-9efb-40dc06f8b70c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/menstrual-cup-c49f8cf3',)
SOLO_SOURCE_ICON_IDS = ('menstrual-cup-c49f8cf3',)
REFERENCE_EXPORT_SHA256 = '55424d86d9f1c23322099a7cc56667b45eb911bd6f3ac5d604311a8c5d5ea4f1'

class Drawing(Sub32):
    icon_id = 'menstrual-cup-c49f8cf3-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (27, 5), (24, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (24, 8), (8, 8))
        self.add_arc('p1-r1-5', (8, 8), (5, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (5, 5), (8, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 8), (8, 15))
        self.add_line('p2-r1-2', (8, 15), (8, 16))
        self.add_arc('p2-r1-3', (8, 16), (16, 24), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('p2-r1-4', (16, 24), (24, 16), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (24, 16), (24, 15))
        self.add_line('p2-r1-6', (24, 15), (24, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (16, 24), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-6')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-6')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-4', 'p3-r1-1')
