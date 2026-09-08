"""Whole cockatoo with swept crest, dot eye, hooked beak, curved wing and long tail. Lucide bird informs a closed avian silhouette; source crest and beak are retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9442c76e-74c3-56b2-8dda-349c7fd38db5'
SOURCE_PATH = 'pictographic-primitives/animals/parrot_9442c76e-74c3-56b2-8dda-349c7fd38db5.svg'
AUTHOR = 'gpt-6'


class Cockatoo(Solo48):
    icon_id = 'cockatoo'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('cockatoo',)

    def build(self) -> None:
        # VRECT_XL centerline extremes: (5,2)-(43,46).
        self.add_arc('back',(5,46),(12,24),radius_x=40)
        self.add_arc('nape',(12,24),(12,16),radius_x=12)
        self.add_arc('crest-back',(12,16),(5,2),radius_x=20,sweep=False)
        self.add_arc('crest-bridge',(5,2),(16,2),radius_x=8,radius_y=6,sweep=False)
        self.add_line('crest-front',(16,2),(24,10))
        self.add_arc('head',(24,10),(35,20),radius_x=11,radius_y=10)
        self.add_arc('beak-top',(35,20),(43,28),radius_x=8)
        self.add_arc('beak-tip',(43,28),(38,34),radius_x=8)
        self.add_line('hook',(38,34),(35,28))
        self.add_arc('throat',(35,28),(32,36),radius_x=12)
        self.add_arc('belly',(32,36),(16,42),radius_x=16,radius_y=6)
        self.add_line('tail',(16,42),(5,46))
        self.add_contour('outline','back','nape','crest-back','crest-bridge','crest-front','head','beak-top','beak-tip','hook','throat','belly','tail',closed=True)
        self.add_dot('eye',(24,20))
        self.add_arc('wing',(23,29),(16,42),radius_x=16)
        self.relate('connect','outline','wing')
