"""Professional Airbrush Spray Gun.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Airbrush barrel, top cup and angled grip at right.
Reduction: Omit enclosed trigger loop; single trigger stroke.
Construction reference: paintbrush: broad tool head versus narrow handle
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ad00d24-fd59-47d1-b4d4-68699424443b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/airbrush_8ad00d24-fd59-47d1-b4d4-68699424443b.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/airbrush_8ad00d24-fd59-47d1-b4d4-68699424443b.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/airbrush_8ad00d24-fd59-47d1-b4d4-68699424443b.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'airbrush-spray-gun-batch-013-13'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('airbrush', 'spray', 'paint', 'cup', 'trigger', 'tool')

    def build(self):
        self.add_polyline('barrel', (4, 24), (12, 20), (40, 20), (44, 24), (40, 28), (32, 28), (36, 40), (26, 40), (22, 28), (12, 28), closed=True)
        self.add_polyline('cup', (22, 20), (18, 8), (34, 8), (30, 20), closed=False)
        self.relate("connect", 'barrel', 'cup')
