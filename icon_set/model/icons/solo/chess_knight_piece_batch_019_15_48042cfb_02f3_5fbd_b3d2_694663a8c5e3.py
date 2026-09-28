from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48042cfb-02f3-5fbd-b3d2-694663a8c5e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/strategy chess_48042cfb-02f3-5fbd-b3d2-694663a8c5e3.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/strategy chess_48042cfb-02f3-5fbd-b3d2-694663a8c5e3.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/15-chess-knight-piece--48042cfb-02f3-5fbd-b3d2-694663a8c5e3.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Muzzle undercut widened; small eye and mane omitted.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'chess-knight-piece-batch-019-15'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    keywords = ('chess', 'knight', 'horse', 'piece', 'game', 'strategy', 'board', 'pedestal')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('horse', (12, 34), (24, 22), (16, 22), (8, 18), (16, 10), (20, 4), (30, 8), (38, 18), (36, 34), closed=False)
        self.add_line('base-0', (11, 34), (37, 34))
        self.add_arc('base-1', (37, 34), (40, 37), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('base-2', (40, 37), (40, 41))
        self.add_arc('base-3', (40, 41), (37, 44), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('base-4', (37, 44), (11, 44))
        self.add_arc('base-5', (11, 44), (8, 41), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('base-6', (8, 41), (8, 37))
        self.add_arc('base-7', (8, 37), (11, 34), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('base', 'base-0', 'base-1', 'base-2', 'base-3', 'base-4', 'base-5', 'base-6', 'base-7', closed=True)
