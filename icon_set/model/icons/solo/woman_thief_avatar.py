"""woman-thief: striped shirt with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 30, shoulder top 34, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: striped shirt. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '8036406b-7914-54c1-be92-c2585863d8f4'
SOURCE_PATH = 'pictographic-primitives/avatars/woman thief_8036406b-7914-54c1-be92-c2585863d8f4.svg'
SOURCE_HEAD_ICON_ID = 'woman-thief'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class WomanThiefAvatar(Solo48):
    icon_id = 'woman-thief-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('woman', 'thief', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(14,12),(34,12),radius_x=10,radius_y=8)
        for side,cx in [('left',14),('right',34)]:
            self.add_arc('lens-top-'+side,(cx,20),(cx,12),radius_x=6,radius_y=4)
            self.add_arc('lens-bottom-'+side,(cx,12),(cx,20),radius_x=6,radius_y=4)
            self.add_contour('lens-'+side,'lens-top-'+side,'lens-bottom-'+side,closed=True)
            self.relate('connect','crown','lens-'+side)
        self.add_line('bridge',(20,16),(28,16))
        self.relate('connect','bridge','lens-left')
        self.relate('connect','bridge','lens-right')
        self.add_arc('face',(34,20),(14,20),radius_x=10)
        self.relate('connect','face','lens-left')
        self.relate('connect','face','lens-right')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*10,20),((24+sign*12,22),(24+sign*14,24),(24+sign*16,24)))
            self.relate('connect','hair-'+side,'face')
            self.relate('connect','hair-'+side,'lens-'+side)
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (18, top), (24, top))
        self.add_line('body-top-right', (24, top), (30, top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_line('body-band', (8,42), (40,42))
        self.relate('connect', 'body-band', 'body-left')
        self.relate('connect', 'body-band', 'body-right')
        self.add_line('body-fastening', (24,top), (24,42))
        self.relate('connect', 'body-fastening', 'body-top')
        self.relate('connect', 'body-fastening', 'body-top-right')
        self.relate('connect', 'body-fastening', 'body-band')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
