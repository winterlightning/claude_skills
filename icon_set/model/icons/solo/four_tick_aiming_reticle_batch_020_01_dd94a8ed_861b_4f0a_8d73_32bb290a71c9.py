from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd94a8ed-861b-4f0a-8d73-32bb290a71c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/circle clock_dd94a8ed-861b-4f0a-8d73-32bb290a71c9.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/circle clock_dd94a8ed-861b-4f0a-8d73-32bb290a71c9.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/01-circular-aiming-reticle--dd94a8ed-861b-4f0a-8d73-32bb290a71c9.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'four-tick-aiming-reticle-batch-020-01'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('reticle', 'aim', 'target', 'circle', 'ticks', 'sight', 'focus', 'crosshair')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('ring-0', (24, 4), (44, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('ring-1', (44, 24), (24, 44), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('ring-2', (24, 44), (4, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('ring-3', (4, 24), (24, 4), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_line('tick-0', (24, 4), (24, 12))
        self.add_line('tick-1', (44, 24), (36, 24))
        self.add_line('tick-2', (24, 44), (24, 36))
        self.add_line('tick-3', (4, 24), (12, 24))
        self.relate("connect", 'ring-0', 'ring-1')
        self.relate("connect", 'ring-0', 'ring-3')
        self.relate("connect", 'ring-0', 'tick-0')
        self.relate("connect", 'ring-0', 'tick-1')
        self.relate("connect", 'ring-1', 'ring-2')
        self.relate("connect", 'ring-1', 'tick-1')
        self.relate("connect", 'ring-1', 'tick-2')
        self.relate("connect", 'ring-2', 'ring-3')
        self.relate("connect", 'ring-2', 'tick-2')
        self.relate("connect", 'ring-2', 'tick-3')
        self.relate("connect", 'ring-3', 'tick-0')
        self.relate("connect", 'ring-3', 'tick-3')
