"""Signal wave (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b320e1dd-5fff-5392-b1e9-42b786d6d39b'
SOURCE_PATH = 'icons-json/interface-essential/signal wave_b320e1dd-5fff-5392-b1e9-42b786d6d39b.json'
AUTHOR = 'json_to_solo'

class SignalWave(Solo48):
    icon_id = 'signal-wave'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('signal', 'wave', 'interface-essential')

    def build(self):
        self.add_arc('e0-top', (8, 24), (20, 24), radius_x=6)
        self.add_arc('e0-bottom', (20, 24), (8, 24), radius_x=6)
        self.add_arc('e1-1', (26, 38), (31, 23), radius_x=20, sweep=False)
        self.add_arc('e1-2', (31, 23), (26, 9), radius_x=25, sweep=False)
        self.add_arc('e2-1', (32, 4), (40, 24), radius_x=29)
        self.add_arc('e2-2', (40, 24), (32, 44), radius_x=29)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('c1', 'e2-1', 'e2-2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
