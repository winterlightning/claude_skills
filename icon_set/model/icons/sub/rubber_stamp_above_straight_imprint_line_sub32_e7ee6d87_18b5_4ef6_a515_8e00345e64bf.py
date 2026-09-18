"""Independent 32px profile of rubber-stamp-above-straight-imprint-line.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e7ee6d87-18b5-4ef6-a515-8e00345e64bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/stamp_e7ee6d87-18b5-4ef6-a515-8e00345e64bf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e7ee6d87-18b5-4ef6-a515-8e00345e64bf', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/stamp_e7ee6d87-18b5-4ef6-a515-8e00345e64bf.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rubber-stamp-above-straight-imprint-line',)
SOLO_SOURCE_ICON_IDS = ('rubber-stamp-above-straight-imprint-line',)
REFERENCE_EXPORT_SHA256 = 'a154add09c811f63c87104e772c980c7d620f676cde61db262ff14b391d7a9c7'

class Drawing(Sub32):
    icon_id = 'rubber-stamp-above-straight-imprint-line-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 8), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 8), (19, 15), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (19, 15), (19, 18))
        self.add_line('p1-r1-4', (19, 18), (24, 18))
        self.add_arc('p1-r1-5', (24, 18), (27, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (27, 21), (27, 24))
        self.add_line('p1-r1-7', (27, 24), (5, 24))
        self.add_line('p1-r1-8', (5, 24), (5, 21))
        self.add_arc('p1-r1-9', (5, 21), (8, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (8, 18), (13, 18))
        self.add_line('p1-r1-11', (13, 18), (13, 15))
        self.add_arc('p1-r1-12', (13, 15), (10, 8), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (5, 30), (27, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
