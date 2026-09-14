"""Wave forward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bb2f977-a3d0-415f-a8d5-a93cf49c7af1'
SOURCE_PATH = 'icons-json/interface-essential/wave forward_4bb2f977-a3d0-415f-a8d5-a93cf49c7af1.json'
AUTHOR = 'json_to_solo'

class WaveForward(Solo48):
    icon_id = 'wave-forward'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('wave', 'forward', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (40, 24), (40, 23), radius_x=26)
        self.add_arc('sym-e1', (40, 23), (26, 4), radius_x=25, sweep=False)
        self.add_arc('sym-e2', (8, 11), (17, 24), radius_x=16)
        self.add_arc('sym-e3', (17, 24), (8, 37), radius_x=16)
        self.add_arc('sym-e4', (40, 24), (40, 25), radius_x=28, sweep=False)
        self.add_arc('sym-e5', (40, 25), (26, 44), radius_x=25)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5')
        self.relate('connect', 'sym-c0', 'sym-c2')
