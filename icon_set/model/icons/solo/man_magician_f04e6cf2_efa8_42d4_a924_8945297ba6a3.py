"""Man Magician: broad jacket lapels, with reference curved shoulders.

Plan: head/headwear and curved body on SOLO48 VRECT_L, ink (6,2)-(42,46).
Circular face and shoulder ink meet with zero visible gap.
Human reference: icon_set/references/human_ref/user.svg; supporting Lucide
original/user-round.svg and atomic-debug/user-round.svg supply cardinal arcs.
Preserve original head identity; omit tiny facial marks and hat trim at 48.
Paired shoulders use shared radii; source hair asymmetry remains intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'f04e6cf2-efa8-42d4-a924-8945297ba6a3'
SOURCE_PATH = 'pictographic-primitives/avatars/man magician_f04e6cf2-efa8-42d4-a924-8945297ba6a3.svg'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26

class ManMagician(Solo48):
    icon_id = 'man-magician'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'magician', 'avatars')

    def build(self):
        self.add_polyline('hat',(14,16),(14,4),(34,4),(34,16))
        self.add_polyline('brim',(8,16),(14,16),(34,16),(40,16))
        self.relate('connect','hat','brim')
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','face','brim')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_polyline('body-lapels',(16,top),(24,42),(32,top))
        self.relate('connect','body-lapels','body-top')
        self.relate('connect','body-lapels','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
