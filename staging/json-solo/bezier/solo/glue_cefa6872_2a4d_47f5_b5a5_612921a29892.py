"""Glue (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cefa6872-2a4d-47f5-b5a5-612921a29892'
SOURCE_PATH = 'icons-json/design/glue_cefa6872-2a4d-47f5-b5a5-612921a29892.json'
AUTHOR = 'json_to_solo'

class GlueDesign(Solo48):
    icon_id = 'glue-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('glue', 'design')

    def build(self):
        self.add_bezier('sym-e0', (24, 4), ((24.054, 4), (23.949, 4.006), (24, 4)))
        self.add_bezier('sym-e1', (24, 4), ((24.08, 4.009), (23.93, 4), (24, 4)))
        self.add_bezier('sym-e2', (24, 4), ((24.92, 4), (26.74, 5.182), (27, 6)))
        self.add_line('sym-e3', (27, 6), (29, 12))
        self.add_line('sym-e4', (29, 12), (32, 21))
        self.add_line('sym-e5', (32, 21), (24, 21))
        self.add_line('sym-e6', (24, 21), (16, 21))
        self.add_line('sym-e7', (16, 21), (19, 12))
        self.add_line('sym-e8', (19, 12), (21, 6))
        self.add_bezier('sym-e9', (21, 6), ((21.26, 5.182), (23.08, 4), (24, 4)))
        self.add_bezier('sym-e10', (24, 4), ((24.07, 4), (23.92, 4.009), (24, 4)))
        self.add_bezier('sym-e11', (24, 4), ((24.051, 4.006), (23.946, 4), (24, 4)))
        self.add_line('sym-e12', (32, 21), (35, 21))
        self.add_bezier('sym-e13', (35, 21), ((36.41, 21.309), (37.14, 21.964), (38, 23)))
        self.add_line('sym-e14', (38, 23), (40, 39))
        self.add_bezier('sym-e15', (40, 39), ((40, 39.091), (40, 39.909), (40, 40)))
        self.add_bezier('sym-e16', (40, 40), ((40, 41.491), (37.85, 44), (36, 44)))
        self.add_bezier('sym-e17', (36, 44), ((35.96, 44), (36.04, 43.991), (36, 44)))
        self.add_line('sym-e18', (36, 44), (24, 44))
        self.add_line('sym-e19', (24, 44), (12, 44))
        self.add_bezier('sym-e20', (12, 44), ((11.96, 43.991), (12.04, 44), (12, 44)))
        self.add_bezier('sym-e21', (12, 44), ((10.15, 44), (8, 41.491), (8, 40)))
        self.add_bezier('sym-e22', (8, 40), ((8, 39.909), (8, 39.091), (8, 39)))
        self.add_line('sym-e23', (8, 39), (10, 23))
        self.add_bezier('sym-e24', (10, 23), ((10.86, 21.964), (11.59, 21.309), (13, 21)))
        self.add_line('sym-e25', (13, 21), (16, 21))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
