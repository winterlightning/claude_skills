"""Head-and-body portrait corresponding to avatar-judo-athlete-woman.

AVATAR48 construction on VRECT_L: visible ink (6,0)-(42,48).
Head bottom 22; shoulder top 30; measured head/body ink gap 4.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs and tangent shoulders. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Shared axis x24 and radius10 shoulders.
"""
from ...keyshapes import Keyshape
from ._base import Avatar48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/avatar-judo-athlete-woman.svg'
SOURCE_HEAD_ICON_ID = 'avatar-judo-athlete-woman'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 22

class JudoAthleteWomanAvatar(Avatar48):
    icon_id = 'judo-athlete-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/avatars'
    aliases = ()
    keywords = ('avatar', 'judo', 'athlete', 'woman', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        # Plan: mirrored hair sweeps, an open face, and a shared centre part.
        for side, sign in [('left',-1),('right',1)]:
            pt = lambda x,y: (cx+sign*x,y)
            self.add_arc('hair-'+side,(cx,2),pt(16,12),radius_x=16,radius_y=10,sweep=sign>0)
            self.add_bezier('tip-'+side,pt(16,12),(pt(16,16),pt(12,19),pt(16,22)))
            self.add_contour('outer-'+side,'hair-'+side,'tip-'+side)
            self.add_arc('fringe-'+side,(cx,2),pt(9,12),radius_x=9,radius_y=10,sweep=sign<0)
            self.relate('connect','outer-'+side,'fringe-'+side)
        self.relate('connect','outer-left','outer-right')
        self.relate('connect','fringe-left','fringe-right')
        self.add_arc('face',(33,12),(15,12),radius_x=9,radius_y=10)
        for side in ['left','right']:
            self.relate('connect','face','fringe-'+side)

        # Shoulders are a separate symbol: mirrored tangent quarter circles.
        # The jaw bottom lies over the plateau, certifying the exact ink gap.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        left, right, bottom, shoulder_radius = 8, 40, 46, 10
        self.add_line('body-left',(left,bottom),(left,top+shoulder_radius))
        self.add_arc('body-shoulder-left',(left,top+shoulder_radius),(left+shoulder_radius,top),radius_x=shoulder_radius)
        self.add_line('body-top',(left+shoulder_radius,top),(right-shoulder_radius,top))
        self.add_arc('body-shoulder-right',(right-shoulder_radius,top),(right,top+shoulder_radius),radius_x=shoulder_radius)
        self.add_line('body-right',(right,top+shoulder_radius),(right,bottom))
        self.add_contour('body','body-left','body-shoulder-left','body-top','body-shoulder-right','body-right')
