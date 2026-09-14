"""Text bar (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6fdd803-e318-450c-9350-15e3faf7e238'
SOURCE_PATH = 'icons-json/interface-essential/text bar_a6fdd803-e318-450c-9350-15e3faf7e238.json'
AUTHOR = 'json_to_solo'

class TextBarInterfaceEssential(Solo48):
    icon_id = 'text-bar-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'bar', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 12), (24, 29))
        self.add_line('sym-e1', (24, 29), (24, 37))
        self.add_line('sym-e2', (24, 37), (24, 39))
        self.add_bezier('sym-e3', (24, 12), ((25.904, 8.964), (27.512, 6.473), (33, 5)))
        self.add_bezier('sym-e4', (33, 5), ((34.264, 4.664), (35.592, 4), (37, 4)))
        self.add_bezier('sym-e5', (37, 4), ((37.672, 4), (38.328, 4), (39, 4)))
        self.add_bezier('sym-e6', (39, 4), ((39.176, 4), (39.824, 4), (40, 4)))
        self.add_bezier('sym-e7', (24, 37), ((24.784, 38.145), (25.784, 38.9), (27, 40)))
        self.add_bezier('sym-e8', (27, 40), ((29.176, 41.982), (32.76, 44), (37, 44)))
        self.add_bezier('sym-e9', (37, 44), ((37.704, 44), (38.28, 44), (39, 44)))
        self.add_bezier('sym-e10', (39, 44), ((39.208, 44), (39.792, 44), (40, 44)))
        self.add_line('sym-e11', (32, 29), (24, 29))
        self.add_line('sym-e12', (24, 29), (16, 29))
        self.add_bezier('sym-e13', (24, 12), ((22.096, 8.964), (20.488, 6.473), (15, 5)))
        self.add_bezier('sym-e14', (15, 5), ((13.736, 4.664), (12.408, 4), (11, 4)))
        self.add_bezier('sym-e15', (11, 4), ((10.328, 4), (9.672, 4), (9, 4)))
        self.add_bezier('sym-e16', (9, 4), ((8.824, 4), (8.176, 4), (8, 4)))
        self.add_bezier('sym-e17', (24, 37), ((23.216, 38.145), (22.216, 38.9), (21, 40)))
        self.add_bezier('sym-e18', (21, 40), ((18.824, 41.982), (15.24, 44), (11, 44)))
        self.add_bezier('sym-e19', (11, 44), ((10.296, 44), (9.72, 44), (9, 44)))
        self.add_bezier('sym-e20', (9, 44), ((8.792, 44), (8.208, 44), (8, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c4', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c5', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
