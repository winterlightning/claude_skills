"""One angular closed navigation pointer, preserving upper-right heading.
Keyshape ink bounds: (4, 4, 44, 44).
Construction reference: Lucide navigation; source render establishes subject.
Reduction: No simplification needed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae765421-f3e6-417b-aaad-f27e361d2511'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cursor right_ae765421-f3e6-417b-aaad-f27e361d2511.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/cursor right_ae765421-f3e6-417b-aaad-f27e361d2511.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'navigation-pointer-arrow-batch-025-09'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("state", "other", "primitives-generate")
    aliases = ()
    keywords = ('navigation', 'pointer', 'arrow')

    def build(self):
        self.add_polyline('pointer',(6,24),(42,6),(28,42),(22,28),closed=True)
