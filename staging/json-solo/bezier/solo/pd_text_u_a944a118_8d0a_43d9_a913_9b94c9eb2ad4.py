"""Pd (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a944a118-8d0a-43d9-a913-9b94c9eb2ad4'
SOURCE_PATH = 'icons-json/symbol/pd (text u)_a944a118-8d0a-43d9-a913-9b94c9eb2ad4.json'
AUTHOR = 'json_to_solo'

class PdTextUSymbol(Solo48):
    icon_id = 'pd-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pd', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (15, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (40, 4), (40, 23))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_bezier('e5', (15, 16), ((15.758, 16), (16.429, 15.464), (17.095, 15.109)), ((21.364, 12.855), (20.775, 5.809), (16.236, 4.336)), ((15.747, 4.182), (15.505, 4), (15, 4)))
        self.add_bezier('e6', (40, 23), ((40, 22.982), (39.992, 23.118), (39.992, 23.136)), ((39.992, 23.482), (39.731, 23.927), (39.571, 24.2)), ((38.4, 26.236), (35.832, 26.718), (33.785, 26.445)), ((30.383, 25.991), (28.463, 22.355), (28.48, 18.891)), ((28.497, 15.064), (31.335, 11.818), (34.838, 11.545)), ((36.354, 11.427), (37.861, 11.9), (39.057, 12.918)), ((39.251, 13.091), (39.992, 13.655), (39.992, 13.982)), ((40, 13.991), (40, 13.991), (40, 14)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e6')
        self.add_contour('c2', 'e4')
