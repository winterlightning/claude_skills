"""Wave backward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46171cc8-d6da-5b69-b0f8-4184f35d56b9'
SOURCE_PATH = 'icons-json/interface-essential/wave backward_46171cc8-d6da-5b69-b0f8-4184f35d56b9.json'
AUTHOR = 'json_to_solo'

class WaveBackward46171cc8(Solo48):
    icon_id = 'wave-backward-46171cc8'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('wave', 'backward', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (22, 4), (8, 23), radius_x=27, sweep=False)
        self.add_line('sym-e1', (8, 23), (8, 24))
        self.add_line('sym-e4', (8, 24), (8, 25))
        self.add_arc('sym-e5', (8, 25), (22, 44), radius_x=27, sweep=False)
        self.add_arc('sym-e6', (30, 24), (40, 10), radius_x=18)
        self.add_arc('sym-e7', (30, 24), (40, 38), radius_x=18, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7')
        self.relate('connect', 'sym-c1', 'sym-c2')
