from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5aacf220-3104-5628-83e3-8dddf6e85cbc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/settings off_5aacf220-3104-5628-83e3-8dddf6e85cbc.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/settings off_5aacf220-3104-5628-83e3-8dddf6e85cbc.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/14-toggle-switch-off--5aacf220-3104-5628-83e3-8dddf6e85cbc.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Both strokes retained, as shown in the held reference.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'capsule-switch-with-two-strokes-batch-016-14'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('switch', 'toggle', 'capsule', 'control', 'off', 'setting')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_line('capsule-0', (18, 10), (30, 10))
        self.add_arc('capsule-1', (30, 10), (44, 24), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('capsule-3', (44, 24), (30, 38), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_line('capsule-4', (30, 38), (18, 38))
        self.add_arc('capsule-5', (18, 38), (4, 24), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('capsule-7', (4, 24), (18, 10), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_contour('capsule', 'capsule-0', 'capsule-1', 'capsule-3', 'capsule-4', 'capsule-5', 'capsule-7', closed=True)
        self.add_line('left-mark', (17, 21), (17, 27))
        self.add_line('right-mark', (25, 21), (25, 27))
