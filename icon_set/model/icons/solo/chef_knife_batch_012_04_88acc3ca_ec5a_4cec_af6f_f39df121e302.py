"""Kitchen Chef Knife.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Diagonal broad blade and rounded handle share heel edge.
Reduction: Single blade cutting curve, no rivets.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88acc3ca-ec5a-4cec-af6f-f39df121e302'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/knife 1_88acc3ca-ec5a-4cec-af6f-f39df121e302.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/knife 1_88acc3ca-ec5a-4cec-af6f-f39df121e302.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/knife 1_88acc3ca-ec5a-4cec-af6f-f39df121e302.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'chef-knife-batch-012-04'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('knife', 'chef', 'blade', 'handle', 'cutlery', 'kitchen')

    def build(self):
        self.add_line('knife-1', (6, 6), (42, 34))
        self.add_line('knife-2', (42, 34), (34, 42))
        self.add_line('knife-3', (34, 42), (26, 34))
        self.add_bezier('knife-4', (26, 34), ((12, 30), (6, 18), (6, 6)))
        self.add_contour('knife', 'knife-1', 'knife-2', 'knife-3', 'knife-4', closed=True)
        self.add_line('heel', (26, 34), (32, 26))
        self.relate("connect", 'knife', 'heel')
