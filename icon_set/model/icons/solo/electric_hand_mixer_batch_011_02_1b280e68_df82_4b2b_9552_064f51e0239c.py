"""Electric Hand Mixer.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Rounded motor housing with an open grip and attached single beater.
Reduction: Drop tiny control mark; one beater loop represents wire cage.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b280e68-df82-4b2b-9552-064f51e0239c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/mixer_1b280e68-df82-4b2b-9552-064f51e0239c.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mixer_1b280e68-df82-4b2b-9552-064f51e0239c.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/mixer_1b280e68-df82-4b2b-9552-064f51e0239c.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'electric-hand-mixer-batch-011-02'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('mixer', 'hand', 'electric', 'beater', 'appliance', 'kitchen')

    def build(self):
        self.add_line('housing-1', (12, 6), (36, 6))
        self.add_arc('housing-2', (36, 6), (42, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_line('housing-3', (42, 12), (42, 20))
        self.add_arc('housing-4', (42, 20), (36, 26), radius_x=6, radius_y=6, sweep=True)
        self.add_line('housing-5', (36, 26), (12, 26))
        self.add_arc('housing-6', (12, 26), (6, 20), radius_x=6, radius_y=6, sweep=True)
        self.add_line('housing-7', (6, 20), (6, 12))
        self.add_arc('housing-8', (6, 12), (12, 6), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('housing', 'housing-1', 'housing-2', 'housing-3', 'housing-4', 'housing-5', 'housing-6', 'housing-7', 'housing-8', closed=True)
        self.add_line('grip', (25, 16), (32, 16))
        self.add_line('shaft', (14, 26), (14, 34))
        self.add_bezier('beater-1', (14, 34), ((6, 34), (6, 42), (14, 42)))
        self.add_bezier('beater-2', (14, 42), ((22, 42), (22, 34), (14, 34)))
        self.add_contour('beater', 'beater-1', 'beater-2', closed=True)
        self.relate("connect", 'housing', 'shaft')
        self.relate("connect", 'shaft', 'beater')
