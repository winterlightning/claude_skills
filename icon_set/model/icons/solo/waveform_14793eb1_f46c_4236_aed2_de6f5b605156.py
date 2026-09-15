"""Waveform (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14793eb1-f46c-4236-aed2-de6f5b605156'
SOURCE_PATH = 'pictographic-primitives/symbol/waveform_14793eb1-f46c-4236-aed2-de6f5b605156.svg'
AUTHOR = 'gpt-6'

class Waveform(Solo48):
    icon_id = 'waveform'
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
        self.add_arc('e6', (39, 25), (35, 20), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('e7', (13, 25), (4, 25))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e3', 'e4', 'e7', closed=False)
