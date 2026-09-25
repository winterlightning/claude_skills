from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84ddd6c0-d313-4647-9090-7ddb7ff5e377'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys train_84ddd6c0-d313-4647-9090-7ddb7ff5e377.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/toys train_84ddd6c0-d313-4647-9090-7ddb7ff5e377.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/12-toy-steam-train-engine--84ddd6c0-d313-4647-9090-7ddb7ff5e377.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Cab window and wheel hubs omitted to keep the locomotive clear.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'toy-steam-train-engine-batch-017-12'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    keywords = ('train', 'locomotive', 'toy', 'steam', 'engine', 'wheels', 'chimney', 'transport')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('engine', (4, 28), (4, 20), (10, 20), (10, 8), (18, 8), (18, 20), (26, 20), (26, 8), (44, 8), (44, 28), (36, 28), (12, 28), closed=True)
        self.add_arc('left-wheel-0', (6, 34), (12, 28), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('left-wheel-1', (12, 28), (18, 34), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('left-wheel-2', (18, 34), (12, 40), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('left-wheel-3', (12, 40), (6, 34), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('left-wheel', 'left-wheel-0', 'left-wheel-1', 'left-wheel-2', 'left-wheel-3', closed=True)
        self.add_arc('right-wheel-0', (30, 34), (36, 28), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('right-wheel-1', (36, 28), (42, 34), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('right-wheel-2', (42, 34), (36, 40), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('right-wheel-3', (36, 40), (30, 34), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('right-wheel', 'right-wheel-0', 'right-wheel-1', 'right-wheel-2', 'right-wheel-3', closed=True)
        self.relate("connect", 'engine', 'left-wheel')
        self.relate("connect", 'engine', 'right-wheel')
