"""House with Chimney and Arched Entrance.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Peaked house envelope with centered entrance and mirrored walls.
Reduction: Connect eaves cleanly; preserve requested entrance detail.
Construction reference: house: broad roof, simple wall and doorway contours
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48ea3c6c-5c29-50ff-bdb7-99895f95d856'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house chimney_48ea3c6c-5c29-50ff-bdb7-99895f95d856.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house chimney_48ea3c6c-5c29-50ff-bdb7-99895f95d856.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/house chimney_48ea3c6c-5c29-50ff-bdb7-99895f95d856.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'house-with-chimney-reference-batch-015-09'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('house', 'home', 'chimney', 'roof', 'door', 'building')

    def build(self):
        self.add_line('house-1', (6, 24), (24, 6))
        self.add_line('house-2', (24, 6), (32, 14))
        self.add_line('house-3', (32, 14), (32, 6))
        self.add_line('house-4', (32, 6), (42, 6))
        self.add_line('house-5', (42, 6), (42, 38))
        self.add_arc('house-6', (42, 38), (38, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('house-7', (38, 42), (30, 42))
        self.add_line('house-8', (30, 42), (30, 32))
        self.add_arc('house-9', (30, 32), (18, 32), radius_x=6, radius_y=6, sweep=False)
        self.add_line('house-10', (18, 32), (18, 42))
        self.add_line('house-11', (18, 42), (10, 42))
        self.add_line('house-12', (10, 42), (10, 20))
        self.add_contour('house', 'house-1', 'house-2', 'house-3', 'house-4', 'house-5', 'house-6', 'house-7', 'house-8', 'house-9', 'house-10', 'house-11', 'house-12', closed=False)
