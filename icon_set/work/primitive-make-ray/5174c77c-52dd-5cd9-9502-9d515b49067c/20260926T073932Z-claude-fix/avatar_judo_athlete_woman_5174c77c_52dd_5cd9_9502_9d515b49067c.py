"""Head-and-body portrait corresponding to avatar-judo-athlete-woman.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Circular face; head and shoulder ink touch with zero visible gap.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: flared gi jacket with a reverse wrap and belt end.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '5174c77c-52dd-5cd9-9502-9d515b49067c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__avatar-judo-athlete-woman/20260926T073831Z-thuan-mac/reference/avatar judo athlete woman_5174c77c-52dd-5cd9-9502-9d515b49067c.svg'
SOURCE_HEAD_ICON_ID = 'avatar-judo-athlete-woman'
AUTHOR = 'claude-opus-5-5'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 22

class AvatarJudoAthleteWoman(Solo48):
    icon_id = 'avatar-judo-athlete-woman'
    human_construction = 'bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('avatar', 'judo', 'athlete', 'woman', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        for side, sign in [('left', -1), ('right', 1)]:
            pt = lambda x, y: (cx + sign * x, y)
            self.add_arc('hair-' + side, (cx, 4), pt(16, 14), radius_x=16, radius_y=10, sweep=sign > 0)
            self.add_bezier('tip-' + side, pt(16, 14), (pt(16, 17), pt(16, 19), pt(16, 20)))
            self.add_contour('outer-' + side, 'hair-' + side, 'tip-' + side)
            self.add_arc('fringe-' + side, (cx, 4), pt(8, 14), radius_x=8, radius_y=10, sweep=sign < 0)
            self.relate('connect', 'outer-' + side, 'fringe-' + side)
        self.relate('connect', 'outer-left', 'outer-right')
        self.relate('connect', 'fringe-left', 'fringe-right')
        self.add_arc('face', (32, 14), (16, 14), radius_x=8, radius_y=8)
        for side in ['left', 'right']:
            self.relate('connect', 'face', 'fringe-' + side)
        # Revision per review: the body curve changes from tall arched sides to sloping shoulders:
        # a short flat neckline (20, 26)-(28, 26), quarter ellipses (rx 12, ry 10) sloping down to
        # the sides (8, 36)/(40, 36), and straight sides to y 44. The gi's wrap is one diagonal
        # from the neckline's right end (28, 26) down to (18, 44). Face-body contact unchanged.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side', (8, 44), (8, 36))
        self.add_arc('body-left-shoulder', (8, 36), (20, top), radius_x=12, radius_y=36 - top)
        self.add_line('body-top', (20, top), (24, top))
        self.add_line('body-top-right', (24, top), (28, top))
        self.add_arc('body-right-shoulder', (28, top), (40, 36), radius_x=12, radius_y=36 - top)
        self.add_line('body-right-side', (40, 36), (40, 44))
        self.add_contour('body', 'body-left-side', 'body-left-shoulder', 'body-top', 'body-top-right',
                         'body-right-shoulder', 'body-right-side')
        self.add_line('body-wrap', (28, top), (18, 44))
        self.relate('connect', 'body', 'body-wrap')
        self.relate('connect', 'face', 'body')
