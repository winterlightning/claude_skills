"""Ts (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bac00f7-2dac-4474-9e27-c7fa30bf8b90'
SOURCE_PATH = 'icons-json/symbol/ts (text u)_9bac00f7-2dac-4474-9e27-c7fa30bf8b90.json'
AUTHOR = 'json_to_solo'

class TsTextUSymbol(Solo48):
    icon_id = 'ts-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ts', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (24, 4))
        self.add_line('e1', (16, 27), (16, 4))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_arc('e3-1', (40, 16), (36, 12), radius_x=4, sweep=False)
        self.add_arc('e3-2', (36, 12), (33, 18), radius_x=4, sweep=False)
        self.add_line('e3-3', (33, 18), (39, 21))
        self.add_arc('e3-4', (39, 21), (40, 23), radius_x=3)
        self.add_arc('e3-5', (40, 23), (32, 23), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c1', 'c0')
