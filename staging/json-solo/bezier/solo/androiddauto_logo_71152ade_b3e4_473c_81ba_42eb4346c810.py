"""Androiddauto logo (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71152ade-b3e4-473c-81ba-42eb4346c810'
SOURCE_PATH = 'icons-json/_uncategorized_03/androiddauto logo_71152ade-b3e4-473c-81ba-42eb4346c810.json'
AUTHOR = 'json_to_solo'

class AndroiddautoLogoUncategorized03(Solo48):
    icon_id = 'androiddauto-logo-uncategorized-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('androiddauto', 'logo', '_uncategorized_03')

    def build(self):
        self.add_bezier('sym-e0', (24, 4), ((24.022, 4), (23.978, 4), (24, 4)))
        self.add_bezier('sym-e1', (24, 4), ((24.623, 4), (25.537, 4.645), (26, 5)))
        self.add_line('sym-e2', (26, 5), (40, 29))
        self.add_bezier('sym-e3', (40, 29), ((40, 29.218), (40, 29.782), (40, 30)))
        self.add_bezier('sym-e4', (40, 30), ((40, 30.073), (40, 29.927), (40, 30)))
        self.add_bezier('sym-e5', (40, 30), ((40, 30.027), (40, 29.973), (40, 30)))
        self.add_bezier('sym-e6', (40, 30), ((40, 30.155), (40, 30.855), (40, 31)))
        self.add_bezier('sym-e7', (40, 31), ((40, 31.873), (38.547, 31.855), (38, 32)))
        self.add_line('sym-e8', (38, 32), (30, 31))
        self.add_line('sym-e9', (30, 31), (35, 41))
        self.add_bezier('sym-e10', (35, 41), ((34.949, 42.655), (34.423, 43.336), (33, 44)))
        self.add_line('sym-e11', (33, 44), (24, 44))
        self.add_line('sym-e12', (24, 44), (15, 44))
        self.add_bezier('sym-e13', (15, 44), ((13.577, 43.336), (13.051, 42.655), (13, 41)))
        self.add_line('sym-e14', (13, 41), (18, 31))
        self.add_line('sym-e15', (18, 31), (10, 32))
        self.add_bezier('sym-e16', (10, 32), ((9.453, 31.855), (8, 31.873), (8, 31)))
        self.add_bezier('sym-e17', (8, 31), ((8, 30.855), (8, 30.155), (8, 30)))
        self.add_bezier('sym-e18', (8, 30), ((8, 29.973), (8, 30.027), (8, 30)))
        self.add_bezier('sym-e19', (8, 30), ((8, 29.927), (8, 30.073), (8, 30)))
        self.add_bezier('sym-e20', (8, 30), ((8, 29.782), (8, 29.218), (8, 29)))
        self.add_line('sym-e21', (8, 29), (22, 5))
        self.add_bezier('sym-e22', (22, 5), ((22.463, 4.645), (23.377, 4), (24, 4)))
        self.add_bezier('sym-e23', (24, 4), ((24.022, 4), (23.978, 4), (24, 4)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
