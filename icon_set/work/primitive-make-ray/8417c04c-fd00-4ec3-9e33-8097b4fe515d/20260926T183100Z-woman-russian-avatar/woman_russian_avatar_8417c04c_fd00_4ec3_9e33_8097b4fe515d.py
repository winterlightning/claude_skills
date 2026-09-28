"""Restored the rounded fur hood.
Compared the reference and current drawing. Anatomy follows human_ref/user.svg.
Lucide user-round informed circular and shoulder construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '8417c04c-fd00-4ec3-9e33-8097b4fe515d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-russian-avatar/20260926T181831Z-thuan-mac-1/reference/woman russian_8417c04c-fd00-4ec3-9e33-8097b4fe515d.svg'
SOURCE_HEAD_ICON_ID = 'woman-russian'
AUTHOR = "gpt-6"
HEAD_BOTTOM = 30
class WomanRussianAvatar(Solo48):
    icon_id = 'woman-russian-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'russian', 'portrait', 'bust')
    def build(self):
        self.add_arc('fur-hood',(8,20),(40,20),radius_x=16)
        self.add_line('hood-left',(8,20),(8,28))
        self.add_line('hood-right',(40,20),(40,28))
        self.add_contour('hood','hood-left','fur-hood','hood-right')
        self.add_arc('face',(34,20),(14,20),radius_x=10)
        self.relate('connect','face','hood')
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
