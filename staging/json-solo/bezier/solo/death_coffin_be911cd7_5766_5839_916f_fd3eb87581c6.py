"""Death coffin (religion), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be911cd7-5766-5839-916f-fd3eb87581c6'
SOURCE_PATH = 'icons-json/religion/death coffin_be911cd7-5766-5839-916f-fd3eb87581c6.json'
AUTHOR = 'json_to_solo'

class DeathCoffinReligion(Solo48):
    icon_id = 'death-coffin-religion'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('death', 'coffin', 'religion')

    def build(self):
        self.add_line('sym-e0', (24, 14), (24, 30))
        self.add_line('sym-e1', (18, 19), (30, 19))
        self.add_line('sym-e2', (24, 44), (18, 44))
        self.add_bezier('sym-e3', (18, 44), ((17.754, 44), (17.246, 44), (17, 44)))
        self.add_bezier('sym-e4', (17, 44), ((15.018, 44), (14.271, 42.127), (14, 41)))
        self.add_line('sym-e5', (14, 41), (8, 16))
        self.add_bezier('sym-e6', (8, 16), ((8, 15.7), (8, 15.3), (8, 15)))
        self.add_line('sym-e7', (8, 15), (15, 5))
        self.add_bezier('sym-e8', (15, 5), ((15.025, 4.973), (16, 4.009), (16, 4)))
        self.add_bezier('sym-e9', (16, 4), ((16.16, 4), (16.852, 4.036), (17, 4)))
        self.add_line('sym-e10', (17, 4), (24, 4))
        self.add_line('sym-e11', (24, 4), (31, 4))
        self.add_bezier('sym-e12', (31, 4), ((31.148, 4.036), (31.84, 4), (32, 4)))
        self.add_bezier('sym-e13', (32, 4), ((32, 4.009), (32.975, 4.973), (33, 5)))
        self.add_line('sym-e14', (33, 5), (40, 15))
        self.add_bezier('sym-e15', (40, 15), ((40, 15.3), (40, 15.7), (40, 16)))
        self.add_line('sym-e16', (40, 16), (34, 41))
        self.add_bezier('sym-e17', (34, 41), ((33.729, 42.127), (32.982, 44), (31, 44)))
        self.add_bezier('sym-e18', (31, 44), ((30.754, 44), (30.246, 44), (30, 44)))
        self.add_line('sym-e19', (30, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
