"""man-viking: tunic fastening with reference headwear/hair silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 30, shoulders 34, zero painted gap. human_ref/user.svg supplies
curved shoulders; Lucide user-round original and atomic-debug guide arcs.
Fine trim is omitted for clarity at 48; body cue: tunic fastening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-07/references/man-viking.svg'
SOURCE_HEAD_ICON_ID = 'man-viking'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class ManVikingAvatar(Solo48):
    icon_id = 'man-viking-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'viking', 'portrait', 'bust')
    def build(self):
        self.add_arc('cap-left',(14,20),(24,10),radius_x=10)
        self.add_arc('cap-right',(24,10),(34,20),radius_x=10)
        self.add_contour('cap','cap-left','cap-right')
        self.add_line('brim',(14,20),(34,20))
        self.relate('connect','cap','brim')
        self.add_arc('face',(34,20),(14,20),radius_x=10)
        self.relate('connect','face','brim')
        for side,sign in [('left',-1),('right',1)]:
            pt=lambda x,y:(24+sign*x,y)
            self.add_bezier('horn-'+side,pt(6,12),(pt(16,12),pt(16,8),pt(16,4)))
            self.relate('connect','cap','horn-'+side)
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
        self.add_line('body-fastening',(24,top),(24,44))
        self.relate('connect','body-fastening','body-top')
        self.relate('connect','body-fastening','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
