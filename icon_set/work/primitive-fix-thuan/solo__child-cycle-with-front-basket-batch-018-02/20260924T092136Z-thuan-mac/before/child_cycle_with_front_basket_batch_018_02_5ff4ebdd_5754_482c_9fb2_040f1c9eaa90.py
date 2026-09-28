from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ff4ebdd-5754-482c-9fb2-040f1c9eaa90'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/tricycle_5ff4ebdd-5754-482c-9fb2-040f1c9eaa90.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/tricycle_5ff4ebdd-5754-482c-9fb2-040f1c9eaa90.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/02-tricycle-with-front-basket--5ff4ebdd-5754-482c-9fb2-040f1c9eaa90.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Raised basket and high seat maintain wheel clearance.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'child-cycle-with-front-basket-batch-018-02'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('cycle', 'tricycle', 'bicycle', 'basket', 'wheels', 'seat', 'child', 'transport')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('rear-wheel-0', (4, 33), (11, 26), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('rear-wheel-1', (11, 26), (18, 33), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('rear-wheel-2', (18, 33), (11, 40), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('rear-wheel-3', (11, 40), (4, 33), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('rear-wheel', 'rear-wheel-0', 'rear-wheel-1', 'rear-wheel-2', 'rear-wheel-3', closed=True)
        self.add_arc('front-wheel-0', (30, 33), (37, 26), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('front-wheel-1', (37, 26), (44, 33), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('front-wheel-2', (44, 33), (37, 40), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('front-wheel-3', (37, 40), (30, 33), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('front-wheel', 'front-wheel-0', 'front-wheel-1', 'front-wheel-2', 'front-wheel-3', closed=True)
        self.add_polyline('frame', (11, 26), (11, 16), (25, 16), (31, 12), (37, 26), closed=False)
        self.add_line('seat', (8, 8), (11, 16))
        self.add_polyline('stem', (27, 8), (31, 8), (31, 12), closed=False)
        self.add_polyline('basket', (31, 8), (44, 8), (42, 16), (33, 16), closed=False)
        self.relate("connect", 'rear-wheel', 'frame')
        self.relate("connect", 'front-wheel', 'frame')
        self.relate("connect", 'frame', 'seat')
        self.relate("connect", 'frame', 'stem')
        self.relate("connect", 'stem', 'basket')
