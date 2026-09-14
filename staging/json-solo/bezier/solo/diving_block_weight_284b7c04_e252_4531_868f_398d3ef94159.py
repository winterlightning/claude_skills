"""Diving block weight (recreation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '284b7c04-e252-4531-868f-398d3ef94159'
SOURCE_PATH = 'icons-json/recreation/diving block weight_284b7c04-e252-4531-868f-398d3ef94159.json'
AUTHOR = 'json_to_solo'

class DivingBlockWeightRecreation(Solo48):
    icon_id = 'diving-block-weight-recreation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    aliases = ()
    keywords = ('diving', 'block', 'weight', 'recreation')

    def build(self):
        self.add_bezier('sym-e0', (24, 29), ((27.84, 29), (32.094, 28.753), (35, 28)))
        self.add_bezier('sym-e1', (35, 28), ((36.932, 27.5), (38.203, 26.736), (40, 26)))
        self.add_line('sym-e2', (40, 26), (40, 38))
        self.add_bezier('sym-e3', (40, 38), ((40, 39.164), (38.095, 40.282), (37, 41)))
        self.add_bezier('sym-e4', (37, 41), ((33.763, 43.118), (29.332, 44), (25, 44)))
        self.add_bezier('sym-e5', (25, 44), ((24.536, 44), (24.464, 44), (24, 44)))
        self.add_bezier('sym-e6', (24, 44), ((23.536, 44), (23.464, 44), (23, 44)))
        self.add_bezier('sym-e7', (23, 44), ((18.668, 44), (14.237, 43.118), (11, 41)))
        self.add_bezier('sym-e8', (11, 41), ((9.905, 40.282), (8, 39.164), (8, 38)))
        self.add_line('sym-e9', (8, 38), (8, 26))
        self.add_bezier('sym-e10', (8, 26), ((9.797, 26.736), (11.068, 27.5), (13, 28)))
        self.add_bezier('sym-e11', (13, 28), ((15.906, 28.753), (20.16, 29), (24, 29)))
        self.add_bezier('sym-e12', (24, 4), ((24.229, 4), (24.767, 4), (25, 4)))
        self.add_bezier('sym-e13', (25, 4), ((26.772, 4), (28.449, 4.409), (30, 5)))
        self.add_bezier('sym-e14', (30, 5), ((35.895, 7.245), (39.003, 12.391), (40, 17)))
        self.add_bezier('sym-e15', (40, 17), ((40, 17.836), (40, 18.164), (40, 19)))
        self.add_line('sym-e16', (40, 19), (40, 26))
        self.add_bezier('sym-e17', (24, 4), ((23.771, 4), (23.233, 4), (23, 4)))
        self.add_bezier('sym-e18', (23, 4), ((21.228, 4), (19.551, 4.409), (18, 5)))
        self.add_bezier('sym-e19', (18, 5), ((12.105, 7.245), (8.997, 12.391), (8, 17)))
        self.add_bezier('sym-e20', (8, 17), ((8, 17.836), (8, 18.164), (8, 19)))
        self.add_line('sym-e21', (8, 19), (8, 26))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
