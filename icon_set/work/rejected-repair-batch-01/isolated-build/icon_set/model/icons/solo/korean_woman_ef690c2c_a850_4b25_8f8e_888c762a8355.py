"""Korean Woman: asymmetric wrap jacket, with reference curved shoulders.

Plan: head/headwear and curved body on SOLO48 VRECT_L, ink (6,2)-(42,46).
Face center is (24,14), radius 10; shoulder ink touches the face.
The side bun is reduced to radius 3 to preserve the centered face and keyshape.
Human reference: icon_set/references/human_ref/user.svg; supporting Lucide
original/user-round.svg and atomic-debug/user-round.svg supply cardinal arcs.
Preserve original head identity; omit tiny facial marks and hat trim at 48.
Paired shoulders use shared radii; source hair asymmetry remains intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ef690c2c-a850-4b25-8f8e-888c762a8355'
SOURCE_PATH = 'pictographic-primitives/avatars/korean woman_ef690c2c-a850-4b25-8f8e-888c762a8355.svg'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24

class KoreanWoman(Solo48):
    icon_id = 'korean-woman'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('korean', 'woman', 'avatars')

    def build(self):
        cx, cy, radius = 24, 14, 10
        self.add_arc('crown',(cx-radius,cy),(cx+radius,cy),radius_x=radius)
        self.add_arc('jaw',(cx+radius,cy),(cx-radius,cy),radius_x=radius)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_bezier('fringe',(14,14),((20,16),(24,12),(27,9)),((29,12),(32,14),(34,14)))
        self.relate('connect','head','fringe')
        self.add_arc('bun-top',(34,14),(40,14),radius_x=3)
        self.add_arc('bun-bottom',(40,14),(34,14),radius_x=3)
        self.add_contour('side-bun','bun-top','bun-bottom',closed=True)
        self.relate('connect','head','side-bun')
        self.relate('connect','fringe','side-bun')
        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: wide flowing sleeves and a short crossed jacket tie.
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
        self.add_polyline('body-collar', (16,top), (24,42), (32,top))
        self.relate('connect', 'body-collar', 'body-top')
        self.relate('connect', 'body-collar', 'body-top-right')
        self.add_line('body-tie', (24,42), (22,44))
        self.relate('connect', 'body-collar', 'body-tie')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
