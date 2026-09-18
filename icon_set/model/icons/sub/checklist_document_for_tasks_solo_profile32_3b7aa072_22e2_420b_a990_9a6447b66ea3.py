"""Independent 32px profile of checklist-document-for-tasks-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3b7aa072-22e2-420b-a990-9a6447b66ea3'
SOURCE_PATH = 'pictographic-primitives/symbol/task list_3b7aa072-22e2-420b-a990-9a6447b66ea3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3b7aa072-22e2-420b-a990-9a6447b66ea3', 'pictographic-primitives/symbol/task list_3b7aa072-22e2-420b-a990-9a6447b66ea3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/checklist-document-for-tasks-solo',)
SOLO_SOURCE_ICON_IDS = ('checklist-document-for-tasks-solo',)
REFERENCE_EXPORT_SHA256 = 'a92e3d237ac9f07d637fcb3d2107e46eb57e4a77a671e826758be4a06a2f3fcf'

class Drawing(Sub32):
    icon_id = 'checklist-document-for-tasks-solo-profile32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (20, 2))
        self.add_line('p1-r1-2', (20, 2), (27, 9))
        self.add_line('p1-r1-3', (27, 9), (27, 30))
        self.add_line('p1-r1-4', (27, 30), (5, 30))
        self.add_line('p1-r1-5', (5, 30), (5, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (11, 11), (15, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (15, 11), (11, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (21, 12), (21, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (11, 22), (15, 22), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (15, 22), (11, 22), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (21, 23), (21, 23))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
