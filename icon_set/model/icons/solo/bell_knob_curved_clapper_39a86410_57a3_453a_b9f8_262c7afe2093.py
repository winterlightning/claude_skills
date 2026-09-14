"""Bell with a small top knob and curved clapper. Lucide bell informs the dome and flared lip. Knob reduced to one round mark; source distinctions preserved.

SOLO48 VRECT_L, live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39a86410-57a3-453a-b9f8-262c7afe2093'
SOURCE_PATH = 'pictographic-primitives/symbol/ring_39a86410-57a3-453a-b9f8-262c7afe2093.svg'
AUTHOR = 'gpt-6'


class BellKnobCurvedClapper(Solo48):
    icon_id = 'bell-knob-curved-clapper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('bell', 'notification', 'alert', 'alarm', 'reminder', 'ring', 'sound', 'news')

    def build(self) -> None:

        self.add_dot('knob',(24,6))
        self.add_arc('dome',(12,24),(36,24),radius_x=12,radius_y=10)
        self.add_line('right-side',(36,24),(36,26))
        self.add_arc('right-flare',(36,26),(40,32),radius_x=7,sweep=False)
        self.add_line('lip',(40,32),(8,32))
        self.add_arc('left-flare',(8,32),(12,26),radius_x=7,sweep=False)
        self.add_line('left-side',(12,26),(12,24))
        self.add_contour('bell','dome','right-side','right-flare','lip','left-flare','left-side',closed=True)
        self.add_arc('clapper',(20,42),(28,42),radius_x=4,radius_y=2,sweep=False)
