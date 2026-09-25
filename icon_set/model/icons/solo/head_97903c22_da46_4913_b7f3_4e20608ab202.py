"""head: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97903c22-da46-4913-b7f3-4e20608ab202'
SOURCE_PATH = 'pictographic-primitives/symbol/head_97903c22-da46-4913-b7f3-4e20608ab202.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Head(Solo48):
    icon_id = 'head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('head', 'symbol')

    def build(self):
        # VRECT_L (8,4)-(40,44); circle cranium and tangent nape, no detached gap.
        # Construction reference: human_ref/user.svg: circular head; continuous anatomical neck
        face_right = True

        def p(x,y): return (48-x,y) if face_right else (x,y)
        self.add_line('neck-back',p(36,44),p(36,32))
        self.add_bezier('nape',p(36,32),(p(36,27),p(40,25),p(40,18)))
        self.add_arc('cranium',p(40,18),p(12,18),radius_x=14,sweep=face_right)
        self.add_line('nose-slope',p(12,18),p(8,28))
        self.add_line('nose-base',p(8,28),p(12,28))
        self.add_line('face',p(12,28),p(12,34))
        self.add_arc('chin',p(12,34),p(16,38),radius_x=4,sweep=face_right)
        self.add_line('jaw',p(16,38),p(20,38))
        self.add_line('neck-front',p(20,38),p(20,44))
        self.add_contour('outline','neck-back','nape','cranium','nose-slope','nose-base','face','chin','jaw','neck-front')
