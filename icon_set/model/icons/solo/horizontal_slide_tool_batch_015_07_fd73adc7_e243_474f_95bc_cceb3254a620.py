"""Horizontal Slide Tool.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Horizontal double arrow through two detached rectangular brackets.
Reduction: Open large side gaps so arrow and brackets remain clear.
Construction reference: move-horizontal: matched arrowheads
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd73adc7-e243-474f-95bc-cceb3254a620'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/slide tool_fd73adc7-e243-474f-95bc-cceb3254a620.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/slide tool_fd73adc7-e243-474f-95bc-cceb3254a620.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/slide tool_fd73adc7-e243-474f-95bc-cceb3254a620.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'horizontal-slide-tool-batch-015-07'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('slide', 'tool', 'arrow', 'edit', 'horizontal', 'rectangle')

    def build(self):
        self.add_line('shaft', (6, 24), (42, 24))
        self.add_polyline('left', (14, 16), (6, 24), (14, 32), closed=False)
        self.add_polyline('right', (34, 16), (42, 24), (34, 32), closed=False)
        self.relate("connect", 'shaft', 'left')
        self.relate("connect", 'shaft', 'right')
        self.add_polyline('top', (20, 10), (20, 6), (28, 6), (28, 10), closed=False)
        self.add_polyline('bottom', (20, 38), (20, 42), (28, 42), (28, 38), closed=False)
