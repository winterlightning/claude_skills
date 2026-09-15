"""Man Construction: work vest centre fastening, with reference curved shoulders.

Plan: head/headwear and curved body on SOLO48 VRECT_L, ink (6,2)-(42,46).
Circular face and shoulder ink meet with zero visible gap.
Human reference: icon_set/references/human_ref/user.svg; supporting Lucide
original/user-round.svg and atomic-debug/user-round.svg supply cardinal arcs.
Preserve original head identity; omit tiny facial marks and hat trim at 48.
Paired shoulders use shared radii; source hair asymmetry remains intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e34e75b6-7322-4658-bc40-c90c4e98051e'
SOURCE_PATH = 'pictographic-primitives/avatars/man construction_e34e75b6-7322-4658-bc40-c90c4e98051e.svg'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26

class ManConstruction(Solo48):
    icon_id = 'man-construction'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'construction', 'avatars')

    def build(self):
        self.add_arc('helmet-left',(12,16),(24,4),radius_x=12)
        self.add_arc('helmet-right',(24,4),(36,16),radius_x=12)
        self.add_contour('helmet','helmet-left','helmet-right')
        self.add_polyline('brim',(8,16),(12,16),(24,16),(36,16),(40,16))
        self.relate('connect','helmet','brim')
        self.add_line('helmet-ridge',(24,4),(24,16))
        self.relate('connect','helmet-ridge','helmet')
        self.relate('connect','helmet-ridge','brim')
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','face','brim')
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
        self.add_line('body-fastening',(24,top),(24,44))
        self.relate('connect','body-fastening','body-top')
        self.relate('connect','body-fastening','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
