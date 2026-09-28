"""Rounded raised index touches a task card. One text line replaces the crowded check, and a smooth hand back replaces the angular thumb.
Lucide hand, crown and user/laptop construction; independently revised on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bcb05217-5ed3-5a98-9ddf-d3ddae2b3497'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-selecting-task/20260927T075452Z-thuan-mac-1/reference/workflow task management_bcb05217-5ed3-5a98-9ddf-d3ddae2b3497.svg'
AUTHOR = 'gpt-6'

class HandSelectingTask(Solo48):
    icon_id = 'hand-selecting-task'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('hand', 'task', 'check', 'selection', 'interface', 'completion')

    def build(self) -> None:
        self.add_polyline('card', (22, 24), (6, 24), (6, 6), (42, 6), (42, 24), (22, 24), closed=False)
        self.add_polyline('task-check', (14, 14), (16, 16), (23, 14))
        self.add_arc('finger-tip', (18, 28), (26, 28), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('finger-right', (26, 28), (26, 33))
        self.add_arc('hand-back', (26, 33), (33, 40), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_polyline('wrist', (33, 40), (33, 42), (18, 42), (18, 28), closed=False)
        self.relate("connect", 'finger-tip', 'finger-right')
        self.relate("connect", 'finger-right', 'hand-back')
        self.relate("connect", 'hand-back', 'wrist')
        self.relate("connect", 'wrist', 'finger-tip')
        self.relate("connect", 'finger-tip', 'card')
