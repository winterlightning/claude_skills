"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e543cdc-214f-483d-bf63-44eeef6a18ba'
SOURCE_PATH = 'icons-json/audio/microphone_3e543cdc-214f-483d-bf63-44eeef6a18ba.json'
AUTHOR = 'json_to_solo'

class Microphone3e543cdc(Solo48):
    icon_id = 'microphone-3e543cdc'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self):
        self.add_bezier('sym-e0', (40, 24), ((40, 24.209), (40, 24.782), (40, 25)))
        self.add_bezier('sym-e1', (40, 25), ((40, 26.682), (39.8, 28.491), (39, 30)))
        self.add_bezier('sym-e2', (39, 30), ((36.27, 35.091), (30.16, 38), (24, 38)))
        self.add_bezier('sym-e3', (24, 38), ((17.84, 38), (11.73, 35.091), (9, 30)))
        self.add_bezier('sym-e4', (9, 30), ((8.2, 28.491), (8, 26.682), (8, 25)))
        self.add_bezier('sym-e5', (8, 25), ((8, 24.782), (8, 24.209), (8, 24)))
        self.add_line('sym-e6', (24, 38), (24, 44))
        self.add_line('sym-e7', (16, 19), (16, 10))
        self.add_bezier('sym-e8', (16, 10), ((16, 9.645), (15.87, 9.336), (16, 9)))
        self.add_bezier('sym-e9', (16, 9), ((17, 6.255), (20.71, 4), (24, 4)))
        self.add_bezier('sym-e10', (24, 4), ((24.12, 4), (23.88, 4), (24, 4)))
        self.add_bezier('sym-e11', (24, 4), ((24.12, 4), (23.88, 4), (24, 4)))
        self.add_bezier('sym-e12', (24, 4), ((27.29, 4), (31, 6.255), (32, 9)))
        self.add_bezier('sym-e13', (32, 9), ((32.13, 9.336), (32, 9.645), (32, 10)))
        self.add_line('sym-e14', (32, 10), (32, 19))
        self.add_bezier('sym-e15', (32, 19), ((32, 22.736), (29.28, 25.327), (25, 26)))
        self.add_bezier('sym-e16', (25, 26), ((24.52, 26.075), (24.472, 26), (24, 26)))
        self.add_bezier('sym-e17', (24, 26), ((23.528, 26), (23.48, 26.075), (23, 26)))
        self.add_bezier('sym-e18', (23, 26), ((18.72, 25.327), (16, 22.736), (16, 19)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
