"""Carplay connect (mobile), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '866bf46c-f592-44ca-a741-a14f2c7f0394'
SOURCE_PATH = 'icons-json/mobile/carplay connect_866bf46c-f592-44ca-a741-a14f2c7f0394.json'
AUTHOR = 'json_to_solo'

class CarplayConnect(Solo48):
    icon_id = 'carplay-connect'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('carplay', 'connect', 'mobile')

    def build(self):
        self.add_line('e0', (19, 13), (33, 24))
        self.add_line('e1', (33, 24), (19, 35))
        self.add_line('e2', (19, 35), (19, 13))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
