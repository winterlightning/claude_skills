"""japanese-woman-avatar: revised SOLO48 drawing from the claimed source.

Comparison: The rejected portrait lost the asymmetric bob, flower, and one sided kimono wrap.
Revision: Uneven bob lengths, temple ornament, and a single slanted kimono lapel restore the main cues.
Human construction: icon_set/references/human_ref/user.svg; Lucide user-round supplies simple circular head and shoulder arcs.
The emitted primitives use a shared axis where the reference is symmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'd8f7770b-d9fb-48cc-9814-dcf0af46b402'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__japanese-woman-avatar/20260926T175531Z-thuan-mac-1/reference/japanese woman_d8f7770b-d9fb-48cc-9814-dcf0af46b402.svg'
SOURCE_HEAD_ICON_ID = 'japanese-woman'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 22

class JapaneseWomanAvatar(Solo48):
    icon_id = 'japanese-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('japanese', 'woman', 'portrait', 'bust')

    def build(self):
        cx = 24
        for side, sign in [('left', -1), ('right', 1)]:
            pt = lambda x, y: (cx + sign * x, y)
            self.add_arc('hair-' + side, (cx, 4), pt(16, 14), radius_x=16, radius_y=10, sweep=sign > 0)
            self.add_line('tip-' + side,pt(16,14),pt(16,22 if side == 'left' else 17))
            self.add_contour('outer-' + side, 'hair-' + side, 'tip-' + side)
            self.add_arc('fringe-' + side, (cx, 4), pt(8, 14), radius_x=8, radius_y=10, sweep=sign < 0)
            self.relate('connect', 'outer-' + side, 'fringe-' + side)
        self.relate('connect', 'outer-left', 'outer-right')
        self.relate('connect', 'fringe-left', 'fringe-right')
        self.add_dot('flower-ornament',(38,7))
        self.relate('connect','flower-ornament','outer-right')
        self.add_arc('face', (32, 14), (16, 14), radius_x=8, radius_y=8)
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
        self.add_line('kimono-lapel',(32,top),(27,44))
        self.relate('connect','kimono-lapel','body-top-right')


        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
