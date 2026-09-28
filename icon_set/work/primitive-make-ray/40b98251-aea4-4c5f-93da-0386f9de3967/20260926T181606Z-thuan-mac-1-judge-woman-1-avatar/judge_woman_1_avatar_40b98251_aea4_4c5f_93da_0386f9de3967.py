"""judge-woman-1-avatar: revised SOLO48 drawing from the claimed source.

Comparison: The rejected parted fringe and vertical apron bands did not match the open hair and robe.
Revision: Removed the fringe and replaced the bands with a clear robe V.
Human construction: icon_set/references/human_ref/user.svg; Lucide user-round supplies simple circular head and shoulder arcs.
The emitted primitives use a shared axis where the reference is symmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '40b98251-aea4-4c5f-93da-0386f9de3967'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__judge-woman-1-avatar/20260926T175531Z-thuan-mac-1/reference/judge woman_40b98251-aea4-4c5f-93da-0386f9de3967.svg'
SOURCE_HEAD_ICON_ID = 'judge-woman-1'
AUTHOR = "gpt-6"
HEAD_BOTTOM = 22

class JudgeWoman1Avatar(Solo48):
    icon_id = 'judge-woman-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('judge', 'woman', '1', 'portrait', 'bust')

    def build(self):
        cx = 24
        for side, sign in [('left', -1), ('right', 1)]:
            pt = lambda x, y: (cx + sign * x, y)
            self.add_arc('hair-' + side, (cx, 4), pt(16, 14), radius_x=16, radius_y=10, sweep=sign > 0)
            self.add_line('tip-' + side, pt(16, 14), pt(16, 18))
            self.add_contour('outer-' + side, 'hair-' + side, 'tip-' + side)
        self.relate('connect', 'outer-left', 'outer-right')
        self.add_arc('face', (32, 14), (16, 14), radius_x=8, radius_y=8)
        for side in ['left', 'right']:
            self.relate('connect', 'face', 'outer-' + side)

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
        self.add_polyline('robe-lapels',(18,top),(24,38),(30,top))
        self.relate('connect', 'robe-lapels', 'body-top')
        self.relate('connect', 'robe-lapels', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
