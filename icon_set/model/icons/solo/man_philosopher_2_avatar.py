"""man-philosopher-2: coat lapel with reference hair/headwear.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 26, shoulders 30, zero painted gap. Curved shoulders follow
human_ref/user.svg; Lucide user-round original and atomic-debug guide arcs.
Fine trim omitted at 48; clothing cue: coat lapel. Source asymmetry is retained
in headwear while the face stays centered.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'efbd83cc-eeb0-52c2-b1f7-2cb051c31e29'
SOURCE_PATH = 'pictographic-primitives/avatars/man philosopher_efbd83cc-eeb0-52c2-b1f7-2cb051c31e29.svg'
SOURCE_HEAD_ICON_ID = 'man-philosopher-2'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class ManPhilosopher2Avatar(Solo48):
    icon_id = 'man-philosopher-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'philosopher', '2', 'portrait', 'bust')
    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        self.add_bezier('beret-left',(14,16),((8,16),(8,12),(12,10)))
        self.add_bezier('beret-crown',(12,10),((18,6),(30,4),(36,4)))
        self.add_bezier('beret-right',(36,4),((42,4),(40,12),(34,16)))
        self.add_line('beret-band',(34,16),(14,16))
        self.add_contour('beret','beret-left','beret-crown','beret-right','beret-band',closed=True)
        self.add_arc('face',(34,16),(14,16),radius_x=10,radius_y=10)
        self.relate('connect','face','beret')

        # Body cue: asymmetric uniform lapel; smooth shoulders remain primary.
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
        self.add_polyline('body-wrap', (18,top), (30,44))
        self.relate('connect', 'body-wrap', 'body-top')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
