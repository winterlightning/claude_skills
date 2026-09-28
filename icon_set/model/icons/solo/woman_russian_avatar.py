"""woman-russian: winter coat collar with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 24, shoulder top 28, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: winter coat collar. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '8417c04c-fd00-4ec3-9e33-8097b4fe515d'
SOURCE_PATH = 'pictographic-primitives/avatars/woman russian_8417c04c-fd00-4ec3-9e33-8097b4fe515d.svg'
SOURCE_HEAD_ICON_ID = 'woman-russian'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class WomanRussianAvatar(Solo48):
    icon_id = 'woman-russian-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'russian', 'portrait', 'bust')
    def build(self):
        self.add_polyline('cap',(14,14),(14,4),(34,4),(34,14))
        self.add_line('cap-bottom',(14,14),(34,14))
        self.relate('connect','cap','cap-bottom')
        self.add_arc('face',(34,14),(14,14),radius_x=10)
        self.relate('connect','face','cap-bottom')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*10,14),((24+sign*12,16),(24+sign*14,18),(24+sign*16,18)))
            self.relate('connect','hair-'+side,'face')
            self.relate('connect','hair-'+side,'cap-bottom')
            self.relate('connect','hair-'+side,'cap')
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
