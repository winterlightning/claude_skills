from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '076bc927-b602-45b8-bfda-183eca16fa3c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/angry person_076bc927-b602-45b8-bfda-183eca16fa3c.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/angry person_076bc927-b602-45b8-bfda-183eca16fa3c.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/03-angry-person-profile-icon--076bc927-b602-45b8-bfda-183eca16fa3c.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Shared human user.svg informed circular head and broad shoulders. Head bottom y34, shoulder top y42: exact 4-unit ink gap.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'angry-person-bust-batch-019-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    keywords = ('person', 'angry', 'face', 'bust', 'emotion', 'frown', 'user', 'expression')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('head-0', (9, 19), (24, 4), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('head-1', (24, 4), (39, 19), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('head-2', (39, 19), (24, 34), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('head-3', (24, 34), (9, 19), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_contour('head', 'head-0', 'head-1', 'head-2', 'head-3', closed=True)
        self.add_arc('shoulders', (8, 44), (40, 44), radius_x=16, radius_y=2, sweep=True, large_arc=False)
        self.add_line('brow-left', (19, 15), (20, 16))
        self.add_line('brow-right', (28, 16), (29, 15))
        self.add_arc('frown', (22, 25), (26, 25), radius_x=2, radius_y=1, sweep=True, large_arc=False)
