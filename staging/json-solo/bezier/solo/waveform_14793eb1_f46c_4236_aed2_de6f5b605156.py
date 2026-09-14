"""Waveform (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14793eb1-f46c-4236-aed2-de6f5b605156'
SOURCE_PATH = 'icons-json/symbol/waveform_14793eb1-f46c-4236-aed2-de6f5b605156.json'
AUTHOR = 'json_to_solo'

class WaveformSymbol(Solo48):
    icon_id = 'waveform-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('waveform', 'symbol')

    def build(self):
        self.add_line('e0', (44, 25), (39, 25))
        self.add_line('e1', (35, 20), (29, 40))
        self.add_line('e2', (29, 40), (24, 8))
        self.add_line('e3', (24, 8), (17, 35))
        self.add_line('e4', (17, 35), (13, 25))
        self.add_line('e5', (12, 25), (4, 25))
        self.add_bezier('e6', (39, 25), ((37.327, 25), (35.809, 21.538), (35, 20)))
        self.add_bezier('e7', (13, 25), ((12.7, 25), (12.291, 25), (12, 25)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e3', 'e4', 'e7', 'e5')
