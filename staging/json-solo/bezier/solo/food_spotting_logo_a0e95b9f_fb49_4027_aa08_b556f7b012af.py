"""Food spotting logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0e95b9f-fb49-4027-aa08-b556f7b012af'
SOURCE_PATH = 'icons-json/logos/food spotting logo_a0e95b9f-fb49-4027-aa08-b556f7b012af.json'
AUTHOR = 'json_to_solo'

class FoodSpottingLogoLogos(Solo48):
    icon_id = 'food-spotting-logo-logos'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('food', 'spotting', 'logo', 'logos')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (22, 13), ((20.336, 13.291), (19, 13.909), (17.609, 14.891)), ((16.209, 15.882), (15.109, 17.3), (14.327, 18.809)), ((10.264, 26.664), (16.891, 36.564), (25.855, 34.936)), ((30, 34.182), (33.109, 31.164), (34.455, 27.245)), ((34.655, 26.664), (35.291, 23.782), (35.173, 23.682)), ((34.564, 23.818), (33.945, 23.964), (33.336, 24.1)), ((32.691, 24.245), (32.036, 24.327), (31.373, 24.355)), ((29.118, 24.455), (27.064, 23.564), (25.509, 21.927)), ((24.027, 20.382), (23.255, 18.218), (23.327, 16.082)), ((23.355, 15.518), (23.409, 14.955), (23.545, 14.4)), ((23.673, 13.873), (23.8, 13.345), (23.936, 12.818)), ((23.345, 12.909), (22.582, 12.909), (22, 13)))
        self.add_contour('c0', 'e1', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
