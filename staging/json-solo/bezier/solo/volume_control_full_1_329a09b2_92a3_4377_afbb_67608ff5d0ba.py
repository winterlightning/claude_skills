"""Volume control full 1 (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '329a09b2-92a3-4377-afbb-67608ff5d0ba'
SOURCE_PATH = 'icons-json/audio/volume control full 1_329a09b2-92a3-4377-afbb-67608ff5d0ba.json'
AUTHOR = 'json_to_solo'

class VolumeControlFull1Audio(Solo48):
    icon_id = 'volume-control-full-1-audio'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'full', 'audio')

    def build(self):
        self.add_line('e0', (26, 40), (16, 31))
        self.add_line('e1', (15, 30), (6, 30))
        self.add_line('e2', (4, 29), (4, 19))
        self.add_line('e3', (6, 17), (15, 17))
        self.add_line('e4', (16, 17), (26, 8))
        self.add_line('e5', (29, 10), (29, 38))
        self.add_bezier('e6', (39, 14), ((41.5, 16.568), (43.991, 20.025), (43.991, 23.571)), ((43.991, 23.67), (44, 23.761), (44, 23.861)), ((44, 23.862), (44, 23.864), (44, 23.865)), ((44, 24.135), (43.991, 24.413), (43.991, 24.682)), ((43.991, 28.168), (41.473, 31.516), (39, 34)))
        self.add_bezier('e7', (35, 18), ((38.045, 21.444), (39.145, 26.312), (36, 30)))
        self.add_bezier('e8', (16, 31), ((15.691, 30.714), (15.327, 30.278), (15, 30)))
        self.add_bezier('e9', (6, 30), ((5.473, 30), (4.627, 29.785), (4.236, 29.415)), ((4.136, 29.314), (4.109, 29.093), (4, 29)))
        self.add_bezier('e10', (4, 19), ((4.009, 18.958), (4.009, 18.863), (4.018, 18.813)), ((4.018, 17.945), (5.336, 17.295), (6, 17)))
        self.add_bezier('e11', (15, 17), ((15.145, 17), (15.891, 17.101), (16, 17)))
        self.add_bezier('e12', (26, 8), ((26.182, 8), (26.182, 8), (26.364, 8)), ((26.536, 8), (26.709, 8), (26.891, 8)), ((27.036, 8), (27.191, 8), (27.336, 8)), ((28.209, 8), (28.855, 9.461), (29, 10)))
        self.add_bezier('e13', (29, 38), ((28.845, 38.472), (28.055, 40), (27.273, 40)), ((27.091, 40), (26.918, 39.983), (26.736, 39.983)), ((26.6, 39.992), (26.464, 39.992), (26.327, 40)), ((26.155, 40), (26.173, 40), (26, 40)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4', 'e12', 'e5', 'e13', closed=True)
