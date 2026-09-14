"""Usb type c (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e1', (4, 24), (4, 25), radius_x=75)
        self.add_arc('sym-e2-1', (4, 25), (6, 35), radius_x=26, sweep=False)
        self.add_arc('sym-e2-2', (6, 35), (10, 40), radius_x=8, sweep=False)
        self.add_line('sym-e3', (10, 40), (11, 40))
        self.add_arc('sym-e4', (11, 40), (14, 40), radius_x=21)
        self.add_line('sym-e5', (14, 40), (15, 40))
        self.add_line('sym-e6', (15, 40), (16, 40))
        self.add_line('sym-e7', (16, 40), (37, 40))
        self.add_line('sym-e8', (37, 40), (38, 40))
        self.add_arc('sym-e9-1', (38, 40), (42, 35), radius_x=6, sweep=False)
        self.add_arc('sym-e9-2', (42, 35), (44, 25), radius_x=28, sweep=False)
        self.add_arc('sym-e10', (44, 25), (44, 24), radius_x=9)
        self.add_arc('sym-e13', (44, 24), (44, 23), radius_x=9)
        self.add_arc('sym-e14-1', (44, 23), (42, 13), radius_x=28, sweep=False)
        self.add_arc('sym-e14-2', (42, 13), (38, 8), radius_x=6, sweep=False)
        self.add_line('sym-e15', (38, 8), (37, 8))
        self.add_line('sym-e16', (37, 8), (16, 8))
        self.add_line('sym-e17', (16, 8), (15, 8))
        self.add_line('sym-e18', (15, 8), (14, 8))
        self.add_arc('sym-e19', (14, 8), (11, 8), radius_x=21)
        self.add_line('sym-e20', (11, 8), (10, 8))
        self.add_arc('sym-e21-1', (10, 8), (6, 13), radius_x=9, sweep=False)
        self.add_arc('sym-e21-2', (6, 13), (4, 23), radius_x=26, sweep=False)
        self.add_arc('sym-e22', (4, 23), (4, 24), radius_x=70)
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2-1', 'sym-e2-2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9-1', 'sym-e9-2', 'sym-e10', 'sym-e13', 'sym-e14-1', 'sym-e14-2', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21-1', 'sym-e21-2', 'sym-e22', closed=True)
