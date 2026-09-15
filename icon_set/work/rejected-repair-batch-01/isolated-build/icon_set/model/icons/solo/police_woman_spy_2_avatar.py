"""police-woman-spy-2: curved coat collar and reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) allows vertical headwear budget.
Face centered x24 with equal circular radii; head bottom 28, shoulders 32,
zero painted gap. Shared human_ref/user.svg supplies curved shoulders;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine hat emblems and facial microdetails omitted for clarity at 48.
Body cue: curved coat collar. Hair and feather asymmetry follow the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-08/references/police-woman-spy-2.svg'
SOURCE_HEAD_ICON_ID = 'police-woman-spy-2'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class PoliceWomanSpy2Avatar(Solo48):
    icon_id = 'police-woman-spy-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('police', 'woman', 'spy', '2', 'portrait', 'bust')
    def build(self):
        self.add_polyline('cap',(12,16),(8,12),(24,4),(40,12),(36,16))
        self.add_arc('face',(36,16),(12,16),radius_x=12)
        self.relate('connect','cap','face')
        self.add_polyline('mask',(12,16),(24,20),(36,16))
        self.relate('connect','mask','cap')
        self.relate('connect','mask','face')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*12,16),((24+sign*12,22),(24+sign*14,24),(24+sign*16,26)))
            self.relate('connect','hair-'+side,'cap')
            self.relate('connect','hair-'+side,'face')
            self.relate('connect','hair-'+side,'mask')
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
