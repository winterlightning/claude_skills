"""Ts (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e3', (40, 16), ((40, 15.982), (39.992, 15.791), (39.992, 15.773)), ((39.992, 15.318), (39.646, 14.691), (39.453, 14.3)), ((38.989, 13.373), (38.291, 12.555), (37.356, 12.2)), ((35.217, 11.382), (32.211, 12.836), (32.194, 15.509)), ((32.185, 18.755), (35.453, 19.218), (37.617, 20.264)), ((38.627, 20.755), (39.992, 21.591), (39.992, 22.982)), ((39.992, 23.036), (40, 23.091), (40, 23.136)), ((39.992, 23.2), (39.992, 23.255), (39.992, 23.309)), ((39.992, 26.818), (34.467, 27.327), (32.926, 25.018)), ((32.522, 24.409), (32.076, 23.7), (32, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c1', 'c0')
