from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40ae9091-ac10-4c02-88bc-c04028f85e36'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_40ae9091-ac10-4c02-88bc-c04028f85e36.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/house_40ae9091-ac10-4c02-88bc-c04028f85e36.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/12-simple-minimalist-home-icon--40ae9091-ac10-4c02-88bc-c04028f85e36.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'house: shared roof axis and integrated doorway.'

class BatchIcon(Solo48):
    icon_id = 'house-with-interior-door-stroke-batch-016-12'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('house', 'home', 'roof', 'building', 'facade', 'door')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('roof', (6, 24), (10, 20), (24, 6), (38, 20), (42, 24), closed=False)
        self.add_polyline('walls', (10, 20), (10, 42), (18, 42), (30, 42), (38, 42), (38, 20), closed=False)
        self.add_line('door-mark', (24, 26), (24, 33))
        self.relate("connect", 'roof', 'walls')
