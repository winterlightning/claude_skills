"""Ir (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0f887c9-5e62-4314-84c5-4a695ee10767'
SOURCE_PATH = 'icons-json/symbol/ir (text u)_f0f887c9-5e62-4314-84c5-4a695ee10767.json'
AUTHOR = 'json_to_solo'

class IrTextU(Solo48):
    icon_id = 'ir-text-u'
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
        self.add_arc('e5', (40, 13), (30, 17), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c4', 'c3')
