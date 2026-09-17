from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1873be1c-2600-5197-83a2-680121a9a499'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/15-traditional-sand-timer-icon--1873be1c-2600-5197-83a2-680121a9a499.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Chambers use deliberate straight slopes instead of many small curves.']
CONSTRUCTION_REFERENCE = 'hourglass: broad caps and a pinched waist.'

class BatchIcon(Solo48):
    icon_id = 'hourglass-with-sand-level-batch-016-15'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('hourglass', 'sand', 'timer', 'time', 'glass', 'chambers')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('glass', (8, 4), (40, 4), (40, 12), (24, 24), (40, 36), (40, 44), (8, 44), (8, 36), (24, 24), (8, 12), closed=True)
        self.add_line('sand', (22, 12), (26, 12))
