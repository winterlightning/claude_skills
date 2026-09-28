from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd582f271-48e8-45e5-a52a-ac9827b9bff7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-closed-book-batch-020-10/20260927T145836Z-thuan-mac-1/reference/book close lines_d582f271-48e8-45e5-a52a-ac9827b9bff7.svg'
AUTHOR = "gpt-6"
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/book close lines_d582f271-48e8-45e5-a52a-ac9827b9bff7.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/10-closed-horizontal-book--d582f271-48e8-45e5-a52a-ac9827b9bff7.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Open right ends and two page lines match the source.']
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
        # Preserve the reference's open right end and rounded left spine.
        self.add_line('top', (44, 8), (9, 8))
        self.add_arc('upper-spine', (9, 8), (4, 13), radius_x=5, sweep=False)
        self.add_line('spine', (4, 13), (4, 35))
        self.add_arc('lower-spine', (4, 35), (9, 40), radius_x=5, sweep=False)
        self.add_line('bottom', (9, 40), (44, 40))
        self.add_contour('book', 'top', 'upper-spine', 'spine', 'lower-spine', 'bottom')
        for name, y in (('page-top', 20), ('page-bottom', 30)):
            self.add_line(name, (13, y), (40, y))
