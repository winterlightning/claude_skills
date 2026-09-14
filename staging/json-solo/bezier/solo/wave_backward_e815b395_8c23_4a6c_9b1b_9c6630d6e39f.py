"""Wave backward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e815b395-8c23-4a6c-9b1b-9c6630d6e39f'
SOURCE_PATH = 'icons-json/interface-essential/wave backward_e815b395-8c23-4a6c-9b1b-9c6630d6e39f.json'
AUTHOR = 'json_to_solo'

class WaveBackwardE815b395(Solo48):
    icon_id = 'wave-backward-e815b395'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('wave', 'backward', 'interface-essential')

    def build(self):
        self.add_bezier('sym-e0', (22, 4), ((13.627, 9.045), (8, 16.309), (8, 23)))
        self.add_bezier('sym-e1', (8, 23), ((8, 23.309), (8, 23.691), (8, 24)))
        self.add_bezier('sym-e2', (8, 24), ((8, 24.021), (8, 23.979), (8, 24)))
        self.add_bezier('sym-e3', (8, 24), ((8, 24.021), (8, 23.979), (8, 24)))
        self.add_bezier('sym-e4', (8, 24), ((8, 24.309), (8, 24.691), (8, 25)))
        self.add_bezier('sym-e5', (8, 25), ((8, 31.691), (13.627, 38.955), (22, 44)))
        self.add_bezier('sym-e6', (30, 24), ((30, 19.168), (33.317, 13.972), (40, 10)))
        self.add_bezier('sym-e7', (30, 24), ((30, 28.832), (33.317, 34.028), (40, 38)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7')
        self.relate('connect', 'sym-c1', 'sym-c2')
