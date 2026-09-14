"""Usb type c (electronics), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0a14e2a-4419-5c4d-bceb-f564e7b8279f'
SOURCE_PATH = 'icons-json/electronics/usb type c_c0a14e2a-4419-5c4d-bceb-f564e7b8279f.json'
AUTHOR = 'json_to_solo'

class UsbTypeCElectronics(Solo48):
    icon_id = 'usb-type-c-electronics'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('usb', 'type', 'c', 'electronics')

    def build(self):
        self.add_line('sym-e0', (14, 24), (34, 24))
        self.add_bezier('sym-e1', (4, 24), ((4, 24.308), (4, 24.698), (4, 25)))
        self.add_bezier('sym-e2', (4, 25), ((4, 32.14), (6.864, 38.7), (10, 40)))
        self.add_bezier('sym-e3', (10, 40), ((10.518, 40), (10.439, 40), (11, 40)))
        self.add_bezier('sym-e4', (11, 40), ((11.739, 40), (13.313, 39.955), (14, 40)))
        self.add_bezier('sym-e5', (14, 40), ((14.464, 40), (14.536, 40), (15, 40)))
        self.add_bezier('sym-e6', (15, 40), ((15.255, 40), (15.745, 40), (16, 40)))
        self.add_line('sym-e7', (16, 40), (37, 40))
        self.add_bezier('sym-e8', (37, 40), ((37.282, 40), (37.709, 40), (38, 40)))
        self.add_bezier('sym-e9', (38, 40), ((41.436, 40), (44, 32.32), (44, 25)))
        self.add_bezier('sym-e10', (44, 25), ((44, 24.7), (43.991, 24.32), (44, 24)))
        self.add_bezier('sym-e11', (44, 24), ((44, 23.993), (44, 24.007), (44, 24)))
        self.add_bezier('sym-e12', (44, 24), ((44, 23.993), (44, 24.007), (44, 24)))
        self.add_bezier('sym-e13', (44, 24), ((43.991, 23.68), (44, 23.3), (44, 23)))
        self.add_bezier('sym-e14', (44, 23), ((44, 15.68), (41.436, 8), (38, 8)))
        self.add_bezier('sym-e15', (38, 8), ((37.709, 8), (37.282, 8), (37, 8)))
        self.add_line('sym-e16', (37, 8), (16, 8))
        self.add_bezier('sym-e17', (16, 8), ((15.745, 8), (15.255, 8), (15, 8)))
        self.add_bezier('sym-e18', (15, 8), ((14.536, 8), (14.464, 8), (14, 8)))
        self.add_bezier('sym-e19', (14, 8), ((13.313, 8.045), (11.739, 8), (11, 8)))
        self.add_bezier('sym-e20', (11, 8), ((10.439, 8), (10.518, 8), (10, 8)))
        self.add_bezier('sym-e21', (10, 8), ((6.864, 9.3), (4, 15.86), (4, 23)))
        self.add_bezier('sym-e22', (4, 23), ((4, 23.302), (4, 23.692), (4, 24)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
