"""Pa (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '443d8fb3-2e9d-434a-8f52-35b60151f3e1'
SOURCE_PATH = 'icons-json/symbol/pa (text u)_443d8fb3-2e9d-434a-8f52-35b60151f3e1.json'
AUTHOR = 'json_to_solo'

class PaTextUSymbol(Solo48):
    icon_id = 'pa-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pa', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (15, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (40, 27), (40, 23))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_bezier('e5', (15, 16), ((15.758, 16), (16.421, 15.464), (17.095, 15.109)), ((21.389, 12.864), (20.792, 5.809), (16.236, 4.336)), ((15.756, 4.182), (15.505, 4), (15, 4)))
        self.add_bezier('e6', (40, 23), ((40, 23), (40, 23.1), (39.992, 23.1)), ((39.992, 23.436), (39.36, 24.091), (39.175, 24.318)), ((37.996, 25.773), (36.48, 26.555), (34.695, 26.518)), ((30.931, 26.427), (28.589, 23.909), (28.539, 19.782)), ((28.505, 16.409), (30.459, 13.082), (33.575, 12.245)), ((36.025, 11.591), (39.992, 13.727), (39.992, 16.755)), ((39.992, 16.836), (40, 16.918), (40, 16.991)), ((40, 19.027), (40, 20.964), (40, 23)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e6', closed=True)
