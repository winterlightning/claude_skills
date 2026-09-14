"""Drop shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c25c47b-1058-47e2-8f07-a986157c4478'
SOURCE_PATH = 'icons-json/design/drop shape_6c25c47b-1058-47e2-8f07-a986157c4478.json'
AUTHOR = 'json_to_solo'

class DropShapeDesign(Solo48):
    icon_id = 'drop-shape-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('drop', 'shape', 'design')

    def build(self):
        self.add_line('sym-e0', (21, 6), (11, 17))
        self.add_bezier('sym-e1', (11, 17), ((8.962, 19.2), (8, 22.918), (8, 26)))
        self.add_bezier('sym-e2', (8, 26), ((8, 26.127), (8, 26.873), (8, 27)))
        self.add_bezier('sym-e3', (8, 27), ((8, 27.336), (8, 27.664), (8, 28)))
        self.add_bezier('sym-e4', (8, 28), ((8, 36.482), (15.202, 44), (23, 44)))
        self.add_bezier('sym-e5', (23, 44), ((23.059, 44), (23.941, 44), (24, 44)))
        self.add_bezier('sym-e6', (24, 44), ((24.16, 44), (23.84, 44), (24, 44)))
        self.add_bezier('sym-e7', (24, 44), ((24.16, 44), (23.84, 44), (24, 44)))
        self.add_bezier('sym-e8', (24, 44), ((24.059, 44), (24.941, 44), (25, 44)))
        self.add_bezier('sym-e9', (25, 44), ((32.798, 44), (40, 36.482), (40, 28)))
        self.add_bezier('sym-e10', (40, 28), ((40, 27.664), (40, 27.336), (40, 27)))
        self.add_bezier('sym-e11', (40, 27), ((40, 26.873), (40, 26.127), (40, 26)))
        self.add_bezier('sym-e12', (40, 26), ((40, 22.918), (39.038, 19.2), (37, 17)))
        self.add_line('sym-e13', (37, 17), (27, 6))
        self.add_bezier('sym-e14', (27, 6), ((26.596, 5.564), (24.547, 4), (24, 4)))
        self.add_bezier('sym-e15', (24, 4), ((23.955, 4), (24.045, 4), (24, 4)))
        self.add_bezier('sym-e16', (24, 4), ((23.955, 4), (24.045, 4), (24, 4)))
        self.add_bezier('sym-e17', (24, 4), ((23.453, 4), (21.404, 5.564), (21, 6)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
