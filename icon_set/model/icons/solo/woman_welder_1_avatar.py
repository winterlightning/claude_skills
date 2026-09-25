"""woman-welder-1: protective apron with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 28, shoulder top 32, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: protective apron. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'f0c8993d-8aa9-4dd6-a53c-1b270d7ea0a8'
SOURCE_PATH = 'pictographic-primitives/avatars/woman welder_f0c8993d-8aa9-4dd6-a53c-1b270d7ea0a8.svg'
SOURCE_HEAD_ICON_ID = 'woman-welder-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class WomanWelder1Avatar(Solo48):
    icon_id = 'woman-welder-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'welder', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(12,16),(36,16),radius_x=12)
        self.add_arc('jaw',(36,16),(12,16),radius_x=12)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_line('visor',(21,16),(27,16))
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*12,16),((24+sign*12,18),(24+sign*14,20),(24+sign*16,20)))
            self.relate('connect','hair-'+side,'head')
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
        self.add_polyline('body-bib',(18,top),(18,44),(30,44),(30,top))
        self.relate('connect','body-bib','body-top')
        self.relate('connect','body-bib','body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
