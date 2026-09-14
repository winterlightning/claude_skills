"""Led light (electronics), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd59a11ac-73de-457c-8be4-5e247555c2b0'
SOURCE_PATH = 'icons-json/electronics/led light_d59a11ac-73de-457c-8be4-5e247555c2b0.json'
AUTHOR = 'json_to_solo'

class LedLightElectronics(Solo48):
    icon_id = 'led-light-electronics'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('led', 'light', 'electronics')

    def build(self):
        self.add_line('sym-e0', (24, 28), (24, 20))
        self.add_line('sym-e1', (24, 20), (20, 18))
        self.add_line('sym-e2', (8, 28), (10, 28))
        self.add_line('sym-e3', (10, 28), (10, 14))
        self.add_bezier('sym-e4', (10, 14), ((10, 13.218), (10.668, 12.736), (11, 12)))
        self.add_bezier('sym-e5', (11, 12), ((12.76, 8.1), (17.043, 4), (23, 4)))
        self.add_bezier('sym-e6', (23, 4), ((23.123, 4), (23.877, 4), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((24.115, 4), (23.885, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((24.115, 4), (23.885, 4), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((24.123, 4), (24.877, 4), (25, 4)))
        self.add_bezier('sym-e10', (25, 4), ((30.957, 4), (35.24, 8.1), (37, 12)))
        self.add_bezier('sym-e11', (37, 12), ((37.332, 12.736), (38, 13.218), (38, 14)))
        self.add_line('sym-e12', (38, 14), (38, 28))
        self.add_line('sym-e13', (38, 28), (40, 28))
        self.add_line('sym-e14', (17, 44), (17, 28))
        self.add_line('sym-e15', (17, 28), (10, 28))
        self.add_line('sym-e16', (24, 28), (17, 28))
        self.add_line('sym-e17', (28, 18), (24, 20))
        self.add_line('sym-e18', (31, 44), (31, 28))
        self.add_line('sym-e19', (31, 28), (38, 28))
        self.add_line('sym-e20', (24, 28), (31, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c3', 'sym-e16')
        self.add_contour('sym-c4', 'sym-e17')
        self.add_contour('sym-c5', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c6', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c3')
