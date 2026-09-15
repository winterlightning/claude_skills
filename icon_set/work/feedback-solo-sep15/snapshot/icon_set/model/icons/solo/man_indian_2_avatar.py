"""man-indian-2: rounded shirt neckline with reference hair/headwear.
Plan: SOLO48 VRECT_L, ink (6,2)-(42,46); circular face x24,
head bottom 28, shoulders 32, zero painted gap. Shared human_ref/user.svg
supplies curved shoulders; Lucide user-round original and atomic-debug guide
cardinal arcs. Fine trim omitted at 48. Body cue: rounded shirt neckline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'ec6a97bf-8b79-5217-9903-4d323ef660ad'
SOURCE_PATH = 'pictographic-primitives/avatars/man indian_ec6a97bf-8b79-5217-9903-4d323ef660ad.svg'
SOURCE_HEAD_ICON_ID = 'man-indian-2'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class ManIndian2Avatar(Solo48):
    icon_id = 'man-indian-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'indian', '2', 'portrait', 'bust')
    def build(self):
        cx, cy, radius = 24, 16, 12
        self.add_arc('crown',(12,16),(36,16),radius_x=radius)
        self.add_arc('jaw',(36,16),(12,16),radius_x=radius)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_bezier('beard',(12,16),((16,24),(20,16),(24,20)),((28,16),(32,24),(36,16)))
        self.relate('connect','head','beard')
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

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
