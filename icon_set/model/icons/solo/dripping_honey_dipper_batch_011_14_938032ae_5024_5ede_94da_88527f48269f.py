"""Honey Dipper with Drip.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Diagonal dipper with three connected broad head ridges and a drop.
Reduction: Represent handle with one stroke and drip with open teardrop.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '938032ae-5024-5ede-94da-88527f48269f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/honey_938032ae-5024-5ede-94da-88527f48269f.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/honey_938032ae-5024-5ede-94da-88527f48269f.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/honey_938032ae-5024-5ede-94da-88527f48269f.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'dripping-honey-dipper-batch-011-14'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('honey', 'dipper', 'drip', 'sweet', 'food', 'utensil')

    def build(self):
        self.add_line('handle', (28, 14), (42, 6))
        self.add_polyline('head-a', (10, 20), (26, 36), closed=False)
        self.add_polyline('head-b', (16, 14), (32, 30), closed=False)
        self.add_polyline('head-c', (22, 8), (38, 24), closed=False)
        self.add_line('spine', (16, 26), (28, 14))
        self.relate("connect", 'spine', 'head-a')
        self.relate("connect", 'spine', 'head-b')
        self.relate("connect", 'spine', 'head-c')
        self.relate("connect", 'handle', 'spine')
        self.relate("connect", 'handle', 'head-c')
        self.relate("connect", 'spine', 'head-c')
        self.add_bezier('drop-1', (10, 34), ((6, 38), (6, 38), (6, 38)))
        self.add_arc('drop-2', (6, 38), (14, 38), radius_x=4, radius_y=4, sweep=False)
        self.add_bezier('drop-3', (14, 38), ((14, 38), (12, 36), (10, 34)))
        self.add_contour('drop', 'drop-1', 'drop-2', 'drop-3', closed=True)
