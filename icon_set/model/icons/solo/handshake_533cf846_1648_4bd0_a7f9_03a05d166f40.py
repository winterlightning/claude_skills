"""Two hands clasp between short cuff bars. HRECT_L extremes (6,8)-(42,40). Lucide handshake informs the central hooked thumb and outer grip. Omit tiny individual finger scallops; retain two cuffs and the asymmetric overlapping hands."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '533cf846-1648-4bd0-a7f9-03a05d166f40'
SOURCE_PATH = 'pictographic-primitives/symbol/handshake_533cf846-1648-4bd0-a7f9-03a05d166f40.svg'
AUTHOR = 'gpt-6'


class Handshake(Solo48):
    icon_id = 'handshake'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('handshake', 'deal', 'agreement', 'partnership', 'business', 'trust', 'greeting', 'cooperation')

    def build(self) -> None:
        self.add_polyline('hands',(10,14),(18,8),(28,8),(38,14),(38,28),(34,30),(28,38),(22,40),(10,28),(10,14),closed=True)
        self.add_polyline('cuff-left',(4,12),(10,12),(10,14),(10,28),(10,32),(4,32))
        self.add_polyline('cuff-right',(44,12),(38,12),(38,14),(38,28),(38,32),(44,32))
        self.relate('connect','hands','cuff-left')
        self.relate('connect','hands','cuff-right')
        self.add_line('thumb-top',(28,8),(18,18))
        self.add_arc('thumb-round',(18,18),(24,24),radius_x=5,sweep=False)
        self.add_line('thumb-inner',(24,24),(30,20))
        self.add_line('grip',(30,20),(34,30))
        self.add_contour('clasp','thumb-top','thumb-round','thumb-inner','grip')
        self.relate('connect','hands','clasp')
