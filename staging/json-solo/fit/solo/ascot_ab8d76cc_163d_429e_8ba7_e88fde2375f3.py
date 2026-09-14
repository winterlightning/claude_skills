"""Ascot (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('sym-e2', (40, 35), (40, 36))
        self.add_line('sym-e3', (40, 36), (26, 44))
        self.add_arc('sym-e4-1', (26, 44), (25, 44), radius_x=29, sweep=False)
        self.add_line('sym-e4-2', (25, 44), (24, 44))
        self.add_arc('sym-e7-1', (24, 44), (23, 44), radius_x=29, sweep=False)
        self.add_arc('sym-e7-2', (23, 44), (22, 44), radius_x=27, sweep=False)
        self.add_line('sym-e8', (22, 44), (8, 36))
        self.add_line('sym-e9', (8, 36), (8, 35))
        self.add_line('sym-e10', (8, 35), (17, 14))
        self.add_line('sym-e11', (17, 14), (8, 7))
        self.add_line('sym-e12', (8, 7), (8, 6))
        self.add_line('sym-e14', (8, 6), (12, 4))
        self.add_line('sym-e15', (12, 4), (24, 4))
        self.add_line('sym-e16', (24, 4), (36, 4))
        self.add_line('sym-e17', (36, 4), (40, 6))
        self.add_arc('sym-e19', (40, 6), (40, 7), radius_x=20, sweep=False)
        self.add_line('sym-e20', (40, 7), (31, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e7-1', 'sym-e7-2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20')
