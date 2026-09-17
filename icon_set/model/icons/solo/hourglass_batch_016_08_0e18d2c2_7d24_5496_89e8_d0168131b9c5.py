from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e18d2c2-7d24-5496-89e8-d0168131b9c5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/08-simple-hourglass-time-symbol--0e18d2c2-7d24-5496-89e8-d0168131b9c5.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Chambers use deliberate straight slopes instead of many small curves.']
CONSTRUCTION_REFERENCE = 'hourglass: broad caps and a pinched waist.'

class BatchIcon(Solo48):
    icon_id = 'hourglass-batch-016-08'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('hourglass', 'time', 'timer', 'glass', 'chambers', 'waist')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('glass', (8, 4), (40, 4), (40, 12), (24, 24), (40, 36), (40, 44), (8, 44), (8, 36), (24, 24), (8, 12), closed=True)
