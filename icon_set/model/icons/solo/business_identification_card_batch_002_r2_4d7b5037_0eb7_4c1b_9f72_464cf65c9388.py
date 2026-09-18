"""Business Identification Card -- batch-002 r2 generation.

Subject: a landscape identification card with a portrait photo box at the
left and two information lines at the right.

Plan: the rounded card (radius 4) owns a square-cornered portrait box and a
two-line series. The box keeps 9 from the rounded card contour, which cannot
certify exactly 8. The lines keep 9 from the card's right edge and exactly 8
from the straight-edged box. The lines share one length and step 8 apart.
Keyshape HRECT_L; centerline box (4,8)-(44,40).
Reduction: none; card, portrait box and both lines are kept.
Construction reference: Lucide id-card (card with a left portrait and right
detail strokes), re-derived on the SOLO48 grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import rounded_rect

SOURCE_ICON_ID = '4d7b5037-0eb7-4c1b-9f72-464cf65c9388'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/business card 3_4d7b5037-0eb7-4c1b-9f72-464cf65c9388.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/business card 3_4d7b5037-0eb7-4c1b-9f72-464cf65c9388.svg'
AUTHOR = 'claude-opus-5'

LEFT, TOP, RIGHT, BOTTOM, RADIUS = 4, 8, 44, 40, 4
PHOTO_LEFT, PHOTO_TOP, PHOTO_RIGHT, PHOTO_BOTTOM = LEFT + 9, TOP + 9, LEFT + 17, BOTTOM - 9
LINE_LEFT, LINE_RIGHT, LINE_Y, LINE_STEP = PHOTO_RIGHT + 8, RIGHT - 9, 20, 8


class BusinessIdentificationCardBatch002R2(Solo48):
    icon_id = 'business-identification-card-batch-002-r2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/business'
    aliases = ('id-card', 'business-card', 'badge')
    keywords = ('card', 'identification', 'id', 'business', 'badge', 'profile', 'contact')

    def build(self) -> None:
        rounded_rect(self, 'card', LEFT, TOP, RIGHT, BOTTOM, RADIUS)
        rounded_rect(self, 'photo', PHOTO_LEFT, PHOTO_TOP, PHOTO_RIGHT, PHOTO_BOTTOM, 0)
        for i in range(2):
            y = LINE_Y + i * LINE_STEP
            self.add_line(f'info-line-{i + 1}', (LINE_LEFT, y), (LINE_RIGHT, y))
