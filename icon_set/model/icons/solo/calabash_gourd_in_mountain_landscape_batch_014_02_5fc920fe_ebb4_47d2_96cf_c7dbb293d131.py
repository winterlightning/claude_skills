"""Calabash Gourd and Mountains.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Double-lobed gourd foreground with two mountain slopes behind.
Reduction: Drop cloud and mountain decoration; preserve gourd and landscape.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5fc920fe-ebb4-47d2-96cf-c7dbb293d131'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/double ninth festival calabash_5fc920fe-ebb4-47d2-96cf-c7dbb293d131.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/double ninth festival calabash_5fc920fe-ebb4-47d2-96cf-c7dbb293d131.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/double ninth festival calabash_5fc920fe-ebb4-47d2-96cf-c7dbb293d131.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'calabash-gourd-in-mountain-landscape-batch-014-02'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('gourd', 'calabash', 'mountain', 'cloud', 'landscape', 'festival')

    def build(self):
        self.add_bezier('gourd-1', (34, 18), ((28, 18), (28, 23), (30, 26)))
        self.add_bezier('gourd-2', (30, 26), ((24, 30), (26, 42), (34, 42)))
        self.add_bezier('gourd-3', (34, 42), ((40, 42), (42, 38), (42, 34)))
        self.add_bezier('gourd-4', (42, 34), ((42, 30), (40, 28), (38, 26)))
        self.add_bezier('gourd-5', (38, 26), ((40, 23), (40, 18), (34, 18)))
        self.add_contour('gourd', 'gourd-1', 'gourd-2', 'gourd-3', 'gourd-4', 'gourd-5', closed=True)
        self.add_polyline('mountains', (6, 32), (12, 16), (18, 24), (24, 6), (36, 6), closed=False)
