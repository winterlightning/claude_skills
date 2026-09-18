"""Independent 32px profile of geometric-shapes-in-rounded-square-batch-006-02.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '610733a3-dfd5-42df-9651-d396d039493b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/shapes_610733a3-dfd5-42df-9651-d396d039493b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('610733a3-dfd5-42df-9651-d396d039493b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/shapes_610733a3-dfd5-42df-9651-d396d039493b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/geometric-shapes-in-rounded-square-batch-006-02',)
SOLO_SOURCE_ICON_IDS = ('geometric-shapes-in-rounded-square-batch-006-02',)
REFERENCE_EXPORT_SHA256 = 'd38ff80d7fc9183b47c7ff0c0ba2e766d259eed2a5f1a6bfa3e53affb9940c45'

class Drawing(Sub32):
    icon_id = 'geometric-shapes-in-rounded-square-batch-006-02-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/batch-006'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 2), (28, 2))
        self.add_arc('p1-r1-2', (28, 2), (30, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 4), (30, 28))
        self.add_arc('p1-r1-4', (30, 28), (28, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (28, 30), (27, 30))
        self.add_line('p1-r1-6', (27, 30), (13, 30))
        self.add_line('p1-r1-7', (13, 30), (4, 30))
        self.add_arc('p1-r1-8', (4, 30), (2, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 28), (2, 24))
        self.add_line('p1-r1-10', (2, 24), (2, 16))
        self.add_line('p1-r1-11', (2, 16), (2, 4))
        self.add_arc('p1-r1-12', (2, 4), (4, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (2, 16), (10, 16))
        self.add_line('p2-r1-2', (10, 16), (10, 24))
        self.add_line('p2-r1-3', (10, 24), (2, 24))
        self.add_line('p2-r1-4', (2, 24), (2, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_arc('p3-r1-1', (18, 11), (21, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (21, 9), (23, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (23, 11), (21, 14), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (21, 14), (18, 11), radius_x=2.1213203435596424, radius_y=2.1213203435596424, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (20, 21), (27, 30))
        self.add_line('p4-r1-2', (27, 30), (13, 30))
        self.add_line('p4-r1-3', (13, 30), (20, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate("connect", 'p1-r1-5', 'p4-r1-1')
        self.relate("connect", 'p1-r1-5', 'p4-r1-2')
        self.relate("connect", 'p1-r1-6', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p4-r1-2')
        self.relate("connect", 'p1-r1-6', 'p4-r1-3')
        self.relate("connect", 'p1-r1-7', 'p4-r1-2')
        self.relate("connect", 'p1-r1-7', 'p4-r1-3')
        self.relate("connect", 'p1-r1-9', 'p2-r1-3')
        self.relate("connect", 'p1-r1-9', 'p2-r1-4')
        self.relate("connect", 'p1-r1-10', 'p2-r1-1')
        self.relate("connect", 'p1-r1-10', 'p2-r1-3')
        self.relate("connect", 'p1-r1-10', 'p2-r1-4')
        self.relate("connect", 'p1-r1-11', 'p2-r1-1')
        self.relate("connect", 'p1-r1-11', 'p2-r1-4')
