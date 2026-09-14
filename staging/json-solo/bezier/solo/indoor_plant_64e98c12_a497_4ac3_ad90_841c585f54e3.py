"""Batch-03/indoor plant (decoration), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64e98c12-a497-4ac3-ad90-841c585f54e3'
SOURCE_PATH = 'icons-json/decoration/batch-03/indoor plant_64e98c12-a497-4ac3-ad90-841c585f54e3.json'
AUTHOR = 'json_to_solo'

class Batch03IndoorPlantDecoration(Solo48):
    icon_id = 'batch-03-indoor-plant-decoration'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'indoor', 'plant', 'decoration')

    def build(self):
        self.add_line('e0', (38, 27), (15, 27))
        self.add_line('e1', (10, 27), (13, 43))
        self.add_line('e2', (15, 44), (33, 44))
        self.add_line('e3', (34, 42), (36, 27))
        self.add_line('e4', (10, 27), (15, 27))
        self.add_line('e5', (14, 25), (15, 27))
        self.add_line('e6', (33, 25), (30, 27))
        self.add_line('e7', (28, 19), (28, 12))
        self.add_line('e8', (19, 16), (19, 19))
        self.add_bezier('e9', (13, 43), ((13.062, 43.382), (14.511, 43.991), (14.942, 43.991)), ((14.991, 44), (15.04, 44), (15.089, 44)), ((15.188, 44), (14.902, 44), (15, 44)))
        self.add_bezier('e10', (33, 44), ((34.095, 43.182), (33.803, 43.209), (34, 42)))
        self.add_bezier('e11', (19, 19), ((16.858, 16.573), (14.954, 13.655), (11.483, 12.164)), ((10.902, 11.913), (8, 10.852), (8, 10.949)), ((8, 10.951), (8, 10.952), (8, 10.955)), ((8, 15.982), (10.96, 20.645), (14, 25)))
        self.add_bezier('e12', (28, 19), ((30.548, 16.409), (32.591, 13.773), (36.369, 12.145)), ((36.721, 11.993), (40, 10.828), (40, 10.974)), ((40, 10.976), (40, 10.979), (40, 10.982)), ((40, 15.536), (36.434, 21.327), (33, 25)))
        self.add_bezier('e13', (28, 12), ((28, 9.8), (26.412, 7.609), (24.997, 5.709)), ((24.706, 5.324), (23.724, 4), (23.611, 4)), ((23.609, 4), (23.607, 4), (23.606, 4)), ((23.483, 4), (22.018, 6.064), (21.723, 6.527)), ((19.84, 9.427), (19.135, 12.818), (19, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e9', 'e2', 'e10', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e11', 'e5')
        self.add_contour('c4', 'e12', 'e6')
        self.add_contour('c5', 'e7', 'e13', 'e8')
        self.relate('connect', 'c4', 'c0')
