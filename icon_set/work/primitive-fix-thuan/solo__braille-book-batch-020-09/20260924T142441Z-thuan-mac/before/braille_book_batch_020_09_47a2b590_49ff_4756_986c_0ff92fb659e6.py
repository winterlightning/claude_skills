from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47a2b590-49ff-4756-986c-0ff92fb659e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/blind book close_47a2b590-49ff-4756-986c-0ff92fb659e6.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/blind book close_47a2b590-49ff-4756-986c-0ff92fb659e6.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/09-closed-braille-book--47a2b590-49ff-4756-986c-0ff92fb659e6.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Six marks treated as generic tactile cues, not a transcribed Braille inscription.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'braille-book-batch-020-09'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('book', 'braille', 'tactile', 'reading', 'accessibility', 'cover', 'publication', 'library')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('book', (12, 4), (36, 4), (40, 8), (40, 36), (40, 40), (36, 44), (12, 44), (8, 40), (8, 8), closed=True)
        self.add_line('page', (12, 36), (40, 36))
        self.add_dot("tactile-0", (18, 12))
        self.add_dot("tactile-1", (28, 12))
        self.add_dot("tactile-2", (18, 20))
        self.add_dot("tactile-3", (28, 20))
        self.add_dot("tactile-4", (18, 28))
        self.add_dot("tactile-5", (28, 28))
        self.relate("connect", 'book', 'page')
