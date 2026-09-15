"""woman-cap-1: casual V neck shirt with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 26, shoulder top 30, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: casual V neck shirt. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '7bab8ae5-030d-5dab-b99e-4b476e5948a4'
SOURCE_PATH = 'pictographic-primitives/avatars/woman cap_7bab8ae5-030d-5dab-b99e-4b476e5948a4.svg'
SOURCE_HEAD_ICON_ID = 'woman-cap-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class WomanCap1Avatar(Solo48):
    icon_id = 'woman-cap-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('woman', 'cap', '1', 'portrait', 'bust')
    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        self.add_arc('cap-left',(12,16),(24,4),radius_x=12)
        self.add_arc('cap-right',(24,4),(36,16),radius_x=12)
        self.add_contour('cap','cap-left','cap-right')
        self.add_polyline('brim',(8,16),(12,16),(14,16),(34,16),(36,16))
        self.relate('connect','cap','brim')
        self.add_arc('face',(34,16),(14,16),radius_x=10,radius_y=10)
        self.relate('connect','face','brim')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*10,16),((24+sign*12,18),(24+sign*14,20),(24+sign*16,20)))
            self.relate('connect','hair-'+side,'face')
            self.relate('connect','hair-'+side,'brim')

        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(12,top),radius_x=4,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(12,top),(24,top))
        self.add_line('body-top-right',(24,top),(36,top))
        self.add_arc('body-right-shoulder',(36,top),(40,42),radius_x=4,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_polyline('body-collar',(12,top),(24,40),(36,top))
        self.relate('connect','body-collar','body-top')
        self.relate('connect','body-collar','body-top-right')
        self.add_line('body-jacket-opening',(24,40),(24,44))
        self.relate('connect','body-jacket-opening','body-collar')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
