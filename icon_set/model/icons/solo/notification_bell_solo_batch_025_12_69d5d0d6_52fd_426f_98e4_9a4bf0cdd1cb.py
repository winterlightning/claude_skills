"""Domed bell with flared corners and attached central clapper stem.
Keyshape ink bounds: (6, 2, 42, 46).
Construction reference: Lucide bell; source render establishes subject.
Reduction: No crown finial added because source has none.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69d5d0d6-52fd-426f-98e4-9a4bf0cdd1cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bell_69d5d0d6-52fd-426f-98e4-9a4bf0cdd1cb.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/bell_69d5d0d6-52fd-426f-98e4-9a4bf0cdd1cb.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'notification-bell-solo-batch-025-12'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ()
    keywords = ('notification', 'bell', 'solo')

    def build(self):
        self.add_arc('dome',(12,16),(36,16),radius_x=12)
        self.add_bezier('right',(36,16),((36,28),(36,30),(40,36)))
        self.add_line('rim-1', (40, 36), (24, 36))
        self.add_line('rim-2', (24, 36), (8, 36))
        self.add_bezier('left',(8,36),((12,30),(12,28),(12,16)))
        self.add_contour('bell','dome','right','rim-1','rim-2','left',closed=True)
        self.add_line('clapper',(24,36),(24,44))
        self.relate('connect','clapper','bell')
