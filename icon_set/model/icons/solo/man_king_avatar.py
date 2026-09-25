"""man-king: royal robe bands with reference hair/headwear.
Plan: SOLO48 VRECT_L, ink (6,2)-(42,46); circular face x24,
head bottom 26, shoulders 30, zero painted gap. Shared human_ref/user.svg
supplies curved shoulders; Lucide user-round original and atomic-debug guide
cardinal arcs. Fine trim omitted at 48. Body cue: royal robe bands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'a5228c4d-8b90-4805-9afd-aa85b127ecfa'
SOURCE_PATH = 'pictographic-primitives/avatars/man king_a5228c4d-8b90-4805-9afd-aa85b127ecfa.svg'
SOURCE_HEAD_ICON_ID = 'man-king'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class ManKingAvatar(Solo48):
    icon_id = 'man-king-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'king', 'portrait', 'bust')
    def build(self):
        self.add_polyline('crown',(14,16),(10,4),(18,8),(24,4),(30,8),(38,4),(34,16),(14,16))
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','face','crown')
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
        self.add_line('body-apron-left', (18,top), (18,44))
        self.add_line('body-apron-right', (30,top), (30,44))
        self.relate('connect', 'body-apron-left', 'body-top')
        self.relate('connect', 'body-apron-right', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
