"""Prisoner with Ball and Chain.

Symbol plan: Frontal stick prisoner and attached ankle ball, head r5 at16,11; torso24 gives exact gap4. Extremes6,6,42,42. Single curved chain replaces individual links.
Construction references: Shared human_ref/full_body_ref.png: circle head, simple limbs. Lucide spline: connecting curve between objects.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0da7938b-98e2-597a-b55d-48e9dd223584'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__prisoner-attached-to-ball-and-chain/20260927T153803Z-thuan-mac-1/reference/prisoner ball_0da7938b-98e2-597a-b55d-48e9dd223584.svg'
AUTHOR = 'gpt-6'


class PrisonerAttachedToBallAndChain(Solo48):
    icon_id = 'prisoner-attached-to-ball-and-chain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('prisoner', 'attached', 'to', 'ball', 'and', 'chain')

    def build(self):
        # Rounded head, lowered arms, separate legs, and an ankle chain to the ball.
        self.add_arc('head-top',(11,11),(21,11),radius_x=5)
        self.add_arc('head-bottom',(21,11),(11,11),radius_x=5)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('torso',(16,24),(16,34))
        self.add_line('shoulders',(8,24),(24,24))
        self.add_polyline('left-arm',(8,24),(6,32))
        self.add_polyline('right-arm',(22,24),(22,32))
        self.add_polyline('legs',(10,42),(16,34),(22,42))
        self.add_arc('ball-top',(30,36),(42,36),radius_x=6)
        self.add_arc('ball-bottom',(42,36),(30,36),radius_x=6)
        self.add_contour('ball','ball-top','ball-bottom',closed=True)
        self.add_line('chain',(22,42),(30,36))
        for a,b in (('torso','shoulders'),('torso','legs'),('shoulders','left-arm'),
                    ('shoulders','right-arm'),('legs','chain'),('chain','ball')):
            self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
