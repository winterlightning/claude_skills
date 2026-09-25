from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '731ae1df-31e9-4e26-9ef7-b84535fc2ef6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/eyeglasses_731ae1df-31e9-4e26-9ef7-b84535fc2ef6.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/eyeglasses_731ae1df-31e9-4e26-9ef7-b84535fc2ef6.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/07-classic-rounded-frame-eyeglasses--731ae1df-31e9-4e26-9ef7-b84535fc2ef6.md'
DESIGN_PLAN = 'Equal circular lens frames arranged on a horizontal axis, joined by an 8-unit bridge.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'glasses: paired empty lens frames and short bridge.'

class BatchIcon(Solo48):
    icon_id = 'eyeglasses-batch-020-07'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('eyeglasses', 'glasses', 'spectacles', 'eyewear', 'lens', 'vision', 'optical', 'accessory')

    def build(self):
        # Equal circular lens frames arranged on a horizontal axis, joined by an 8-unit bridge.
        self.add_arc('left-0', (4, 24), (12, 16), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('left-1', (12, 16), (20, 24), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('left-2', (20, 24), (12, 32), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('left-3', (12, 32), (4, 24), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('left', 'left-0', 'left-1', 'left-2', 'left-3', closed=True)
        self.add_arc('right-0', (28, 24), (36, 16), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('right-1', (36, 16), (44, 24), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('right-2', (44, 24), (36, 32), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('right-3', (36, 32), (28, 24), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('right', 'right-0', 'right-1', 'right-2', 'right-3', closed=True)
        self.add_line('bridge', (20, 24), (28, 24))
        self.relate("connect", 'left', 'bridge')
        self.relate("connect", 'right', 'bridge')
