"""Hand Holding a Mask.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Costume mask above a supporting gripping hand.
Reduction: Eye holes become short slanted strokes; omit finger creases. Human reference consulted for sparse hand contour.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5521723a-f61f-58b0-9d3b-7bb857fa845d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/cosplay_5521723a-f61f-58b0-9d3b-7bb857fa845d.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/cosplay_5521723a-f61f-58b0-9d3b-7bb857fa845d.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/cosplay_5521723a-f61f-58b0-9d3b-7bb857fa845d.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'hand-holding-mask-batch-013-11'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('hand', 'mask', 'costume', 'cosplay', 'holding', 'face')

    def build(self):
        self.add_line('mask-1', (14, 28), (14, 6))
        self.add_bezier('mask-2', (14, 6), ((24, 9), (32, 9), (42, 6)))
        self.add_line('mask-3', (42, 6), (42, 24))
        self.add_bezier('mask-4', (42, 24), ((42, 34), (36, 36), (24, 36)))
        self.add_contour('mask', 'mask-1', 'mask-2', 'mask-3', 'mask-4', closed=False)
        self.add_dot('eye-left', (23, 17))
        self.add_line('eye-right', (32, 18), (33, 17))
        self.add_line('hand-1', (6, 42), (6, 30))
        self.add_bezier('hand-2', (6, 30), ((6, 25), (12, 24), (14, 28)))
        self.add_line('hand-3', (14, 28), (24, 28))
        self.add_bezier('hand-4', (24, 28), ((30, 28), (30, 36), (24, 36)))
        self.add_line('hand-5', (24, 36), (20, 36))
        self.add_line('hand-6', (20, 36), (20, 42))
        self.add_contour('hand', 'hand-1', 'hand-2', 'hand-3', 'hand-4', 'hand-5', 'hand-6', closed=False)
        self.relate("connect", 'mask', 'hand')
