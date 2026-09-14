"""Acrobatic hanging (sports), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f4c8289-e849-53c5-b3f3-f7613d3cd883'
SOURCE_PATH = 'icons-json/sports/acrobatic hanging_0f4c8289-e849-53c5-b3f3-f7613d3cd883.json'
AUTHOR = 'json_to_solo'

class AcrobaticHanging(Solo48):
    icon_id = 'acrobatic-hanging'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('acrobatic', 'hanging', 'sports')

    def build(self):
        self.add_line('e0', (24, 4), (24, 15))
        self.add_arc('e1-top', (8, 29), (40, 29), radius_x=16, radius_y=15)
        self.add_arc('e1-bottom', (40, 29), (8, 29), radius_x=16, radius_y=15)
        self.add_contour('c0', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.relate('connect', 'c0', 'e1')
