"""man-surgeon: scrub neckline with reference hair/headwear.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 26, shoulders 30, zero painted gap. Curved shoulders follow
human_ref/user.svg; Lucide user-round original and atomic-debug guide arcs.
Fine trim omitted at 48; clothing cue: scrub neckline. Source asymmetry is retained
in headwear while the face stays centered.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'ad6b9cf9-9367-5b4b-92ac-ee4f3268da38'
SOURCE_PATH = 'pictographic-primitives/avatars/man surgeon_ad6b9cf9-9367-5b4b-92ac-ee4f3268da38.svg'
SOURCE_HEAD_ICON_ID = 'man-surgeon'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class ManSurgeonAvatar(Solo48):
    icon_id = 'man-surgeon-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'surgeon', 'portrait', 'bust')
    def build(self):
        self.add_polyline('cap',(14,16),(14,4),(34,4),(34,16),(14,16))
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','face','cap')
        self.add_polyline('tie',(40,12),(34,16),(40,20))
        self.relate('connect','tie','cap')
        self.relate('connect','tie','face')
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
