"""Two mirrored swans make a heart between their necks. Bounds (2,8)-(46,40). Lucide bird informs open body contours. Beaks and eyes omitted to preserve the central opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea964fee-5bf0-42a1-bfb2-b6f7dbff3fea'
SOURCE_PATH = 'pictographic-primitives/animals/swan couple_ea964fee-5bf0-42a1-bfb2-b6f7dbff3fea.svg'
AUTHOR = 'gpt-6'


class SwanCoupleHeart(Solo48):
    icon_id = 'swan-couple-heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('swan', 'couple', 'heart', 'love', 'pair', 'romance', 'birds', 'wedding')

    def build(self) -> None:
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            tag='left' if side<0 else 'right'
            self.add_arc(tag+'-head-inner',p(3,14),p(9,8),radius_x=6,sweep=(side>0))
            self.add_arc(tag+'-head-outer',p(9,8),p(15,14),radius_x=6,sweep=(side>0))
            self.add_arc(tag+'-neck',p(15,14),p(8,27),radius_x=17,sweep=(side>0))
            self.add_arc(tag+'-breast',p(8,27),p(0,34),radius_x=12,sweep=(side>0))
            self.add_arc(tag+'-body-inner',p(0,34),p(9,40),radius_x=9,radius_y=6,sweep=(side<0))
            self.add_line(tag+'-body-base',p(9,40),p(12,40))
            self.add_arc(tag+'-body-outer',p(12,40),p(22,30),radius_x=10,sweep=(side<0))
            self.add_line(tag+'-tail',p(22,30),p(22,26))
            self.add_arc(tag+'-wing',p(22,26),p(9,28),radius_x=15,radius_y=8,sweep=(side>0))
            self.add_contour(tag+'-swan',*[tag+'-'+n for n in ('head-inner','head-outer','neck','breast','body-inner','body-base','body-outer','tail','wing')])
        self.relate('connect','left-swan','right-swan')
