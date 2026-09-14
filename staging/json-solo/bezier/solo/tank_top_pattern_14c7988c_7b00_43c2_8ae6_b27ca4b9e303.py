"""Tank top pattern (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14c7988c-7b00-43c2-8ae6-b27ca4b9e303'
SOURCE_PATH = 'icons-json/clothes/tank top pattern_14c7988c-7b00-43c2-8ae6-b27ca4b9e303.json'
AUTHOR = 'json_to_solo'

class TankTopPatternClothes(Solo48):
    icon_id = 'tank-top-pattern-clothes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('tank', 'top', 'pattern', 'clothes')

    def build(self):
        self.add_line('sym-e0', (8, 44), (8, 22))
        self.add_bezier('sym-e1', (8, 22), ((8.093, 21.845), (8, 22.155), (8, 22)))
        self.add_bezier('sym-e2', (8, 22), ((8.531, 21.309), (9.579, 20.791), (10, 20)))
        self.add_bezier('sym-e3', (10, 20), ((11.179, 17.773), (10.739, 14.509), (11, 12)))
        self.add_line('sym-e4', (11, 12), (12, 4))
        self.add_line('sym-e5', (12, 4), (16, 4))
        self.add_bezier('sym-e6', (16, 4), ((16.371, 6.455), (17.341, 9.073), (19, 11)))
        self.add_bezier('sym-e7', (19, 11), ((20.457, 12.697), (22.029, 13), (24, 13)))
        self.add_bezier('sym-e8', (24, 13), ((25.971, 13), (27.543, 12.697), (29, 11)))
        self.add_bezier('sym-e9', (29, 11), ((30.659, 9.073), (31.629, 6.455), (32, 4)))
        self.add_line('sym-e10', (32, 4), (36, 4))
        self.add_line('sym-e11', (36, 4), (37, 12))
        self.add_bezier('sym-e12', (37, 12), ((37.261, 14.509), (36.821, 17.773), (38, 20)))
        self.add_bezier('sym-e13', (38, 20), ((38.421, 20.791), (39.469, 21.309), (40, 22)))
        self.add_bezier('sym-e14', (40, 22), ((40, 22.155), (39.907, 21.845), (40, 22)))
        self.add_line('sym-e15', (40, 22), (40, 44))
        self.add_line('sym-e16', (40, 44), (24, 44))
        self.add_line('sym-e17', (24, 44), (8, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
