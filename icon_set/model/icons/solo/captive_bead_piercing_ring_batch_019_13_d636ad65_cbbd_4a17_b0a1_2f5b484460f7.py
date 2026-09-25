from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd636ad65-cbbd-4a17-b0a1-2f5b484460f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/circle top circle_d636ad65-cbbd-4a17-b0a1-2f5b484460f7.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/circle top circle_d636ad65-cbbd-4a17-b0a1-2f5b484460f7.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/13-captive-bead-ring-piercing--d636ad65-cbbd-4a17-b0a1-2f5b484460f7.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Open bottom ring and central captive bead remain separate.', 'Ring opens broadly above bead to keep distinct strokes clear.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'captive-bead-piercing-ring-batch-019-13'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("container", "other", "primitives-generate")
    keywords = ('piercing', 'ring', 'bead', 'jewelry', 'captive', 'circular', 'accessory', 'body')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('left', (8, 20), (24, 4), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('right', (24, 4), (40, 20), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('lower-left', (12, 30), (8, 20), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('lower-right', (40, 20), (36, 30), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('bead-0', (18, 38), (24, 32), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('bead-1', (24, 32), (30, 38), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('bead-2', (30, 38), (24, 44), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('bead-3', (24, 44), (18, 38), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('bead', 'bead-0', 'bead-1', 'bead-2', 'bead-3', closed=True)
        self.relate("connect", 'left', 'right')
        self.relate("connect", 'left', 'lower-left')
        self.relate("connect", 'right', 'lower-right')
