"""Three upright pointed drill bits; one flute slash per bit replaces the dense spiral pattern."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d4d9cd7-decb-4e86-b74a-d70f70e17bcb'
SOURCE_PATH = 'pictographic-primitives/tools/hardware drill carbide_3d4d9cd7-decb-4e86-b74a-d70f70e17bcb.svg'
AUTHOR = 'gpt-6'

class ThreeDrillBits(Solo48):
    icon_id = 'three-drill-bits'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('drill bit', 'drill', 'bits', 'carbide', 'twist', 'boring', 'hardware', 'set')

    def build(self) -> None:
        for j,x in enumerate((4,20,36)):
            n='bit'+str(j)
            self.add_polyline(n,(x,40),(x,16),(x+4,8),(x+8,16),(x+8,40),closed=True)
            self.add_line(n+'-flute',(x,30),(x+8,20))
            self.relate('connect',n,n+'-flute')
