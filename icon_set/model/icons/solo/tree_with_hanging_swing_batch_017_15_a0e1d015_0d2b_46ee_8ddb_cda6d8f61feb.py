from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/15-tree-with-hanging-swing--a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Three-lobed crown supports a two-rope swing at right.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'tree-with-hanging-swing-batch-017-15'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    categories = ("primitives", "kids")
    keywords = ('tree', 'swing', 'branch', 'ropes', 'seat', 'playground', 'outdoors', 'childhood')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('left-crown', (14, 26), (14, 10), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('top-crown', (14, 10), (30, 10), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('right-crown', (30, 10), (30, 26), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('crown', 'left-crown', 'top-crown', 'right-crown', closed=False)
        self.add_polyline('trunk', (18, 19), (18, 30), (18, 42), closed=False)
        self.add_polyline('branch', (18, 30), (30, 26), (42, 26), closed=False)
        self.add_polyline('swing', (30, 26), (30, 42), (42, 42), (42, 26), closed=False)
        self.relate("connect", 'crown', 'branch')
        self.relate("connect", 'crown', 'swing')
        self.relate("connect", 'trunk', 'branch')
        self.relate("connect", 'branch', 'swing')
