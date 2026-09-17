"""Ship in a Bottle.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Horizontal bottle with right neck and tiny sailboat.
Reduction: Omit support feet; retain bottle, sail and hull as physical display scene.
Construction reference: sailboat: upright mast, one triangular sail and broad hull
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5720cf8d-a68c-5487-ad88-9c5c72331cbb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/crafts bottle art ship_5720cf8d-a68c-5487-ad88-9c5c72331cbb.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/crafts bottle art ship_5720cf8d-a68c-5487-ad88-9c5c72331cbb.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/crafts bottle art ship_5720cf8d-a68c-5487-ad88-9c5c72331cbb.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'ship-in-a-bottle-batch-013-14'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('ship', 'bottle', 'sailboat', 'model', 'craft', 'display')

    def build(self):
        self.add_line('bottle-1', (10, 8), (28, 8))
        self.add_bezier('bottle-2', (28, 8), ((34, 8), (34, 16), (40, 16)))
        self.add_line('bottle-3', (40, 16), (44, 16))
        self.add_line('bottle-4', (44, 16), (44, 32))
        self.add_line('bottle-5', (44, 32), (40, 32))
        self.add_bezier('bottle-6', (40, 32), ((34, 32), (34, 40), (28, 40)))
        self.add_line('bottle-7', (28, 40), (10, 40))
        self.add_arc('bottle-8', (10, 40), (4, 34), radius_x=6, radius_y=6, sweep=True)
        self.add_line('bottle-9', (4, 34), (4, 14))
        self.add_arc('bottle-10', (4, 14), (10, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('bottle', 'bottle-1', 'bottle-2', 'bottle-3', 'bottle-4', 'bottle-5', 'bottle-6', 'bottle-7', 'bottle-8', 'bottle-9', 'bottle-10', closed=True)
        self.add_polyline('sail', (17, 30), (17, 17), (28, 30), closed=False)
        self.add_line('hull', (13, 30), (28, 30))
        self.relate("connect", 'sail', 'hull')
