"""Microscopic Human Cell Cluster.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Three touching polygonal tissue cells surrounding a center seam.
Reduction: Reduce six cells to three readable polygonal cells with shared tissue walls.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '769dab87-d710-4602-94e8-16b89c223b42'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/human cell_769dab87-d710-4602-94e8-16b89c223b42.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/human cell_769dab87-d710-4602-94e8-16b89c223b42.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/human cell_769dab87-d710-4602-94e8-16b89c223b42.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'microscopic-cell-cluster-batch-012-10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('cell', 'cluster', 'polygon', 'biology', 'microscopic', 'tissue')

    def build(self):
        self.add_polyline('left-cell', (6, 14), (16, 6), (26, 14), (24, 26), (12, 30), (6, 22), closed=True)
        self.add_polyline('right-cell', (26, 14), (36, 6), (42, 16), (40, 30), (24, 26), closed=True)
        self.add_polyline('lower-cell', (12, 30), (24, 26), (40, 30), (34, 42), (20, 42), closed=True)
        self.relate("connect", 'left-cell', 'right-cell')
        self.relate("connect", 'left-cell', 'lower-cell')
        self.relate("connect", 'right-cell', 'lower-cell')
