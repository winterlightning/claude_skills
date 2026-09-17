"""Human Foot with Two Dots.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Side-view foot with raised ankle, rounded heel/toe and two detached marks.
Reduction: Preserve both ambiguous dots below the foot. Human-reference consulted; no detached head applies.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcbbd8ae-d89f-5e3c-838f-3a4b9ef6294a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/specialty feet_dcbbd8ae-d89f-5e3c-838f-3a4b9ef6294a.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty feet_dcbbd8ae-d89f-5e3c-838f-3a4b9ef6294a.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/specialty feet_dcbbd8ae-d89f-5e3c-838f-3a4b9ef6294a.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'foot-in-side-view-batch-012-09'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('foot', 'ankle', 'heel', 'toe', 'anatomy', 'side')

    def build(self):
        self.add_line('foot-1', (8, 8), (8, 22))
        self.add_bezier('foot-2', (8, 22), ((8, 30), (4, 30), (4, 32)))
        self.add_bezier('foot-3', (4, 32), ((4, 36), (12, 34), (16, 32)))
        self.add_bezier('foot-4', (16, 32), ((24, 28), (30, 32), (38, 32)))
        self.add_bezier('foot-5', (38, 32), ((46, 32), (46, 24), (38, 24)))
        self.add_bezier('foot-6', (38, 24), ((30, 24), (20, 18), (20, 8)))
        self.add_contour('foot', 'foot-1', 'foot-2', 'foot-3', 'foot-4', 'foot-5', 'foot-6', closed=False)
        self.add_dot('mark-left', (21, 40))
        self.add_dot('mark-right', (32, 40))
