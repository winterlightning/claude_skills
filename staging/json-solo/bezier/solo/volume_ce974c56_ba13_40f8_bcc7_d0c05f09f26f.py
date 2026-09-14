"""Volume (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce974c56-ba13-40f8-bcc7-d0c05f09f26f'
SOURCE_PATH = 'icons-json/interface-essential/volume_ce974c56-ba13-40f8-bcc7-d0c05f09f26f.json'
AUTHOR = 'json_to_solo'

class VolumeCe974c56(Solo48):
    icon_id = 'volume-ce974c56'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('volume', 'interface-essential')

    def build(self):
        self.add_line('e0', (26, 8), (13, 17))
        self.add_line('e1', (4, 21), (4, 27))
        self.add_line('e2', (7, 30), (12, 30))
        self.add_line('e3', (13, 30), (26, 40))
        self.add_line('e4', (26, 40), (26, 34))
        self.add_line('e5', (26, 34), (26, 11))
        self.add_line('e6', (26, 11), (26, 8))
        self.add_bezier('e7', (39, 13), ((41.427, 15.956), (43.982, 19.352), (43.982, 23.2)), ((43.991, 23.267), (43.991, 23.335), (44, 23.402)), ((44, 23.405), (44, 23.407), (44, 23.41)), ((44, 23.567), (43.991, 23.733), (43.991, 23.891)), ((43.991, 27.857), (42.4, 30.775), (40, 34)))
        self.add_bezier('e8', (34, 29), ((36.427, 25.531), (36.4, 22.478), (34, 19)))
        self.add_bezier('e9', (13, 17), ((12.545, 17.328), (11.891, 17.617), (11.355, 17.667)), ((10.373, 17.768), (9.373, 17.844), (8.382, 17.92)), ((6.6, 18.063), (4.009, 18.164), (4.009, 20.438)), ((4.009, 20.505), (4, 20.933), (4, 21)))
        self.add_bezier('e10', (4, 27), ((4, 27.194), (4.009, 26.914), (4.009, 27.099)), ((4.009, 27.234), (4.009, 27.36), (4, 27.495)), ((4, 27.554), (4, 27.621), (4, 27.688)), ((4, 27.815), (4.009, 27.941), (4.009, 28.067)), ((4.009, 28.227), (4.164, 28.472), (4.236, 28.606)), ((4.773, 29.541), (5.909, 30), (7, 30)))
        self.add_bezier('e11', (12, 30), ((12.218, 30), (12.809, 29.848), (13, 30)))
        self.add_contour('c0', 'e7')
        self.add_contour('c1', 'e8')
        self.add_contour('c2', 'e0', 'e9', 'e1', 'e10', 'e2', 'e11', 'e3', 'e4', 'e5', 'e6', closed=True)
