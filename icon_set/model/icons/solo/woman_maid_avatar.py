"""woman-maid: rounded cap and dress neckline.
Distinct-avatar plan: preserve reference identity; use rounded cap and dress neckline.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 26; shoulder top 30; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '4ad15ed0-39d7-5697-9c7a-e38390e6da16'
SOURCE_PATH = 'pictographic-primitives/avatars/woman maid_4ad15ed0-39d7-5697-9c7a-e38390e6da16.svg'
SOURCE_HEAD_ICON_ID = 'woman-maid'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class WomanMaidAvatar(Solo48):
    icon_id = 'woman-maid-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('woman', 'maid', 'portrait', 'bust')
    def build(self):
        self.add_arc('puff-left',(14,16),(14,8),radius_x=4)
        self.add_line('hat-left',(14,8),(20,8))
        self.add_arc('puff-top',(20,8),(28,8),radius_x=4)
        self.add_line('hat-right',(28,8),(34,8))
        self.add_arc('puff-right',(34,8),(34,16),radius_x=4)
        self.add_line('hat-base',(34,16),(14,16))
        self.add_contour('hat','puff-left','hat-left','puff-top','hat-right','puff-right','hat-base',closed=True)
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','face','hat')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('side-hair-'+side,(24+sign*10,16),((24+sign*12,18),(24+sign*14,20),(24+sign*16,20)))
            self.relate('connect','side-hair-'+side,'face')
            self.relate('connect','side-hair-'+side,'hat')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(18,top),(24,top))
        self.add_line('body-top-right',(24,top),(30,top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_arc('body-neckline',(18,top),(30,top),radius_x=6,radius_y=6,sweep=False)
        self.relate('connect','body-neckline','body-top')
        self.relate('connect','body-neckline','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
