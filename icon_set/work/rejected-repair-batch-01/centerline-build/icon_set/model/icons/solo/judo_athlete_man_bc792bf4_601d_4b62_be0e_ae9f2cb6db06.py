"""Judo Athlete Man: overlapping gi lapel, with reference curved shoulders.

Plan: head/headwear and curved body on SOLO48 VRECT_L, ink (6,2)-(42,46).
Circular face and shoulder ink meet with zero visible gap.
Human reference: icon_set/references/human_ref/user.svg; supporting Lucide
original/user-round.svg and atomic-debug/user-round.svg supply cardinal arcs.
Preserve original head identity; omit tiny facial marks and hat trim at 48.
Paired shoulders use shared radii; source hair asymmetry remains intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'bc792bf4-601d-4b62-be0e-ae9f2cb6db06'
SOURCE_PATH = 'pictographic-primitives/avatars/judo athlete man_bc792bf4-601d-4b62-be0e-ae9f2cb6db06.svg'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24

class JudoAthleteMan(Solo48):
    icon_id = 'judo-athlete-man'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('judo', 'athlete', 'man', 'avatars')

    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('crown', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
        self.add_arc('jaw', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('head', 'crown', 'jaw', closed=True)
        self.add_bezier('fringe', (14, 14), ((16, 14), (18, 12), (20, 9)), ((24, 13), (29, 14), (34, 14)))
        self.relate('connect', 'head', 'fringe')

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: wide gi sleeves and an overlapping diagonal lapel.
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
        self.add_polyline('body-wrap', (18,top), (30,44))
        self.relate('connect', 'body-wrap', 'body-top')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
