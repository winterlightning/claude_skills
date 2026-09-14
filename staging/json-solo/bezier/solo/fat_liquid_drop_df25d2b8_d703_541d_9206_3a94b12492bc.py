"""Fat liquid drop (drinks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df25d2b8-d703-541d-9206-3a94b12492bc'
SOURCE_PATH = 'icons-json/drinks/fat liquid drop_df25d2b8-d703-541d-9206-3a94b12492bc.json'
AUTHOR = 'json_to_solo'

class FatLiquidDropDf25d2b8(Solo48):
    icon_id = 'fat-liquid-drop-df25d2b8'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('fat', 'liquid', 'drop', 'drinks')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 44))
        self.add_bezier('sym-e1', (24, 44), ((23.956, 44), (24.043, 44), (24, 44)))
        self.add_bezier('sym-e2', (24, 44), ((17.36, 44), (11.12, 39.727), (9, 34)))
        self.add_bezier('sym-e3', (9, 34), ((8.6, 32.918), (8, 32.145), (8, 31)))
        self.add_bezier('sym-e4', (8, 31), ((8, 30.918), (8.01, 31.073), (8, 31)))
        self.add_bezier('sym-e5', (8, 31), ((8, 30.836), (8, 30.164), (8, 30)))
        self.add_bezier('sym-e6', (8, 30), ((8, 28.227), (8.48, 26.7), (9, 25)))
        self.add_bezier('sym-e7', (9, 25), ((11.5, 19.018), (15.7, 14.027), (20, 9)))
        self.add_bezier('sym-e8', (20, 9), ((21.01, 7.818), (21.91, 6.127), (23, 5)))
        self.add_bezier('sym-e9', (23, 5), ((23.36, 4.627), (23.64, 4.373), (24, 4)))
        self.add_bezier('sym-e10', (24, 4), ((24, 4), (23.97, 4), (24, 4)))
        self.add_bezier('sym-e11', (24, 4), ((24.015, 4), (23.979, 4), (24, 4)))
        self.add_bezier('sym-e12', (24, 4), ((24.021, 4), (23.985, 4), (24, 4)))
        self.add_bezier('sym-e13', (24, 4), ((24.03, 4), (24, 4), (24, 4)))
        self.add_bezier('sym-e14', (24, 4), ((24.36, 4.373), (24.64, 4.627), (25, 5)))
        self.add_bezier('sym-e15', (25, 5), ((26.09, 6.127), (26.99, 7.818), (28, 9)))
        self.add_bezier('sym-e16', (28, 9), ((32.3, 14.027), (36.5, 19.018), (39, 25)))
        self.add_bezier('sym-e17', (39, 25), ((39.52, 26.7), (40, 28.227), (40, 30)))
        self.add_bezier('sym-e18', (40, 30), ((40, 30.164), (40, 30.836), (40, 31)))
        self.add_bezier('sym-e19', (40, 31), ((39.99, 31.073), (40, 30.918), (40, 31)))
        self.add_bezier('sym-e20', (40, 31), ((40, 32.145), (39.4, 32.918), (39, 34)))
        self.add_bezier('sym-e21', (39, 34), ((36.88, 39.727), (30.64, 44), (24, 44)))
        self.add_bezier('sym-e22', (24, 44), ((23.957, 44), (24.044, 44), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
