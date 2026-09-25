"""Simple Open Eye Shape.

SOLO48 visible bounds: (2, 8, 46, 40). Centerline extremes: (4, 10, 44, 38).

Symbol plan: Empty almond contour mirrored across both center axes.
Reduction: No iris or pupil, as in this saved reference.
Construction reference: eye: paired upper/lower curves; preserve empty source
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ae6185e-ac20-41e7-9b72-2e0f5c114690'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/eye_6ae6185e-ac20-41e7-9b72-2e0f5c114690.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/eye_6ae6185e-ac20-41e7-9b72-2e0f5c114690.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/eye_6ae6185e-ac20-41e7-9b72-2e0f5c114690.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'open-eye-outline-batch-012-13'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('eye', 'outline', 'almond', 'vision', 'shape', 'open')

    def build(self):
        self.add_bezier('eye-1', (4, 24), ((10, 15), (17, 10), (24, 10)))
        self.add_bezier('eye-2', (24, 10), ((31, 10), (38, 15), (44, 24)))
        self.add_bezier('eye-3', (44, 24), ((38, 33), (31, 38), (24, 38)))
        self.add_bezier('eye-4', (24, 38), ((17, 38), (10, 33), (4, 24)))
        self.add_contour('eye', 'eye-1', 'eye-2', 'eye-3', 'eye-4', closed=True)
