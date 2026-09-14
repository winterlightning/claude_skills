"""Laundry retro iron (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '879a01d8-65f1-5821-9058-fbf154f1e7ed'
SOURCE_PATH = 'icons-json/wayfinding/laundry retro iron_879a01d8-65f1-5821-9058-fbf154f1e7ed.json'
AUTHOR = 'json_to_solo'

class LaundryRetroIronWayfinding(Solo48):
    icon_id = 'laundry-retro-iron-wayfinding'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('laundry', 'retro', 'iron', 'wayfinding')

    def build(self):
        self.add_line('e0', (19, 8), (34, 8))
        self.add_line('e1', (39, 13), (44, 40))
        self.add_line('e2', (44, 40), (4, 40))
        self.add_line('e3', (20, 21), (40, 21))
        self.add_bezier('e4', (34, 8), ((36.664, 8), (38.518, 10.13), (39, 13)))
        self.add_bezier('e5', (4, 40), ((4, 39.57), (4, 39.15), (4, 38.72)), ((4, 38), (4.627, 35.5), (4.845, 34.74)), ((6.745, 28.1), (11.391, 22.8), (17.745, 21.44)), ((18.573, 21.26), (19.164, 21), (20, 21)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e2', 'e5', 'e3')
