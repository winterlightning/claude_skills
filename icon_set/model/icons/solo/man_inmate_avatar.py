"""man-inmate: uniform chest stripe with reference hair/headwear.
Plan: SOLO48 VRECT_L, ink (6,2)-(42,46); circular face x24,
head bottom 30, shoulders 34, zero painted gap. Shared human_ref/user.svg
supplies curved shoulders; Lucide user-round original and atomic-debug guide
cardinal arcs. Fine trim omitted at 48. Body cue: uniform chest stripe.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-05/references/man-inmate.svg'
SOURCE_HEAD_ICON_ID = 'man-inmate'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class ManInmateAvatar(Solo48):
    icon_id = 'man-inmate-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'inmate', 'portrait', 'bust')
    def build(self):
        self.add_arc('hat-top',(12,12),(36,12),radius_x=12,radius_y=8)
        self.add_polyline('hat-band',(12,12),(12,20),(36,20),(36,12))
        self.relate('connect','hat-top','hat-band')
        self.add_line('hat-seam',(24,4),(24,20))
        self.relate('connect','hat-seam','hat-top')
        self.relate('connect','hat-seam','hat-band')
        self.add_arc('face',(34,20),(14,20),radius_x=10)
        self.relate('connect','face','hat-band')
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
        self.add_line('body-band', (8,42), (40,42))
        self.relate('connect', 'body-band', 'body-left')
        self.relate('connect', 'body-band', 'body-right')
        self.add_line('body-fastening', (24,top), (24,42))
        self.relate('connect', 'body-fastening', 'body-top')
        self.relate('connect', 'body-fastening', 'body-top-right')
        self.relate('connect', 'body-fastening', 'body-band')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
