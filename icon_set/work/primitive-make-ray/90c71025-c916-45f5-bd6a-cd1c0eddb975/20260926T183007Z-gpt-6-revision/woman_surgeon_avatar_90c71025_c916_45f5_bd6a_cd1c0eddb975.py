"""woman-surgeon: scrub neckline with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 30, shoulder top 34, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: scrub neckline. Shared parameters own mirrored elements.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '90c71025-c916-45f5-bd6a-cd1c0eddb975'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-surgeon-avatar/20260926T182452Z-thuan-mac-1/reference/woman surgeon_90c71025-c916-45f5-bd6a-cd1c0eddb975.svg'
SOURCE_HEAD_ICON_ID = 'woman-surgeon'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class WomanSurgeonAvatar(Solo48):
    icon_id = 'woman-surgeon-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'surgeon', 'portrait', 'bust')
    def build(self):
        # The reference uses a flat surgical cap, not a peaked badge.
        self.add_polyline('cap',(12,20),(12,8),(16,4),(32,4),(36,8),(36,20))
        self.add_polyline('brim',(8,20),(12,20),(14,20),(34,20),(36,20),(40,20))
        self.relate('connect','cap','brim')
        # A centered cross is formed with the cap's top and brim as its stems.
        self.add_line('cross-stem',(24,4),(24,20))
        self.add_line('cross-arm',(20,12),(28,12))
        self.relate('connect','cross-stem','cap')
        self.relate('connect','cross-stem','brim')
        self.relate('connect','cross-arm','cross-stem')
        self.add_arc('face',(34,20),(14,20),radius_x=10)
        self.relate('connect','face','brim')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*10,20),((24+sign*12,22),(24+sign*14,24),(24+sign*16,24)))
            self.relate('connect','hair-'+side,'face')
            self.relate('connect','hair-'+side,'brim')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(12,top),radius_x=4,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (12, top), (24, top))
        self.add_line('body-top-right', (24, top), (36, top))
        self.add_arc('body-right-shoulder',(36,top),(40,42),radius_x=4,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_polyline('body-tie', (12, top), (24,44), (36, top))
        self.relate('connect', 'body-tie', 'body-top')
        self.relate('connect', 'body-tie', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
