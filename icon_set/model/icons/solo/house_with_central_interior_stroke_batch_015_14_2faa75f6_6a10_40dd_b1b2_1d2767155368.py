"""Minimalist House Symbol.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Peaked house envelope with centered entrance and mirrored walls.
Reduction: Connect eaves cleanly; preserve requested entrance detail.
Construction reference: house: broad roof, simple wall and doorway contours
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2faa75f6-6a10-40dd-b1b2-1d2767155368'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_2faa75f6-6a10-40dd-b1b2-1d2767155368.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_2faa75f6-6a10-40dd-b1b2-1d2767155368.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/house_2faa75f6-6a10-40dd-b1b2-1d2767155368.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'house-with-central-interior-stroke-batch-015-14'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('house', 'home', 'roof', 'building', 'facade', 'outline')

    def build(self):
        self.add_polyline('roof', (6, 24), (10, 20), (24, 6), (38, 20), (42, 24), closed=False)
        self.add_polyline('walls', (10, 20), (10, 42), (24, 42), (38, 42), (38, 20), closed=False)
        self.relate("connect", 'roof', 'walls')
        self.add_line('door', (24, 28), (24, 34))
