from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc1e2dbd-292e-42fa-a1c7-f4605f4b7b93'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_cc1e2dbd-292e-42fa-a1c7-f4605f4b7b93.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/house_cc1e2dbd-292e-42fa-a1c7-f4605f4b7b93.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/07-simple-home-icon-with-arched-door--cc1e2dbd-292e-42fa-a1c7-f4605f4b7b93.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'house: shared roof axis and integrated doorway.'

class BatchIcon(Solo48):
    icon_id = 'house-with-arched-doorway-batch-016-07'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    keywords = ('house', 'home', 'roof', 'door', 'building', 'entrance')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('roof', (6, 24), (10, 20), (24, 6), (38, 20), (42, 24), closed=False)
        self.add_polyline('walls', (10, 20), (10, 42), (18, 42), (30, 42), (38, 42), (38, 20), closed=False)
        self.add_line('door-left', (18, 42), (18, 32))
        self.add_arc('door-arch', (18, 32), (30, 32), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('door-right', (30, 32), (30, 42))
        self.add_contour('door', 'door-left', 'door-arch', 'door-right', closed=False)
        self.relate("connect", 'roof', 'walls')
        self.relate("connect", 'walls', 'door')
