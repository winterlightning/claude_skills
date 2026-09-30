"""Endless Infinity Symbol.

SOLO48 visible bounds: (2, 8, 46, 40). Centerline extremes: (4, 10, 44, 38).

Symbol plan: Continuous figure-eight with equal lobes and smooth crossing.
Reduction: Use an unbroken center crossing in place of sub-clearance source breaks.
Construction reference: infinity: paired lobes and smooth cubic crossing
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1739e39c-1f28-5f58-b32d-18e847e5acf6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/loop_1739e39c-1f28-5f58-b32d-18e847e5acf6.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/loop_1739e39c-1f28-5f58-b32d-18e847e5acf6.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/loop_1739e39c-1f28-5f58-b32d-18e847e5acf6.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'open-infinity-loop-batch-015-02'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('infinity', 'loop', 'endless', 'continuous', 'symbol', 'interface')

    def build(self):
        self.add_bezier('loop-1', (14, 10), ((26, 10), (22, 38), (34, 38)))
        self.add_bezier('loop-2', (34, 38), ((40, 38), (44, 32), (44, 24)))
        self.add_bezier('loop-3', (44, 24), ((44, 16), (40, 10), (34, 10)))
        self.add_bezier('loop-4', (34, 10), ((22, 10), (26, 38), (14, 38)))
        self.add_bezier('loop-5', (14, 38), ((8, 38), (4, 32), (4, 24)))
        self.add_bezier('loop-6', (4, 24), ((4, 16), (8, 10), (14, 10)))
        self.add_contour('loop', 'loop-1', 'loop-2', 'loop-3', 'loop-4', 'loop-5', 'loop-6', closed=True)
