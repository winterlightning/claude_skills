"""Fat liquid drop (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df25d2b8-d703-541d-9206-3a94b12492bc'
SOURCE_PATH = 'icons-json/drinks/fat liquid drop_df25d2b8-d703-541d-9206-3a94b12492bc.json'
AUTHOR = 'json_to_solo'

class FatLiquidDropDrinks(Solo48):
    icon_id = 'fat-liquid-drop-drinks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('fat', 'liquid', 'drop', 'drinks')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 44))
        self.add_arc('sym-e2', (24, 44), (9, 34), radius_x=17)
        self.add_arc('sym-e3', (9, 34), (8, 31), radius_x=11)
        self.add_line('sym-e5', (8, 31), (8, 30))
        self.add_arc('sym-e6', (8, 30), (9, 25), radius_x=17)
        self.add_arc('sym-e7', (9, 25), (20, 9), radius_x=62)
        self.add_arc('sym-e8', (20, 9), (23, 5), radius_x=71)
        self.add_line('sym-e9', (23, 5), (24, 4))
        self.add_line('sym-e14', (24, 4), (25, 5))
        self.add_arc('sym-e15', (25, 5), (28, 9), radius_x=72, sweep=False)
        self.add_arc('sym-e16', (28, 9), (39, 25), radius_x=62)
        self.add_arc('sym-e17', (39, 25), (40, 30), radius_x=17)
        self.add_arc('sym-e18', (40, 30), (40, 31), radius_x=32, sweep=False)
        self.add_line('sym-e20', (40, 31), (39, 34))
        self.add_arc('sym-e21', (39, 34), (24, 44), radius_x=17)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', closed=True)
