"""Revision: Raised the top dome and expanded the central patty band with consistent eight-unit spacing."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'be3b26b6-b45d-4812-8c00-261ef430b1ad'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hamburger-solo-batch-020-05/20260927T101626Z-thuan-mac-1/reference/hamburger_be3b26b6-b45d-4812-8c00-261ef430b1ad.svg'
AUTHOR = "gpt-6"
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/hamburger_be3b26b6-b45d-4812-8c00-261ef430b1ad.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/05-classic-fast-food-hamburger--be3b26b6-b45d-4812-8c00-261ef430b1ad.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Three layers and two full-width seams retained.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'hamburger-solo-batch-020-05'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    keywords = ('hamburger', 'burger', 'bun', 'food', 'sandwich', 'meal', 'snack', 'fast-food')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('bun-top', (6, 23), (42, 23), radius_x=18, radius_y=15, sweep=True, large_arc=False)
        self.add_polyline('bun-base', (42, 23), (44, 27), (42, 31), (6, 31), (4, 27), (6, 23), closed=False)
        self.add_line('top-seam', (6, 23), (42, 23))
        self.add_arc('bun-bottom', (42, 31), (6, 31), radius_x=18, radius_y=9, sweep=True, large_arc=False)
        self.relate("connect", 'bun-top', 'bun-base')
        self.relate("connect", 'bun-top', 'top-seam')
        self.relate("connect", 'bun-base', 'top-seam')
        self.relate("connect", 'bun-base', 'bun-bottom')
