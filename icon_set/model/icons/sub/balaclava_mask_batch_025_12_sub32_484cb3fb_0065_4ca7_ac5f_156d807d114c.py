"""Independent 32px profile of balaclava-mask-batch-025-12.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '484cb3fb-0065-4ca7-ac5f-156d807d114c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('484cb3fb-0065-4ca7-ac5f-156d807d114c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/balaclava-mask-batch-025-12',)
SOLO_SOURCE_ICON_IDS = ('balaclava-mask-batch-025-12',)
REFERENCE_EXPORT_SHA256 = 'c4e86c80d7111839b06cbdba703750f8525d496d58afabdac997f2e29302f882'

class Drawing(Sub32):
    icon_id = 'balaclava-mask-batch-025-12-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (9, 23), ((6, 20), (5, 17), (5, 13)))
        self.add_arc('p1-r1-2', (5, 13), (16, 2), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 2), (27, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-4', (27, 13), ((27, 17), (27, 20), (23, 23)))
        self.add_line('p1-r1-5', (23, 23), (26, 29))
        self.add_bezier('p1-r1-6', (26, 29), ((23, 30), (20, 30), (16, 30)))
        self.add_bezier('p1-r1-7', (16, 30), ((12, 30), (9, 30), (6, 29)))
        self.add_line('p1-r1-8', (6, 29), (9, 23))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_bezier('p2-r1-1', (16, 12), ((15, 11), (14, 10), (13, 10)))
        self.add_bezier('p2-r1-2', (13, 10), ((12, 10), (11, 12), (11, 14)))
        self.add_bezier('p2-r1-3', (11, 14), ((11, 16), (12, 17), (13, 17)))
        self.add_bezier('p2-r1-4', (13, 17), ((14, 17), (15, 17), (16, 16)))
        self.add_bezier('p2-r1-5', (16, 16), ((17, 17), (18, 17), (19, 17)))
        self.add_bezier('p2-r1-6', (19, 17), ((20, 17), (21, 16), (21, 14)))
        self.add_bezier('p2-r1-7', (21, 14), ((21, 12), (20, 10), (19, 10)))
        self.add_bezier('p2-r1-8', (19, 10), ((18, 10), (17, 11), (16, 12)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
