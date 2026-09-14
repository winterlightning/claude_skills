"""Check towing device (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad8d4223-a4f4-42f7-b925-f4a368d15a45'
SOURCE_PATH = 'icons-json/transportation/check towing device_ad8d4223-a4f4-42f7-b925-f4a368d15a45.json'
AUTHOR = 'json_to_solo'

class CheckTowingDeviceTransportation(Solo48):
    icon_id = 'check-towing-device-transportation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('check', 'towing', 'device', 'transportation')

    def build(self):
        self.add_line('e0', (6, 42), (27, 42))
        self.add_line('e1', (34, 35), (34, 22))
        self.add_arc('e2-top', (26, 14), (42, 14), radius_x=8)
        self.add_arc('e2-bottom', (42, 14), (26, 14), radius_x=8)
        self.add_arc('e3', (27, 42), (34, 35), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'e2')
