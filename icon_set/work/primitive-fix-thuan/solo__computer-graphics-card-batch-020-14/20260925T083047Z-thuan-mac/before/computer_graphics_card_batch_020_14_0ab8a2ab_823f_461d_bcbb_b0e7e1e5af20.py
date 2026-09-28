from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ab8a2ab-823f-461d-bcbb-b0e7e1e5af20'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/gpu mining_0ab8a2ab-823f-461d-bcbb-b0e7e1e5af20.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/gpu mining_0ab8a2ab-823f-461d-bcbb-b0e7e1e5af20.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/14-computer-graphics-card--0ab8a2ab-823f-461d-bcbb-b0e7e1e5af20.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Circular fan, right detail and four pins retained.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'computer-graphics-card-batch-020-14'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    keywords = ('graphics', 'gpu', 'card', 'computer', 'circuit', 'hardware', 'fan', 'connector')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('board', (8, 8), (40, 8), (44, 12), (44, 32), (36, 32), (28, 32), (20, 32), (12, 32), (4, 32), (4, 12), closed=True)
        self.add_arc('fan-0', (14, 20), (17, 17), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('fan-1', (17, 17), (20, 20), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('fan-2', (20, 20), (17, 23), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('fan-3', (17, 23), (14, 20), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('fan', 'fan-0', 'fan-1', 'fan-2', 'fan-3', closed=True)
        self.add_line('detail', (31, 20), (36, 20))
        self.add_line('pin-12', (12, 32), (12, 40))
        self.add_line('pin-20', (20, 32), (20, 40))
        self.add_line('pin-28', (28, 32), (28, 40))
        self.add_line('pin-36', (36, 32), (36, 40))
        self.relate("connect", 'board', 'pin-12')
        self.relate("connect", 'board', 'pin-20')
        self.relate("connect", 'board', 'pin-28')
        self.relate("connect", 'board', 'pin-36')
