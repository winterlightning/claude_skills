"""Contact Form with Checkmark Button -- batch-002 r2 generation.

Subject: a contact form of two stacked entry fields with a check-mark submit
control below them at the left.

Plan: the two fields are one repeated definition: a full-width bar 8 tall on
a 16-unit step. Square corners with round joins let neighbours sit on the
exact 8-unit straight minimum. The submit control is a left-aligned check
mark (legs at 45 degrees) whose apex is exactly 8 below the second field.
Keyshape VRECT_L; centerline box (8,4)-(40,44).
Reduction: the reference draws the check inside a rounded button. Two fields
and a button that encloses a check need about 52 units of height with 4-unit
clearances; VRECT_L gives 40. The button outline is dropped and the check
itself is the submit control. Capsule fields were also rendered; they need a
9-unit gap from their curved ends, which shrank the check to 6 tall. The
square-cornered version was kept.
Construction reference: Lucide form (stacked entry bars on an even step) and
check (two 45-degree legs), re-derived on the SOLO48 grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import polyline, rounded_rect

SOURCE_ICON_ID = 'f716840b-dc67-49c0-9cb4-458bcfde5a4f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/lead capture_f716840b-dc67-49c0-9cb4-458bcfde5a4f.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/lead capture_f716840b-dc67-49c0-9cb4-458bcfde5a4f.svg'
AUTHOR = 'claude-opus-5'

LEFT, TOP, RIGHT, BOTTOM = 8, 4, 40, 44
FIELD_HEIGHT, FIELD_STEP, FIELD_COUNT = 8, 16, 2
CHECK_LEFT, CHECK_SHORT, CHECK_LONG = 12, 4, 8


class ContactFormWithCheckmarkButtonBatch002R2(Solo48):
    icon_id = 'contact-form-with-checkmark-button-batch-002-r2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/business'
    aliases = ('lead-capture', 'contact-form', 'sign-up-form')
    keywords = ('form', 'contact', 'lead', 'capture', 'fields', 'submit', 'check', 'signup')

    def build(self) -> None:
        for i in range(FIELD_COUNT):
            top = TOP + i * FIELD_STEP
            rounded_rect(self, f'field-{i + 1}', LEFT, top, RIGHT, top + FIELD_HEIGHT, 0)
        bottom_of_check = BOTTOM
        corner = (CHECK_LEFT + CHECK_SHORT, bottom_of_check)
        polyline(self, 'check',
                 (CHECK_LEFT, bottom_of_check - CHECK_SHORT), corner,
                 (corner[0] + CHECK_LONG, bottom_of_check - CHECK_LONG))
