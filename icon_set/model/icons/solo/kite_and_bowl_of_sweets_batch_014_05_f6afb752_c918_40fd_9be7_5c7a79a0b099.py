"""Kite and Bowl of Sweets.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Kite upper-right and shallow sweet bowl lower-left.
Reduction: Retain one large sweet, omit spars and tail bow for spacing.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6afb752-c918-40fd-9be7-5c7a79a0b099'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/makara sankranti_f6afb752-c918-40fd-9be7-5c7a79a0b099.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/makara sankranti_f6afb752-c918-40fd-9be7-5c7a79a0b099.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/makara sankranti_f6afb752-c918-40fd-9be7-5c7a79a0b099.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'kite-and-bowl-of-sweets-batch-014-05'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('kite', 'sweets', 'bowl', 'festival', 'sankranti', 'tail')

    def build(self):
        self.add_polyline('kite', (32, 6), (42, 16), (32, 28), (22, 16), closed=True)
        self.add_bezier('tail-1', (32, 28), ((30, 34), (38, 34), (38, 42)))
        self.add_contour('tail', 'tail-1', closed=False)
        self.relate("connect", 'kite', 'tail')
        self.add_arc('sweet-1', (6, 32), (22, 32), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('sweet', 'sweet-1', closed=False)
        self.add_bezier('bowl-1', (6, 32), ((6, 38), (10, 42), (14, 42)))
        self.add_bezier('bowl-2', (14, 42), ((18, 42), (22, 38), (22, 32)))
        self.add_line('bowl-close', (22, 32), (6, 32))
        self.add_contour('bowl', 'bowl-1', 'bowl-2', 'bowl-close', closed=True)
        self.relate("connect", 'sweet', 'bowl')
