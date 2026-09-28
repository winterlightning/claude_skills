"""Symmetric rounded dome with flowing flared skirt and a short crown finial.
Keyshape ink bounds: (4, 4, 44, 44).
Construction reference: Lucide bell; source render establishes subject.
Reduction: No clapper added because source has none.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37d06a72-3489-49e9-931d-b10559d99ab1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bell_37d06a72-3489-49e9-931d-b10559d99ab1.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/bell_37d06a72-3489-49e9-931d-b10559d99ab1.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'notification-bell-solo-batch-025-11'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('notification', 'bell', 'solo')

    def build(self):
        # Circular crown joins vertical skirt tangentially, mirrored about x=24.
        self.add_bezier('left',(6,42),((10,36),(12,32),(12,24)))
        self.add_arc('dome-left',(12,24),(24,12),radius_x=12)
        self.add_arc('dome-right',(24,12),(36,24),radius_x=12)
        self.add_bezier('right',(36,24),((36,32),(38,36),(42,42)))
        self.add_line('rim',(42,42),(6,42))
        self.add_contour('bell','left','dome-left','dome-right','right','rim',closed=True)
        self.add_line('finial',(24,6),(24,12))
        self.relate('connect','finial','bell')
