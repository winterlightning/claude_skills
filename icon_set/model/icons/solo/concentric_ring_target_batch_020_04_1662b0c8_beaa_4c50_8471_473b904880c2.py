from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1662b0c8-beaa-4c50-8471-473b904880c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/chinese board_1662b0c8-beaa-4c50-8471-473b904880c2.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/chinese board_1662b0c8-beaa-4c50-8471-473b904880c2.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/04-circular-target-symbol--1662b0c8-beaa-4c50-8471-473b904880c2.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Two rings retained: a third nested ring cannot keep 4-unit ink clearance.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'concentric-ring-target-batch-020-04'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('target', 'bullseye', 'rings', 'crosshair', 'aim', 'concentric', 'circle', 'sight')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('ring-20-0', (24, 4), (44, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('ring-20-1', (44, 24), (24, 44), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('ring-20-2', (24, 44), (4, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('ring-20-3', (4, 24), (24, 4), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('ring-10-0', (24, 14), (34, 24), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ring-10-1', (34, 24), (24, 34), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ring-10-2', (24, 34), (14, 24), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ring-10-3', (14, 24), (24, 14), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('spoke-0', (24, 14), (24, 4))
        self.add_line('spoke-1', (34, 24), (44, 24))
        self.add_line('spoke-2', (24, 34), (24, 44))
        self.add_line('spoke-3', (14, 24), (4, 24))
        self.relate("connect", 'ring-20-0', 'ring-20-1')
        self.relate("connect", 'ring-20-0', 'ring-20-3')
        self.relate("connect", 'ring-20-0', 'spoke-0')
        self.relate("connect", 'ring-20-0', 'spoke-1')
        self.relate("connect", 'ring-20-1', 'ring-20-2')
        self.relate("connect", 'ring-20-1', 'spoke-1')
        self.relate("connect", 'ring-20-1', 'spoke-2')
        self.relate("connect", 'ring-20-2', 'ring-20-3')
        self.relate("connect", 'ring-20-2', 'spoke-2')
        self.relate("connect", 'ring-20-2', 'spoke-3')
        self.relate("connect", 'ring-20-3', 'spoke-0')
        self.relate("connect", 'ring-20-3', 'spoke-3')
        self.relate("connect", 'ring-10-0', 'ring-10-1')
        self.relate("connect", 'ring-10-0', 'ring-10-3')
        self.relate("connect", 'ring-10-0', 'spoke-0')
        self.relate("connect", 'ring-10-0', 'spoke-1')
        self.relate("connect", 'ring-10-1', 'ring-10-2')
        self.relate("connect", 'ring-10-1', 'spoke-1')
        self.relate("connect", 'ring-10-1', 'spoke-2')
        self.relate("connect", 'ring-10-2', 'ring-10-3')
        self.relate("connect", 'ring-10-2', 'spoke-2')
        self.relate("connect", 'ring-10-2', 'spoke-3')
        self.relate("connect", 'ring-10-3', 'spoke-0')
        self.relate("connect", 'ring-10-3', 'spoke-3')
