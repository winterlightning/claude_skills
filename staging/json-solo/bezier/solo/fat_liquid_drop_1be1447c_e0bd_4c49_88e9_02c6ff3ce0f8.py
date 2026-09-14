"""Fat liquid drop (drinks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1be1447c-e0bd-4c49-88e9-02c6ff3ce0f8'
SOURCE_PATH = 'icons-json/drinks/fat liquid drop_1be1447c-e0bd-4c49-88e9-02c6ff3ce0f8.json'
AUTHOR = 'json_to_solo'

class FatLiquidDrop1be1447c(Solo48):
    icon_id = 'fat-liquid-drop-1be1447c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('fat', 'liquid', 'drop', 'drinks')

    def build(self):
        self.add_line('sym-e0', (22, 7), (14, 18))
        self.add_bezier('sym-e1', (14, 18), ((11.93, 20.818), (8, 26.736), (8, 30)))
        self.add_bezier('sym-e2', (8, 30), ((8, 30.227), (8, 30.773), (8, 31)))
        self.add_bezier('sym-e3', (8, 31), ((8, 31.218), (8, 30.782), (8, 31)))
        self.add_bezier('sym-e4', (8, 31), ((8, 32.282), (8.51, 33.818), (9, 35)))
        self.add_bezier('sym-e5', (9, 35), ((11.21, 40.291), (16.8, 44), (23, 44)))
        self.add_bezier('sym-e6', (23, 44), ((23.13, 44), (23.87, 44), (24, 44)))
        self.add_bezier('sym-e7', (24, 44), ((24.071, 44), (23.93, 44), (24, 44)))
        self.add_bezier('sym-e8', (24, 44), ((24.07, 44), (23.929, 44), (24, 44)))
        self.add_bezier('sym-e9', (24, 44), ((24.13, 44), (24.87, 44), (25, 44)))
        self.add_bezier('sym-e10', (25, 44), ((31.2, 44), (36.79, 40.291), (39, 35)))
        self.add_bezier('sym-e11', (39, 35), ((39.49, 33.818), (40, 32.282), (40, 31)))
        self.add_bezier('sym-e12', (40, 31), ((40, 30.782), (40, 31.218), (40, 31)))
        self.add_bezier('sym-e13', (40, 31), ((40, 30.773), (40, 30.227), (40, 30)))
        self.add_bezier('sym-e14', (40, 30), ((40, 26.736), (36.07, 20.818), (34, 18)))
        self.add_line('sym-e15', (34, 18), (26, 7))
        self.add_line('sym-e16', (26, 7), (24, 4))
        self.add_line('sym-e17', (24, 4), (22, 7))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
