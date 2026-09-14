"""Cd (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b549dc2-c357-42c8-9126-e2a818b17485'
SOURCE_PATH = 'icons-json/symbol/cd (text u)_2b549dc2-c357-42c8-9126-e2a818b17485.json'
AUTHOR = 'json_to_solo'

class CdTextUSymbol(Solo48):
    icon_id = 'cd-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cd', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (40, 4), (40, 23))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_bezier('e3', (19, 8), ((17.973, 5.991), (16.168, 4.009), (13.912, 4.009)), ((13.777, 4.009), (13.642, 4), (13.507, 4)), ((13.44, 4), (13.373, 4), (13.305, 4.009)), ((10.813, 4.009), (8.008, 6.391), (8.008, 9.236)), ((8.008, 9.309), (8, 8.927), (8, 9)))
        self.add_bezier('e4', (8, 21), ((8, 24.7), (11.933, 27.209), (14.956, 26.518)), ((16.808, 26.091), (18.099, 24.736), (19, 23)))
        self.add_bezier('e5', (40, 23), ((40, 22.982), (39.992, 23.118), (39.992, 23.136)), ((39.992, 23.445), (39.747, 23.864), (39.604, 24.109)), ((38.467, 26.082), (36.135, 26.527), (34.147, 26.491)), ((30.341, 26.418), (27.815, 22.809), (27.857, 18.864)), ((27.899, 14.8), (31.124, 11.727), (34.754, 11.545)), ((36.303, 11.473), (37.861, 11.955), (39.091, 12.991)), ((39.276, 13.145), (39.992, 13.682), (39.992, 13.982)), ((40, 13.991), (40, 13.991), (40, 14)))
        self.add_contour('c0', 'e3', 'e0', 'e4')
        self.add_contour('c1', 'e1', 'e5')
        self.add_contour('c2', 'e2')
