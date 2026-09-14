"""Woman with a flared bob with rounded evening neckline.

Plan: separate head/hair or headwear symbol, painted head/body contact, curved torso
with rounded evening neckline. SOLO48 VRECT_L visible ink (6,2)-(42,46);
centerline extremes (8,4)-(40,44). Head and body ink touch on the shoulder plateau.
Primary source supplies the hair/headwear silhouette; fine facial marks,
hat stitching and microdetails are omitted to preserve openings at 48.
Human reference: icon_set/references/human_ref/user.svg for proportions,
curved shoulders and open bottom. Lucide original/user-round.svg and its
atomic-debug counterpart inform cardinal arcs and tangent joins; original/shirt.svg
and atomic-debug/shirt.svg inform the clothing cue. Intentional source hairstyle
or hat asymmetry is retained, with mirrored shoulders where appropriate.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-02/references/casino-player-woman.svg'
SOURCE_HEAD_ICON_ID = 'casino-player-woman'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 23


class CasinoPlayerWomanAvatar(Solo48):
    icon_id = 'casino-player-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('casino', 'player', 'woman', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        for side,sign in [('left',-1),('right',1)]:
            pt=lambda x,y:(24+sign*x,y)
            self.add_arc('hair-'+side,(24,4),pt(16,14),radius_x=16,radius_y=10,sweep=sign>0)
            self.add_bezier('tip-'+side,pt(16,14),(pt(16,18),pt(12,21),pt(16,24)))
            self.add_contour('outer-'+side,'hair-'+side,'tip-'+side)
            self.add_arc('fringe-'+side,(24,4),pt(9,14),radius_x=9,radius_y=10,sweep=sign<0)
            self.relate('connect','outer-'+side,'fringe-'+side)
        self.relate('connect','outer-left','outer-right')
        self.relate('connect','fringe-left','fringe-right')
        self.add_arc('face',(33,14),(15,14),radius_x=9,radius_y=9)
        for side in ['left','right']:
            self.relate('connect','face','fringe-'+side)

        # Body cue: rounded evening neckline; smooth shoulders remain primary.
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
