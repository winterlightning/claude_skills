"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70c2117f-0d53-445a-80cb-9c38d8a76797'
SOURCE_PATH = 'icons-json/audio/microphone_70c2117f-0d53-445a-80cb-9c38d8a76797.json'
AUTHOR = 'json_to_solo'

class Microphone(Solo48):
    icon_id = 'microphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 36))
        self.add_bezier('sym-e1', (24, 36), ((24.222, 36), (24.777, 36), (25, 36)))
        self.add_bezier('sym-e2', (25, 36), ((25.111, 36), (24.889, 36), (25, 36)))
        self.add_bezier('sym-e3', (25, 36), ((24.89, 36.003), (25.111, 36), (25, 36)))
        self.add_bezier('sym-e4', (25, 36), ((24.777, 36), (24.22, 36), (24, 36)))
        self.add_bezier('sym-e5', (24, 36), ((23.778, 36), (23.223, 36), (23, 36)))
        self.add_bezier('sym-e6', (23, 36), ((22.889, 36), (23.111, 36), (23, 36)))
        self.add_bezier('sym-e7', (23, 36), ((23.11, 36.003), (22.889, 36), (23, 36)))
        self.add_bezier('sym-e8', (23, 36), ((23.223, 36), (23.78, 36), (24, 36)))
        self.add_bezier('sym-e9', (25, 36), ((31.52, 35.864), (37.07, 31.627), (39, 26)))
        self.add_bezier('sym-e10', (39, 26), ((39.34, 25.009), (40, 24.045), (40, 23)))
        self.add_bezier('sym-e11', (40, 23), ((40, 22.864), (39.99, 22.127), (40, 22)))
        self.add_bezier('sym-e12', (24, 4), ((24.141, 4), (23.86, 4), (24, 4)))
        self.add_bezier('sym-e13', (24, 4), ((27.6, 4), (31.25, 6.9), (32, 10)))
        self.add_bezier('sym-e14', (32, 10), ((32.21, 10.864), (32, 11.155), (32, 12)))
        self.add_line('sym-e15', (32, 12), (32, 22))
        self.add_bezier('sym-e16', (32, 22), ((32, 22.264), (31.14, 23.682), (31, 24)))
        self.add_bezier('sym-e17', (31, 24), ((29.727, 26.83), (27.259, 29), (24, 29)))
        self.add_bezier('sym-e18', (24, 29), ((20.741, 29), (18.273, 26.83), (17, 24)))
        self.add_bezier('sym-e19', (17, 24), ((16.86, 23.682), (16, 22.264), (16, 22)))
        self.add_line('sym-e20', (16, 22), (16, 12))
        self.add_bezier('sym-e21', (16, 12), ((16, 11.155), (15.79, 10.864), (16, 10)))
        self.add_bezier('sym-e22', (16, 10), ((16.75, 6.9), (20.4, 4), (24, 4)))
        self.add_bezier('sym-e23', (24, 4), ((24.14, 4), (23.859, 4), (24, 4)))
        self.add_bezier('sym-e24', (23, 36), ((16.48, 35.864), (10.93, 31.627), (9, 26)))
        self.add_bezier('sym-e25', (9, 26), ((8.66, 25.009), (8, 24.045), (8, 23)))
        self.add_bezier('sym-e26', (8, 23), ((8, 22.864), (8.01, 22.127), (8, 22)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c1', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
        self.add_contour('sym-c3', 'sym-e24', 'sym-e25', 'sym-e26')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
