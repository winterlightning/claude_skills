from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4211bd70-7ef9-520f-8c0e-7caa3ac14927'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house chimney_4211bd70-7ef9-520f-8c0e-7caa3ac14927.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/house chimney_4211bd70-7ef9-520f-8c0e-7caa3ac14927.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/10-simple-house-with-chimney--4211bd70-7ef9-520f-8c0e-7caa3ac14927.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Chimney is integrated into the right roof slope; asymmetry is intentional.']
CONSTRUCTION_REFERENCE = 'house: shared roof axis and integrated doorway.'

class BatchIcon(Solo48):
    icon_id = 'house-with-rectangular-chimney-batch-016-10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('house', 'home', 'chimney', 'roof', 'door', 'building')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('roof', (6, 24), (24, 6), (32, 14), (32, 6), (40, 6), (40, 22), (42, 24), closed=False)
        self.add_polyline('walls', (6, 24), (10, 24), (10, 42), (18, 42), (30, 42), (38, 42), (38, 24), (42, 24), closed=False)
        self.add_polyline('door', (18, 42), (18, 28), (30, 28), (30, 42), closed=False)
        self.relate("connect", 'roof', 'walls')
        self.relate("connect", 'walls', 'door')
