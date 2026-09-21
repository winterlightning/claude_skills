"""Independent 32px profile of prohibition-sign-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/prohitbition_ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/prohitbition_ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf.svg'), ('9d7e100f-bbce-49f1-a485-175de3295e3d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/cancel_9d7e100f-bbce-49f1-a485-175de3295e3d.svg'))
PROFILE_SOURCE_KEYS = ('solo/prohibition-sign-solo',)
SOLO_SOURCE_ICON_IDS = ('prohibition-sign-solo',)
REFERENCE_EXPORT_SHA256 = '23c54c8a7a1e6e82d73a8021292de19b8e794ebb3f94431efc854dd701fcc733'

class Drawing(Sub32):
    icon_id = 'prohibition-sign-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (8, 5), ((10, 3), (13, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((17, 2), (17, 2), (18, 2)))
        self.add_bezier('p1-r1-3', (18, 2), ((22, 3), (25, 5), (27, 8)))
        self.add_bezier('p1-r1-4', (27, 8), ((29, 10), (30, 13), (30, 16)))
        self.add_bezier('p1-r1-5', (30, 16), ((30, 17), (30, 17), (30, 18)))
        self.add_bezier('p1-r1-6', (30, 18), ((29, 22), (27, 25), (24, 27)))
        self.add_bezier('p1-r1-7', (24, 27), ((22, 29), (19, 30), (16, 30)))
        self.add_bezier('p1-r1-8', (16, 30), ((15, 30), (15, 30), (14, 30)))
        self.add_bezier('p1-r1-9', (14, 30), ((10, 29), (7, 27), (5, 24)))
        self.add_bezier('p1-r1-10', (5, 24), ((3, 22), (2, 19), (2, 16)))
        self.add_bezier('p1-r1-11', (2, 16), ((2, 15), (2, 15), (2, 14)))
        self.add_bezier('p1-r1-12', (2, 14), ((3, 10), (5, 7), (8, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (5, 24), (27, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
        self.relate("connect", 'p1-r1-10', 'p2-r1-1')
