"""Independent 32px profile of upward-hand-pointer-batch-024-07.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'eab3080c-0a62-4d7b-b2b0-750ba686504c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand point 1_eab3080c-0a62-4d7b-b2b0-750ba686504c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eab3080c-0a62-4d7b-b2b0-750ba686504c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand point 1_eab3080c-0a62-4d7b-b2b0-750ba686504c.svg'), ('82734f7a-f16b-4ab7-8833-a4322d4cbd4b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand point_82734f7a-f16b-4ab7-8833-a4322d4cbd4b.svg'))
PROFILE_SOURCE_KEYS = ('solo/upward-hand-pointer-batch-024-07', 'solo/upward-hand-pointer-batch-024-08')
SOLO_SOURCE_ICON_IDS = ('upward-hand-pointer-batch-024-07', 'upward-hand-pointer-batch-024-08')
REFERENCE_EXPORT_SHA256 = 'aa934776c74bb68e01a16f3a104dde6a87e4430f41e0f1465eea3d92e1c7d917'

class Drawing(Sub32):
    icon_id = 'upward-hand-pointer-batch-024-07-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 30), (6, 22))
        self.add_bezier('p1-r1-2', (6, 22), ((6, 21), (5, 20), (5, 18)))
        self.add_bezier('p1-r1-3', (5, 18), ((5, 16), (6, 15), (7, 15)))
        self.add_bezier('p1-r1-4', (7, 15), ((8, 15), (9, 16), (10, 17)))
        self.add_line('p1-r1-5', (10, 17), (13, 20))
        self.add_line('p1-r1-6', (13, 20), (13, 5))
        self.add_arc('p1-r1-7', (13, 5), (19, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (19, 5), (19, 15))
        self.add_line('p1-r1-9', (19, 15), (20, 15))
        self.add_arc('p1-r1-10', (20, 15), (27, 22), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (27, 22), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
