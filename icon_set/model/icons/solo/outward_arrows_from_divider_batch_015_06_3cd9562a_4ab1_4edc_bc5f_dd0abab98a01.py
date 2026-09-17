"""Horizontal Expansion Arrows.

SOLO48 visible bounds: (2, 8, 46, 40). Centerline extremes: (4, 10, 44, 38).

Symbol plan: Two outward arrows separated by a central vertical divider.
Reduction: Use mirrored arrowheads and 8-unit gaps to divider.
Construction reference: move-horizontal: matched arrowheads on a shared axis
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cd9562a-4ab1-4edc-bc5f-dd0abab98a01'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/expand horizontal 2_3cd9562a-4ab1-4edc-bc5f-dd0abab98a01.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/expand horizontal 2_3cd9562a-4ab1-4edc-bc5f-dd0abab98a01.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/expand horizontal 2_3cd9562a-4ab1-4edc-bc5f-dd0abab98a01.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'outward-arrows-from-divider-batch-015-06'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('expand', 'outward', 'arrows', 'divider', 'horizontal', 'resize')

    def build(self):
        self.add_line('divider', (24, 10), (24, 38))
        self.add_polyline('left-head', (12, 16), (4, 24), (12, 32), closed=False)
        self.add_line('left-shaft', (4, 24), (16, 24))
        self.relate("connect", 'left-head', 'left-shaft')
        self.add_polyline('right-head', (36, 16), (44, 24), (36, 32), closed=False)
        self.add_line('right-shaft', (44, 24), (32, 24))
        self.relate("connect", 'right-head', 'right-shaft')
