"""Rounded raised index touches a task card. One text line replaces the crowded check, and a smooth hand back replaces the angular thumb.
Lucide hand, crown and user/laptop construction; independently revised on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bcb05217-5ed3-5a98-9ddf-d3ddae2b3497'
SOURCE_PATH = 'pictographic-primitives/work/workflow task management_bcb05217-5ed3-5a98-9ddf-d3ddae2b3497.svg'
AUTHOR = 'gpt-6'

class HandSelectingTask(Solo48):
    icon_id = 'hand-selecting-task'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    aliases = ()
    keywords = ('hand', 'task', 'check', 'selection', 'interface', 'completion')

    def build(self) -> None:
        self.add_polyline('card', (22, 24), (6, 24), (6, 6), (42, 6), (42, 24), (22, 24), closed=False)
        self.add_line('task-line', (14, 15), (26, 15))
        self.add_arc('finger-tip', (18, 28), (26, 28), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('finger-right', (26, 28), (26, 30))
        self.add_arc('hand-back', (26, 30), (36, 40), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_polyline('wrist', (36, 40), (36, 42), (18, 42), (18, 28), closed=False)
        self.relate("connect", 'finger-tip', 'finger-right')
        self.relate("connect", 'finger-right', 'hand-back')
        self.relate("connect", 'hand-back', 'wrist')
        self.relate("connect", 'wrist', 'finger-tip')
        self.relate("connect", 'finger-tip', 'card')
