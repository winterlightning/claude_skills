"""Tank top pattern (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e2', (8, 22), (10, 20), radius_x=14)
        self.add_line('sym-e3', (10, 20), (11, 12))
        self.add_line('sym-e4', (11, 12), (12, 4))
        self.add_line('sym-e5', (12, 4), (16, 4))
        self.add_arc('sym-e6', (16, 4), (19, 11), radius_x=12, sweep=False)
        self.add_arc('sym-e7', (19, 11), (24, 13), radius_x=6, sweep=False)
        self.add_arc('sym-e8', (24, 13), (29, 11), radius_x=6, sweep=False)
        self.add_arc('sym-e9', (29, 11), (32, 4), radius_x=12, sweep=False)
        self.add_line('sym-e10', (32, 4), (36, 4))
        self.add_line('sym-e11', (36, 4), (37, 12))
        self.add_arc('sym-e12', (37, 12), (38, 20), radius_x=19, sweep=False)
        self.add_line('sym-e13', (38, 20), (40, 22))
        self.add_line('sym-e15', (40, 22), (40, 44))
        self.add_line('sym-e16', (40, 44), (24, 44))
        self.add_line('sym-e17', (24, 44), (8, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
