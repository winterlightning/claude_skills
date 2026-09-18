"""Mirrored curved open pages with central fold and sparse tactile dots.
Keyshape ink bounds: (2, 6, 46, 42).
Construction reference: Lucide book-open; source render establishes subject.
Reduction: Eight source dots reduced to three generic tactile marks, with no invented inscription.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbb829d1-01cc-49f5-8c4d-bb18a32f2acf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/blind book open_dbb829d1-01cc-49f5-8c4d-bb18a32f2acf.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/blind book open_dbb829d1-01cc-49f5-8c4d-bb18a32f2acf.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'open-braille-book-batch-025-15'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ()
    keywords = ('open', 'braille', 'book')

    def build(self):
        self.add_bezier('top-left',(4,8),((14,8),(18,8),(24,14)))
        self.add_bezier('top-right',(24,14),((30,8),(34,8),(44,8)))
        self.add_line('right',(44,8),(44,34))
        self.add_bezier('bottom-right',(44,34),((34,34),(30,34),(24,40)))
        self.add_bezier('bottom-left',(24,40),((18,34),(14,34),(4,34)))
        self.add_line('left',(4,34),(4,8))
        self.add_contour('pages','top-left','top-right','right','bottom-right','bottom-left','left',closed=True)
        self.add_line('fold',(24,14),(24,40))
        self.relate('connect','fold','pages')
        for tag,x,y in [('l1',14,18),('l2',14,26),('r1',34,22)]: self.add_dot(tag,(x,y))
