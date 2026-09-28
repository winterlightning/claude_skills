"""greek-woman-1-avatar: revised SOLO48 drawing from the claimed source.

Comparison: The rejected symmetric generic Y collar obscured the long locks and draped garment.
Revision: Lengthened the side hair and used one tunic drape instead of the Y collar.
Human construction: icon_set/references/human_ref/user.svg; Lucide user-round supplies simple circular head and shoulder arcs.
The emitted primitives use a shared axis where the reference is symmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '79364157-f679-4191-9b80-a86b9182f682'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__greek-woman-1-avatar/20260926T175531Z-thuan-mac-1/reference/greek woman_79364157-f679-4191-9b80-a86b9182f682.svg'
SOURCE_HEAD_ICON_ID = 'greek-woman-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26

class GreekWoman1Avatar(Solo48):
    icon_id = 'greek-woman-1-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('greek', 'woman', '1', 'portrait', 'bust')

    def build(self):
        cx = 24
        for side, sign in [('left', -1), ('right', 1)]:
            pt = lambda x, y: (cx + sign * x, y)
            self.add_arc('hair-' + side, (cx, 4), pt(16, 18), radius_x=16, radius_y=14, sweep=sign > 0)
            self.add_line('tip-' + side, pt(16,18), pt(16,26))
            self.add_contour('outer-' + side, 'hair-' + side, 'tip-' + side)
            self.add_arc('fringe-' + side, (cx, 4), pt(8, 18), radius_x=8, radius_y=14, sweep=sign < 0)
            self.relate('connect', 'outer-' + side, 'fringe-' + side)
        self.relate('connect', 'outer-left', 'outer-right')
        self.relate('connect', 'fringe-left', 'fringe-right')
        self.add_arc('face', (32, 18), (16, 18), radius_x=8, radius_y=8)
        for side in ['left', 'right']:
            self.relate('connect', 'face', 'fringe-' + side)

        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (16,top), (24, top))
        self.add_line('body-top-right', (24, top), (32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_line('tunic-drape',(32,top),(28,44))
        self.relate('connect','tunic-drape','body-top-right')


        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
