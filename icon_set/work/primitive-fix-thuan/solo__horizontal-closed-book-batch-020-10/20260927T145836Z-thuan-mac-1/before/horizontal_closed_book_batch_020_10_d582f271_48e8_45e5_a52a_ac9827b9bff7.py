from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd582f271-48e8-45e5-a52a-ac9827b9bff7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/book close lines_d582f271-48e8-45e5-a52a-ac9827b9bff7.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/book close lines_d582f271-48e8-45e5-a52a-ac9827b9bff7.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/10-closed-horizontal-book--d582f271-48e8-45e5-a52a-ac9827b9bff7.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Completed clipped right ends; two internal page lines retained.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'horizontal-closed-book-batch-020-10'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "state", "primitives-generate")
    keywords = ('book', 'closed', 'spine', 'pages', 'reading', 'horizontal', 'library', 'publication')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_line('book-0', (9, 8), (39, 8))
        self.add_arc('book-1', (39, 8), (44, 13), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('book-2', (44, 13), (44, 35))
        self.add_arc('book-3', (44, 35), (39, 40), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('book-4', (39, 40), (9, 40))
        self.add_arc('book-5', (9, 40), (4, 35), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('book-6', (4, 35), (4, 13))
        self.add_arc('book-7', (4, 13), (9, 8), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('book', 'book-0', 'book-1', 'book-2', 'book-3', 'book-4', 'book-5', 'book-6', 'book-7', closed=True)
        self.add_line('page1', (15, 19), (44, 19))
        self.add_line('page2', (15, 29), (44, 29))
