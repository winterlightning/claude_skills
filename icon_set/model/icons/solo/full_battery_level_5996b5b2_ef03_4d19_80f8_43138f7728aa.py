"""Full Battery Level. Horizontal battery with integral right terminal and repeated full-charge bars. Three evenly spaced bars replace five to preserve 8-unit centerline gaps. Symmetric about y=24. Lucide battery-full contributes repeated vertical charge marks; source contributes attached terminal. Envelope (4,10)-(44,38)."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '5996b5b2-ef03-4d19-80f8-43138f7728aa'
SOURCE_PATH = 'pictographic-primitives/devices/charging battery almost full 1_5996b5b2-ef03-4d19-80f8-43138f7728aa.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'full-battery-level'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'devices'
    aliases = ('Full Battery Level',)
    keywords = ('full', 'battery', 'level')
    def build(self):
        self.add_polyline('case',(4,10),(36,10),(36,20),(44,20),(44,28),(36,28),(36,38),(4,38),closed=True)
        for i,x in enumerate((12,20,28)):
            self.add_line(f'charge-{i}',(x,18),(x,30))
