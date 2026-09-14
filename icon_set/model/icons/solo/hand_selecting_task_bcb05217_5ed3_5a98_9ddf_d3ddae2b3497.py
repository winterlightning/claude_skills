"""An upward-pointing index finger touches a circular checked control inside a horizontal task card. Two text lines sit to the right, while the bent hand and short cuff extend below the card.
Lucide pointer, workflow card and check construction. Raised index meets the check on a task card. Circular control border and second text line omitted for clearance; hand overlaps the card edge naturally.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bcb05217-5ed3-5a98-9ddf-d3ddae2b3497'
SOURCE_PATH = 'pictographic-primitives/work/workflow task management_bcb05217-5ed3-5a98-9ddf-d3ddae2b3497.svg'
AUTHOR = 'gpt-6'


class HandSelectingTask(Solo48):
    icon_id = 'hand-selecting-task'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('hand', 'task', 'check', 'selection', 'interface', 'completion')

    def build(self) -> None:
        self.add_polyline('card', (6, 14), (6, 6), (42, 6), (42, 26), (32, 26), closed=False)
        self.add_polyline('check', (14, 17), (18, 21), (23, 14), closed=False)
        self.add_line('text', (32, 15), (34, 15))
        self.add_polyline('hand', (18, 21), (18, 34), (6, 24), (6, 36), (12, 42), (28, 42), (32, 34), (32, 26), closed=False)
        self.relate("connect", 'hand', 'check')
        self.relate("connect", 'hand', 'card')
