"""pajamas: soft sleepwear neckline with reference headwear/hair silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 24, shoulders 28, zero painted gap. human_ref/user.svg supplies
curved shoulders; Lucide user-round original and atomic-debug guide arcs.
Fine trim is omitted for clarity at 48; body cue: soft sleepwear neckline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '73e9def9-0b2e-5cf8-9165-59cc0218b7a6'
SOURCE_PATH = 'pictographic-primitives/avatars/pajamas_73e9def9-0b2e-5cf8-9165-59cc0218b7a6.svg'
SOURCE_HEAD_ICON_ID = 'pajamas'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class PajamasAvatar(Solo48):
    icon_id = 'pajamas-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('pajamas', 'portrait', 'bust')
    def build(self):
        cx, cy, radius = 24, 14, 10
        self.add_arc('crown',(14,14),(34,14),radius_x=radius)
        self.add_arc('jaw',(34,14),(14,14),radius_x=radius)
        self.add_contour('head','crown','jaw',closed=True)
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
