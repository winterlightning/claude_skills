"""Judge Man: paired judicial robe bands, with reference curved shoulders.

Plan: head/headwear and curved body on SOLO48 VRECT_L, ink (6,2)-(42,46).
Circular face and shoulder ink meet with zero visible gap.
Human reference: icon_set/references/human_ref/user.svg; supporting Lucide
original/user-round.svg and atomic-debug/user-round.svg supply cardinal arcs.
Preserve original head identity; omit tiny facial marks and hat trim at 48.
Paired shoulders use shared radii; source hair asymmetry remains intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e8fb8e23-2308-4fdf-ac4b-d8a8d044a6df'
SOURCE_PATH = 'icons-json/avatars/judge man_e8fb8e23-2308-4fdf-ac4b-d8a8d044a6df.json'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 23

class JudgeMan(Solo48):
    icon_id = 'judge-man'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('judge', 'man', 'avatars')

    def build(self):
        cx = 24
        for side, sign in [('left', -1), ('right', 1)]:
            pt = lambda x, y: (cx + sign * x, y)
            self.add_arc('hair-' + side, (cx, 4), pt(16, 14), radius_x=16, radius_y=10, sweep=sign > 0)
            self.add_line('tip-' + side, pt(16, 14), pt(16, 24))
            self.add_contour('outer-' + side, 'hair-' + side, 'tip-' + side)
            self.add_arc('fringe-' + side, (cx, 4), pt(9, 14), radius_x=9, radius_y=10, sweep=sign < 0)
            self.relate('connect', 'outer-' + side, 'fringe-' + side)
        self.relate('connect', 'outer-left', 'outer-right')
        self.relate('connect', 'fringe-left', 'fringe-right')
        self.add_arc('face', (33, 14), (15, 14), radius_x=9, radius_y=9)
        for side in ['left', 'right']:
            self.relate('connect', 'face', 'fringe-' + side)

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
        self.add_line('body-band-left',(18,top),(18,44))
        self.add_line('body-band-right',(30,top),(30,44))
        self.relate('connect','body-band-left','body-top')
        self.relate('connect','body-band-right','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
