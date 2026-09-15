"""A C-frame opening left with screw and two T-handles; double wall omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cc790d6-4532-4db2-ad90-b5debf2d073c'
SOURCE_PATH = 'pictographic-primitives/tools/clamp press_2cc790d6-4532-4db2-ad90-b5debf2d073c.svg'
AUTHOR = 'gpt-6'

class CClamp(Solo48):
    icon_id = 'c-clamp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('clamp', 'c-clamp', 'press', 'vise', 'hold', 'woodworking', 'workshop', 'tool')

    def build(self) -> None:
        self.add_polyline('frame',(8,14),(42,14),(42,34),(8,34))
        for name,y,end in [('upper',6,14),('lower',42,34)]:
            self.add_line(name+'-screw',(20,y),(20,end))
            self.add_line(name+'-handle',(12,y),(28,y))
            self.relate('connect',name+'-screw','frame')
            self.relate('connect',name+'-screw',name+'-handle')
        self.add_line('pressure-screw',(6,24),(30,24))
