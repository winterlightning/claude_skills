"""Independent 32px profile of round-grape-bunch.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6eac0ad2-ae25-49cf-88fe-05d8f8b65add'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/sugar apple_6eac0ad2-ae25-49cf-88fe-05d8f8b65add.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6eac0ad2-ae25-49cf-88fe-05d8f8b65add', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/sugar apple_6eac0ad2-ae25-49cf-88fe-05d8f8b65add.svg'), ('2fc0acbf-1d1b-470d-a272-1cf68f822b5a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/grape_2fc0acbf-1d1b-470d-a272-1cf68f822b5a.svg'))
PROFILE_SOURCE_KEYS = ('solo/round-grape-bunch',)
SOLO_SOURCE_ICON_IDS = ('round-grape-bunch',)
REFERENCE_EXPORT_SHA256 = 'ec4575ba9774463f2b86929f13e7c96f978cb2fcfaa2d2ae1540e4d9e6c2e47f'

class Drawing(Sub32):
    icon_id = 'round-grape-bunch-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/food'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 13), (13, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (13, 13), (5, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (19, 13), (27, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (27, 13), (19, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (12, 26), (20, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (20, 26), (12, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 2), (16, 4))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
