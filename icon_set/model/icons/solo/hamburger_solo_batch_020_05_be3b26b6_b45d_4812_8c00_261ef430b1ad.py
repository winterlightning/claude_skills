from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be3b26b6-b45d-4812-8c00-261ef430b1ad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hamburger_be3b26b6-b45d-4812-8c00-261ef430b1ad.svg'
AUTHOR = 'gpt-6'
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
    category = "objects"
    keywords = ('hamburger', 'burger', 'bun', 'food', 'sandwich', 'meal', 'snack', 'fast-food')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('bun-top', (6, 22), (42, 22), radius_x=18, radius_y=14, sweep=True, large_arc=False)
        self.add_polyline('bun-base', (42, 22), (44, 26), (42, 30), (6, 30), (4, 26), (6, 22), closed=False)
        self.add_line('top-seam', (6, 22), (42, 22))
        self.add_arc('bun-bottom', (42, 30), (6, 30), radius_x=18, radius_y=10, sweep=True, large_arc=False)
        self.relate("connect", 'bun-top', 'bun-base')
        self.relate("connect", 'bun-top', 'top-seam')
        self.relate("connect", 'bun-base', 'top-seam')
        self.relate("connect", 'bun-base', 'bun-bottom')
