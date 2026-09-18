"""Professional Business Briefcase -- batch-002 r2 generation.

Subject: a wide briefcase with a raised rounded handle, a flap seam across
the body and a short clasp dropping from the seam's midpoint.

Plan: symmetric about x=24. The rounded body (radius 4) is split at the
handle feet and at both seam ends. The handle is one open run with radius-4
shoulders whose feet share the body's top nodes. The seam is a full-width
chord 8 below the top edge (straight to straight). The clasp shares the
seam's midpoint node.
Keyshape HRECT_L; centerline box (4,8)-(44,40).
Reduction: none; handle, body, seam and clasp are all kept.
Construction reference: Lucide briefcase (rounded body with a separate
radiused handle), re-derived on the SOLO48 grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import path, polyline, rounded_rect

SOURCE_ICON_ID = 'c246de89-264c-46cf-bdc1-2edde954a7a7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/briefcase_c246de89-264c-46cf-bdc1-2edde954a7a7.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/briefcase_c246de89-264c-46cf-bdc1-2edde954a7a7.svg'
AUTHOR = 'claude-opus-5'

AXIS = 24
LEFT, RIGHT, HANDLE_TOP, BODY_TOP, BOTTOM, RADIUS = 4, 44, 8, 16, 40, 4
HANDLE_HALF = 6
SEAM_Y, CLASP_BOTTOM = BODY_TOP + 8, 30


class ProfessionalBusinessBriefcaseBatch002R2(Solo48):
    icon_id = 'professional-business-briefcase-batch-002-r2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/business'
    aliases = ('briefcase', 'business-bag', 'portfolio')
    keywords = ('briefcase', 'business', 'case', 'bag', 'handle', 'work', 'job', 'office')

    def build(self) -> None:
        hl, hr = AXIS - HANDLE_HALF, AXIS + HANDLE_HALF
        seam_left, seam_right, seam_mid = (LEFT, SEAM_Y), (RIGHT, SEAM_Y), (AXIS, SEAM_Y)
        rounded_rect(self, 'body', LEFT, BODY_TOP, RIGHT, BOTTOM, RADIUS,
                     nodes=((hl, BODY_TOP), (hr, BODY_TOP), seam_left, seam_right))
        path(self, 'handle', (hl, BODY_TOP),
             ('L', (hl, HANDLE_TOP + RADIUS)),
             ('A', (hl + RADIUS, HANDLE_TOP), RADIUS, RADIUS, True),
             ('L', (hr - RADIUS, HANDLE_TOP)),
             ('A', (hr, HANDLE_TOP + RADIUS), RADIUS, RADIUS, True),
             ('L', (hr, BODY_TOP)))
        polyline(self, 'seam', seam_left, seam_right, nodes=(seam_mid,))
        self.add_line('clasp', seam_mid, (AXIS, CLASP_BOTTOM))
        self.relate('connect', 'body', 'handle')
        self.relate('connect', 'body', 'seam')
        self.relate('connect', 'seam', 'clasp')
