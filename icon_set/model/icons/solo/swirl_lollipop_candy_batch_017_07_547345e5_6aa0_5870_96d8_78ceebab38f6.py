from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '547345e5-6aa0-5870-96d8-78ceebab38f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/baby family lolipop_547345e5-6aa0-5870-96d8-78ceebab38f6.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/baby family lolipop_547345e5-6aa0-5870-96d8-78ceebab38f6.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/07-swirl-lollipop-candy--547345e5-6aa0-5870-96d8-78ceebab38f6.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Spiral head and diagonal stick separated by a clear cut.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'swirl-lollipop-candy-batch-017-07'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('candy', 'sweet', 'lollipop', 'spiral', 'swirl', 'stick', 'treat', 'confectionery')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('outer', (26, 38), (26, 6), radius_x=16, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('middle', (26, 6), (26, 28), radius_x=11, radius_y=11, sweep=False, large_arc=False)
        self.add_arc('inner', (26, 28), (26, 16), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_contour('spiral', 'outer', 'middle', 'inner', closed=False)
        self.add_line('stick', (14, 34), (6, 42))
