from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a50ac06-4771-4a58-8940-8f56776aa85a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/office/desk document base work_8a50ac06-4771-4a58-8940-8f56776aa85a.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/desk document base work_8a50ac06-4771-4a58-8940-8f56776aa85a.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/13-office-computer-desk-workspace--8a50ac06-4771-4a58-8940-8f56776aa85a.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Two detached document marks retained; one drawer instead of multiple narrow rails.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'desk-with-computer-monitor-batch-018-13'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "office"
    keywords = ('desk', 'computer', 'monitor', 'workspace', 'office', 'furniture', 'drawers', 'work')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('desk', (4, 40), (4, 28), (18, 28), (30, 28), (44, 28), (44, 40), closed=False)
        self.add_polyline('drawer', (30, 28), (30, 40), (44, 40), closed=False)
        self.add_line('monitor-0', (7, 8), (23, 8))
        self.add_arc('monitor-1', (23, 8), (26, 11), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('monitor-2', (26, 11), (26, 17))
        self.add_arc('monitor-3', (26, 17), (23, 20), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('monitor-4', (23, 20), (7, 20))
        self.add_arc('monitor-5', (7, 20), (4, 17), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('monitor-6', (4, 17), (4, 11))
        self.add_arc('monitor-7', (4, 11), (7, 8), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('monitor', 'monitor-0', 'monitor-1', 'monitor-2', 'monitor-3', 'monitor-4', 'monitor-5', 'monitor-6', 'monitor-7', closed=True)
        self.add_line('stand', (15, 20), (15, 28))
        self.add_line('paper1', (35, 9), (44, 9))
        self.add_line('paper2', (35, 18), (44, 18))
        self.relate("connect", 'desk', 'drawer')
