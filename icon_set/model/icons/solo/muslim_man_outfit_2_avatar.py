"""muslim-man-outfit-2: long garment front with reference headwear/hair silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 24, shoulders 28, zero painted gap. human_ref/user.svg supplies
curved shoulders; Lucide user-round original and atomic-debug guide arcs.
Fine trim is omitted for clarity at 48; body cue: long garment front.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'ebfdfda3-cd66-462a-9339-bae242892b0f'
SOURCE_PATH = 'pictographic-primitives/avatars/muslim man outfit_ebfdfda3-cd66-462a-9339-bae242892b0f.svg'
SOURCE_HEAD_ICON_ID = 'muslim-man-outfit-2'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class MuslimManOutfit2Avatar(Solo48):
    icon_id = 'muslim-man-outfit-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('muslim', 'man', 'outfit', '2', 'portrait', 'bust')
    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('wrap-left', (14, cy), (cx, 4), radius_x=radius)
        self.add_arc('wrap-right', (cx, 4), (34, cy), radius_x=radius)
        self.add_arc('jaw', (34, cy), (14, cy), radius_x=radius)
        self.add_contour('head', 'wrap-left', 'wrap-right', 'jaw', closed=True)
        self.add_bezier('twist', (cx, 4), ((34, 9), (26, 14), (14, 14)))
        self.relate('connect', 'head', 'twist')

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: soft sleep shirt with a low curved neckline.
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

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
