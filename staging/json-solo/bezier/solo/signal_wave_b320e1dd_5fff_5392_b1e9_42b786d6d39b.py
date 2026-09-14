"""Signal wave (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b320e1dd-5fff-5392-b1e9-42b786d6d39b'
SOURCE_PATH = 'icons-json/interface-essential/signal wave_b320e1dd-5fff-5392-b1e9-42b786d6d39b.json'
AUTHOR = 'json_to_solo'

class SignalWaveInterfaceEssential(Solo48):
    icon_id = 'signal-wave-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('signal', 'wave', 'interface-essential')

    def build(self):
        self.add_arc('e0-top', (8, 24), (20, 24), radius_x=6)
        self.add_arc('e0-bottom', (20, 24), (8, 24), radius_x=6)
        self.add_bezier('e1', (26, 38), ((27.945, 35.627), (29.432, 32.645), (30.291, 29.573)), ((32.261, 22.527), (30.295, 14.436), (26, 9)))
        self.add_bezier('e2', (32, 4), ((32.135, 4.145), (32.724, 4.182), (32.851, 4.345)), ((33.844, 5.7), (34.897, 7.009), (35.773, 8.464)), ((38.274, 12.618), (39.983, 17.836), (39.983, 22.845)), ((39.983, 23.136), (40, 23.427), (40, 23.718)), ((40, 23.723), (40, 23.727), (40, 23.732)), ((40, 24.018), (39.992, 24.305), (39.992, 24.591)), ((39.992, 29.709), (38.442, 35.045), (35.891, 39.336)), ((34.981, 40.864), (33.886, 42.236), (32.851, 43.655)), ((32.724, 43.818), (32.135, 43.855), (32, 44)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
