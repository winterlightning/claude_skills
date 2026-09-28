"""Head-and-body portrait corresponding to avatar-judo-athlete-woman.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Circular face; head and shoulder ink touch with zero visible gap.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: flared gi jacket with a reverse wrap and belt end.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '5174c77c-52dd-5cd9-9502-9d515b49067c'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar judo athlete woman_5174c77c-52dd-5cd9-9502-9d515b49067c.svg'
SOURCE_HEAD_ICON_ID = 'avatar-judo-athlete-woman'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 23

class JudoAthleteWomanAvatar(Solo48):
    icon_id = 'judo-athlete-woman-avatar'
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
            self.add_bezier('tip-' + side, pt(16, 14), (pt(16, 18), pt(12, 21), pt(16, 24)))
            self.add_contour('outer-' + side, 'hair-' + side, 'tip-' + side)
            self.add_arc('fringe-' + side, (cx, 4), pt(9, 14), radius_x=9, radius_y=10, sweep=sign < 0)
            self.relate('connect', 'outer-' + side, 'fringe-' + side)
        self.relate('connect', 'outer-left', 'outer-right')
        self.relate('connect', 'fringe-left', 'fringe-right')
        self.add_arc('face', (33, 14), (15, 14), radius_x=9, radius_y=9)
        for side in ['left', 'right']:
            self.relate('connect', 'face', 'fringe-' + side)

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: flared gi jacket with a reverse wrap and belt end.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (18,top), (24, top))
        self.add_line('body-top-right', (24, top), (30,top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_polyline('body-wrap', (30,top), (24,38), (18,44))
        self.relate('connect', 'body-wrap', 'body-top-right')
        self.add_line('body-belt-end', (24,38), (28,44))
        self.relate('connect', 'body-wrap', 'body-belt-end')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
