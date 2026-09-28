"""House with Arched Entrance.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Peaked house envelope with centered entrance and mirrored walls.
Reduction: Connect eaves cleanly; preserve requested entrance detail.
Construction reference: house: broad roof, simple wall and doorway contours
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '227ad5a9-e803-58fe-a499-6f8e9c5274e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_227ad5a9-e803-58fe-a499-6f8e9c5274e9.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_227ad5a9-e803-58fe-a499-6f8e9c5274e9.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/house_227ad5a9-e803-58fe-a499-6f8e9c5274e9.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'house-with-open-arched-entrance-batch-015-08'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('house', 'home', 'roof', 'arched', 'door', 'building')

    def build(self):
        self.add_polyline('roof', (6, 24), (10, 20), (24, 6), (38, 20), (42, 24), closed=False)
        self.add_line('walls-1', (10, 20), (10, 38))
        self.add_arc('walls-2', (10, 38), (14, 42), radius_x=4, radius_y=4, sweep=False)
        self.add_line('walls-3', (14, 42), (18, 42))
        self.add_line('walls-4', (18, 42), (18, 32))
        self.add_arc('walls-5', (18, 32), (30, 32), radius_x=6, radius_y=6, sweep=True)
        self.add_line('walls-6', (30, 32), (30, 42))
        self.add_line('walls-7', (30, 42), (34, 42))
        self.add_arc('walls-8', (34, 42), (38, 38), radius_x=4, radius_y=4, sweep=False)
        self.add_line('walls-9', (38, 38), (38, 20))
        self.add_contour('walls', 'walls-1', 'walls-2', 'walls-3', 'walls-4', 'walls-5', 'walls-6', 'walls-7', 'walls-8', 'walls-9', closed=False)
        self.relate("connect", 'roof', 'walls')
