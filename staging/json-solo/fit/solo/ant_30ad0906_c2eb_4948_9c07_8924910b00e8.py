"""Ant (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30ad0906-c2eb-4948-9c07-8924910b00e8'
SOURCE_PATH = 'icons-json/_uncategorized_03/ant_30ad0906-c2eb-4948-9c07-8924910b00e8.json'
AUTHOR = 'json_to_solo'

class Ant30ad0906(Solo48):
    icon_id = 'ant-30ad0906'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('ant', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (8, 26), (14, 22))
        self.add_line('e1', (14, 22), (20, 26))
        self.add_line('e2', (9, 41), (15, 30))
        self.add_line('e3', (15, 30), (21, 30))
        self.add_line('e4', (39, 41), (34, 31))
        self.add_line('e5', (33, 30), (27, 30))
        self.add_line('e6', (40, 26), (35, 22))
        self.add_line('e7', (34, 22), (28, 26))
        self.add_line('e8', (22, 30), (27, 30))
        self.add_line('e9', (26, 21), (22, 21))
        self.add_line('e10', (27, 21), (27, 23))
        self.add_arc('e11', (13, 4), (21, 12), radius_x=16)
        self.add_line('e12', (34, 31), (33, 30))
        self.add_arc('e13', (35, 22), (34, 22), radius_x=37)
        self.add_arc('e14', (35, 4), (28, 13), radius_x=17, sweep=False)
        self.add_arc('e15-1', (27, 30), (24, 44), radius_x=8)
        self.add_arc('e15-2', (24, 44), (21, 30), radius_x=8)
        self.add_arc('e16', (27, 30), (28, 26), radius_x=15)
        self.add_arc('e17', (27, 23), (28, 26), radius_x=6)
        self.add_line('e18', (21, 30), (20, 26))
        self.add_arc('e19', (21, 12), (28, 13), radius_x=5)
        self.add_arc('e20', (21, 12), (22, 21), radius_x=6, sweep=False)
        self.add_arc('e21', (28, 13), (26, 21), radius_x=5)
        self.add_arc('e22', (20, 26), (22, 21), radius_x=5)
        self.add_contour('c0', 'e11')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4', 'e12', 'e5')
        self.add_contour('c4', 'e6', 'e13', 'e7')
        self.add_contour('c5', 'e14')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e15-1', 'e15-2')
        self.add_contour('c8', 'e16')
        self.add_contour('c9', 'e9')
        self.add_contour('c10', 'e10', 'e17')
        self.add_contour('c11', 'e18')
        self.add_contour('c12', 'e19')
        self.add_contour('c13', 'e20')
        self.add_contour('c14', 'e21')
        self.add_contour('c15', 'e22')
        self.relate('connect', 'c0', 'c12')
        self.relate('connect', 'c0', 'c13')
        self.relate('connect', 'c12', 'c13')
        self.relate('connect', 'c1', 'c11')
        self.relate('connect', 'c1', 'c15')
        self.relate('connect', 'c11', 'c15')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c4')
        self.relate('connect', 'c10', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c12', 'c14')
        self.relate('connect', 'c12', 'c5')
        self.relate('connect', 'c14', 'c5')
        self.relate('connect', 'c13', 'c15')
        self.relate('connect', 'c13', 'c9')
        self.relate('connect', 'c15', 'c9')
