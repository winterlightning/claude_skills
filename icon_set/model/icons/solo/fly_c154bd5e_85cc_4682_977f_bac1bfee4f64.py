'Hang glider: full-width smooth wing tips, continuous trailing edge and genuine shared harness attachments.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c154bd5e-85cc-4682-977f-bac1bfee4f64'
SOURCE_PATH = 'pictographic-primitives/animals/fly_c154bd5e-85cc-4682-977f-bac1bfee4f64.svg'
AUTHOR = 'gpt-6'


class HangGliderWithHarness(Solo48):
    icon_id = 'hang-glider-with-harness'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('hang', 'glider', 'with', 'harness')

    def build(self) -> None:
        self.add_line('wing-left',(24,8),(5,24))
        self.add_bezier('tip-left',(5,24),((4,25),(4,28),(4,30)))
        self.add_polyline('trailing-left',(4,30),(16,28),(24,26))
        self.add_polyline('trailing-right',(24,26),(32,28),(44,30))
        self.add_bezier('tip-right',(44,30),((44,28),(44,25),(43,24)))
        self.add_line('wing-right',(43,24),(24,8))
        self.add_contour('left','wing-left','tip-left')
        self.add_contour('right','tip-right','wing-right')
        for a,b in (('left','right'),('left','trailing-left'),('trailing-left','trailing-right'),('trailing-right','right')):self.relate('connect',a,b)
        self.add_polyline('harness',(16,28),(18,36),(24,40),(30,36),(32,28))
        self.relate('connect','harness','trailing-left')
        self.relate('connect','harness','trailing-right')
