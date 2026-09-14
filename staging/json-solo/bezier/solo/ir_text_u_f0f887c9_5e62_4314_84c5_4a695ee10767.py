"""Ir (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0f887c9-5e62-4314-84c5-4a695ee10767'
SOURCE_PATH = 'icons-json/symbol/ir (text u)_f0f887c9-5e62-4314-84c5-4a695ee10767.json'
AUTHOR = 'json_to_solo'

class IrTextUSymbol(Solo48):
    icon_id = 'ir-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ir', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (19, 4), (8, 4))
        self.add_line('e1', (13, 4), (13, 27))
        self.add_line('e2', (8, 27), (19, 27))
        self.add_line('e3', (30, 13), (30, 27))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_bezier('e5', (40, 13), ((40, 13), (39.988, 13.082), (39.988, 13.082)), ((39.988, 13.018), (39.631, 12.836), (39.582, 12.8)), ((38.326, 12.036), (36.677, 11.682), (35.089, 12.009)), ((32.16, 12.618), (30.763, 15.036), (30, 17)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c4', 'c3')
