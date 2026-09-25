"""Strong Flexing Arm with Leaf.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Flexed arm with clenched fist and a broad inner muscle curve.
Reduction: Open the inner pointed oval to a single muscle contour. Human-reference consulted for sparse anatomy.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4100bb0-e557-5776-84f3-12d5a0ad1a62'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/massage muscle_f4100bb0-e557-5776-84f3-12d5a0ad1a62.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage muscle_f4100bb0-e557-5776-84f3-12d5a0ad1a62.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/massage muscle_f4100bb0-e557-5776-84f3-12d5a0ad1a62.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'flexed-arm-with-inner-muscle-shape-batch-012-14'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('arm', 'bicep', 'muscle', 'flex', 'fist', 'anatomy')

    def build(self):
        self.add_bezier('arm-1', (44, 24), ((36, 19), (28, 21), (24, 28)))
        self.add_line('arm-2', (24, 28), (20, 18))
        self.add_line('arm-3', (20, 18), (26, 16))
        self.add_line('arm-4', (26, 16), (24, 8))
        self.add_line('arm-5', (24, 8), (14, 8))
        self.add_bezier('arm-6', (14, 8), ((10, 18), (4, 30), (4, 34)))
        self.add_bezier('arm-7', (4, 34), ((4, 40), (13, 40), (24, 40)))
        self.add_bezier('arm-8', (24, 40), ((34, 40), (41, 38), (44, 36)))
        self.add_contour('arm', 'arm-1', 'arm-2', 'arm-3', 'arm-4', 'arm-5', 'arm-6', 'arm-7', 'arm-8', closed=False)
        self.add_bezier('muscle-1', (24, 28), ((28, 32), (34, 32), (38, 28)))
        self.add_contour('muscle', 'muscle-1', closed=False)
        self.relate("connect", 'arm', 'muscle')
