"""End point reversed triangle (devices), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d07c79d-33b8-4d96-a76c-208a00c1fb9a'
SOURCE_PATH = 'icons-json/devices/end point reversed triangle_0d07c79d-33b8-4d96-a76c-208a00c1fb9a.json'
AUTHOR = 'json_to_solo'

class EndPointReversedTriangleDevices(Solo48):
    icon_id = 'end-point-reversed-triangle-devices'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ()
    keywords = ('end', 'point', 'reversed', 'triangle', 'devices')

    def build(self):
        self.add_line('e0', (4, 24), (30, 24))
        self.add_line('e1', (30, 24), (44, 8))
        self.add_line('e2', (44, 8), (44, 40))
        self.add_line('e3', (44, 40), (30, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
