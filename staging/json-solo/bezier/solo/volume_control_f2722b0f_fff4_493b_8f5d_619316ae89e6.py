"""Volume control (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2722b0f-fff4-493b-8f5d-619316ae89e6'
SOURCE_PATH = 'icons-json/audio/volume control_f2722b0f-fff4-493b-8f5d-619316ae89e6.json'
AUTHOR = 'json_to_solo'

class VolumeControlAudio(Solo48):
    icon_id = 'volume-control-audio'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'audio')

    def build(self):
        self.add_line('e0', (15, 31), (8, 31))
        self.add_line('e1', (4, 28), (4, 20))
        self.add_line('e2', (7, 17), (15, 17))
        self.add_line('e3', (15, 31), (15, 17))
        self.add_line('e4', (15, 31), (29, 40))
        self.add_line('e5', (32, 38), (32, 10))
        self.add_line('e6', (29, 9), (15, 17))
        self.add_bezier('e7', (8, 31), ((6.564, 31), (4, 29.971), (4, 28.354)), ((4, 28.303), (4, 28.051), (4, 28)))
        self.add_bezier('e8', (4, 20), ((4, 18.787), (5.709, 17), (7, 17)))
        self.add_bezier('e9', (29, 40), ((29.2, 40), (29.864, 40), (30.064, 40)), ((30.236, 40), (30.427, 39.992), (30.609, 39.992)), ((30.664, 39.992), (30.718, 40), (30.773, 40)), ((30.891, 39.992), (31, 39.992), (31.118, 39.983)), ((31.609, 39.983), (31.873, 38.328), (32, 38)))
        self.add_bezier('e10', (32, 10), ((32, 9.318), (31.436, 8.008), (30.636, 8.008)), ((30.574, 8.008), (30.511, 8), (30.448, 8)), ((30.447, 8), (30.446, 8), (30.445, 8)), ((29.809, 8), (29.509, 8.688), (29, 9)))
        self.add_bezier('e11', (39, 16), ((41.127, 17.516), (42.727, 19.006), (43.518, 21.347)), ((43.745, 22.038), (43.991, 22.762), (43.991, 23.495)), ((43.991, 23.594), (44, 23.694), (44, 23.793)), ((44, 23.795), (44, 23.796), (44, 23.798)), ((44, 23.899), (43.982, 24), (43.982, 24.101)), ((43.982, 24.808), (43.7, 25.558), (43.445, 26.223)), ((42.545, 28.615), (40.945, 30.181), (39, 32)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.add_contour('c3', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
