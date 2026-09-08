"""Low crouching mouse with a round haunch, circular ear, eye, short pointed muzzle and exposed curling tail. Lucide rat informs the rodent silhouette; proportions are redrawn for recognition."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1fc63f6-12db-5dd9-8649-42850ceca103'
SOURCE_PATH = 'pictographic-primitives/animals/mouse 1_d1fc63f6-12db-5dd9-8649-42850ceca103.svg'
AUTHOR = 'gpt-6'


class CrouchingMouse(Solo48):
    icon_id = 'crouching-mouse'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('crouching', 'mouse')

    def build(self) -> None:
        # HRECT_L centerline extremes: (2,8)-(46,40).
        self.add_arc('back',(10,28),(25,15),radius_x=15,radius_y=13)
        self.add_arc('ear-top',(25,15),(39,15),radius_x=7)
        self.add_arc('ear-side',(39,15),(37,21),radius_x=7)
        self.add_line('snout',(37,21),(46,30))
        self.add_arc('muzzle',(46,30),(39,35),radius_x=7,radius_y=5)
        self.add_line('belly',(39,35),(18,35))
        self.add_arc('rump',(18,35),(10,28),radius_x=8,radius_y=7)
        self.add_contour('body','back','ear-top','ear-side','snout','muzzle','belly','rump',closed=True)
        self.add_arc('ear-fold',(25,15),(32,22),radius_x=7,sweep=False)
        self.relate('connect','body','ear-fold')
        self.add_dot('eye',(35,28))
        self.add_arc('tail-left',(10,28),(2,34),radius_x=8,radius_y=6,sweep=False)
        self.add_arc('tail-bottom',(2,34),(10,40),radius_x=8,radius_y=6,sweep=False)
        self.add_line('tail-tip',(10,40),(14,40))
        self.add_contour('tail','tail-left','tail-bottom','tail-tip')
        self.relate('connect','body','tail')
