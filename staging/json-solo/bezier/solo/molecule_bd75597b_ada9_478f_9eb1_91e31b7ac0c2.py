"""Molecule (science), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd75597b-ada9-478f-9eb1-91e31b7ac0c2'
SOURCE_PATH = 'icons-json/science/molecule_bd75597b-ada9-478f-9eb1-91e31b7ac0c2.json'
AUTHOR = 'json_to_solo'

class Molecule(Solo48):
    icon_id = 'molecule'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('molecule', 'science')

    def build(self):
        self.add_line('e0', (35, 29), (29, 21))
        self.add_line('e1', (19, 21), (14, 29))
        self.add_arc('e2-top', (16, 16), (32, 16), radius_x=8)
        self.add_arc('e2-bottom', (32, 16), (16, 16), radius_x=8)
        self.add_arc('e3-top', (4, 34), (16, 34), radius_x=6)
        self.add_arc('e3-bottom', (16, 34), (4, 34), radius_x=6)
        self.add_bezier('e4', (35, 29), ((36.445, 28.562), (37.727, 28.185), (39.264, 28.455)), ((41.809, 28.884), (43.991, 31.478), (43.991, 33.853)), ((43.991, 33.969), (44, 34.085), (44, 34.209)), ((44, 34.211), (44, 34.213), (44, 34.215)), ((44, 34.375), (43.991, 34.543), (43.991, 34.703)), ((43.991, 37.297), (41.264, 40), (38.455, 40)), ((38.453, 40), (38.451, 40), (38.449, 40)), ((38.333, 40), (38.216, 39.991), (38.1, 39.983)), ((34.445, 39.983), (32.045, 36.32), (32.473, 33.238)), ((32.7, 31.571), (33.882, 30.255), (35, 29)))
        self.add_contour('c0', 'e4', closed=True)
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'e2')
        self.relate('connect', 'c2', 'e2')
        self.relate('connect', 'c2', 'e3')
