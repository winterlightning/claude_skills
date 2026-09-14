"""Ascot (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab8d76cc-163d-429e-8ba7-e88fde2375f3'
SOURCE_PATH = 'icons-json/_uncategorized_04/ascot_ab8d76cc-163d-429e-8ba7-e88fde2375f3.json'
AUTHOR = 'json_to_solo'

class AscotUncategorized04(Solo48):
    icon_id = 'ascot-uncategorized-04'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('ascot', '_uncategorized_04')

    def build(self):
        self.add_line('sym-e0', (17, 14), (31, 14))
        self.add_line('sym-e1', (31, 14), (40, 35))
        self.add_bezier('sym-e2', (40, 35), ((40, 35.3), (40, 35.7), (40, 36)))
        self.add_line('sym-e3', (40, 36), (26, 44))
        self.add_bezier('sym-e4', (26, 44), ((25.502, 44), (24.498, 44), (24, 44)))
        self.add_bezier('sym-e5', (24, 44), ((23.914, 44), (24.091, 44), (24, 44)))
        self.add_bezier('sym-e6', (24, 44), ((23.909, 44), (24.086, 44), (24, 44)))
        self.add_bezier('sym-e7', (24, 44), ((23.502, 44), (22.498, 44), (22, 44)))
        self.add_line('sym-e8', (22, 44), (8, 36))
        self.add_bezier('sym-e9', (8, 36), ((8, 35.7), (8, 35.3), (8, 35)))
        self.add_line('sym-e10', (8, 35), (17, 14))
        self.add_line('sym-e11', (17, 14), (8, 7))
        self.add_bezier('sym-e12', (8, 7), ((8, 6.818), (8, 6.182), (8, 6)))
        self.add_bezier('sym-e13', (8, 6), ((8.018, 5.982), (8, 6.018), (8, 6)))
        self.add_bezier('sym-e14', (8, 6), ((8, 4.791), (10.098, 4.436), (12, 4)))
        self.add_line('sym-e15', (12, 4), (24, 4))
        self.add_line('sym-e16', (24, 4), (36, 4))
        self.add_bezier('sym-e17', (36, 4), ((37.902, 4.436), (40, 4.791), (40, 6)))
        self.add_bezier('sym-e18', (40, 6), ((40, 6.018), (39.982, 5.982), (40, 6)))
        self.add_bezier('sym-e19', (40, 6), ((40, 6.182), (40, 6.818), (40, 7)))
        self.add_line('sym-e20', (40, 7), (31, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
