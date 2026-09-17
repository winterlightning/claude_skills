from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f81bb0f5-e79c-5478-8158-f8e1d2294934'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys ping pong_f81bb0f5-e79c-5478-8158-f8e1d2294934.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/toys ping pong_f81bb0f5-e79c-5478-8158-f8e1d2294934.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/08-table-tennis-paddle-and-ball--f81bb0f5-e79c-5478-8158-f8e1d2294934.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Paddle face seam omitted to reserve space for the separate ball.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'table-tennis-paddle-and-ball-batch-017-08'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('table-tennis', 'paddle', 'ball', 'sport', 'game', 'racket', 'ping-pong', 'recreation')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('paddle-0', (10, 18), (22, 6), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('paddle-1', (22, 6), (34, 18), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('paddle-2', (34, 18), (22, 30), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('paddle-3', (22, 30), (10, 18), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('paddle', 'paddle-0', 'paddle-1', 'paddle-2', 'paddle-3', closed=True)
        self.add_polyline('handle', (10, 18), (6, 34), (6, 42), (14, 42), (22, 30), closed=False)
        self.add_arc('ball-0', (34, 38), (38, 34), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('ball-1', (38, 34), (42, 38), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('ball-2', (42, 38), (38, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('ball-3', (38, 42), (34, 38), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('ball', 'ball-0', 'ball-1', 'ball-2', 'ball-3', closed=True)
        self.relate("connect", 'paddle', 'handle')
