from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '359d205e-3e65-4681-9176-4cc7661ec8be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_359d205e-3e65-4681-9176-4cc7661ec8be.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/house_359d205e-3e65-4681-9176-4cc7661ec8be.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/13-simple-residential-house-building--359d205e-3e65-4681-9176-4cc7661ec8be.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'house: shared roof axis and integrated doorway.'

class BatchIcon(Solo48):
    icon_id = 'house-with-open-rectangular-entrance-batch-016-13'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "other", "primitives-generate")
    keywords = ('house', 'home', 'roof', 'door', 'building', 'entrance')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('roof', (6, 24), (10, 20), (24, 6), (38, 20), (42, 24), closed=False)
        self.add_polyline('door', (18, 42), (18, 28), (30, 28), (30, 42), closed=False)
        self.add_polyline('wall-left', (10, 20), (10, 42), (18, 42), closed=False)
        self.add_polyline('wall-right', (30, 42), (38, 42), (38, 20), closed=False)
        self.relate("connect", 'roof', 'wall-left')
        self.relate("connect", 'roof', 'wall-right')
        self.relate("connect", 'door', 'wall-left')
        self.relate("connect", 'door', 'wall-right')
