"""Text bar (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6fdd803-e318-450c-9350-15e3faf7e238'
SOURCE_PATH = 'icons-json/interface-essential/text bar_a6fdd803-e318-450c-9350-15e3faf7e238.json'
AUTHOR = 'json_to_solo'

class TextBar(Solo48):
    icon_id = 'text-bar'
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
        self.add_arc('sym-e3', (24, 12), (33, 5), radius_x=14)
        self.add_line('sym-e4', (33, 5), (37, 4))
        self.add_line('sym-e5', (37, 4), (39, 4))
        self.add_line('sym-e6', (39, 4), (40, 4))
        self.add_arc('sym-e7', (24, 37), (27, 40), radius_x=16, sweep=False)
        self.add_arc('sym-e8', (27, 40), (37, 44), radius_x=16, sweep=False)
        self.add_line('sym-e9', (37, 44), (39, 44))
        self.add_line('sym-e10', (39, 44), (40, 44))
        self.add_line('sym-e11', (32, 29), (24, 29))
        self.add_line('sym-e12', (24, 29), (16, 29))
        self.add_arc('sym-e13', (24, 12), (15, 5), radius_x=14, sweep=False)
        self.add_line('sym-e14', (15, 5), (11, 4))
        self.add_line('sym-e15', (11, 4), (9, 4))
        self.add_arc('sym-e16', (9, 4), (8, 4), radius_x=11)
        self.add_arc('sym-e17', (24, 37), (21, 40), radius_x=16)
        self.add_arc('sym-e18', (21, 40), (11, 44), radius_x=16)
        self.add_line('sym-e19', (11, 44), (9, 44))
        self.add_line('sym-e20', (9, 44), (8, 44))
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
