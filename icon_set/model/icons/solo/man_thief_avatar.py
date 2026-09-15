"""man-thief: striped shirt with reference headwear/hair silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 30, shoulders 34, zero painted gap. human_ref/user.svg supplies
curved shoulders; Lucide user-round original and atomic-debug guide arcs.
Fine trim is omitted for clarity at 48; body cue: striped shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c6bef80e-c0fc-405f-b89d-a52e7d929757'
SOURCE_PATH = 'pictographic-primitives/avatars/man thief_c6bef80e-c0fc-405f-b89d-a52e7d929757.svg'
SOURCE_HEAD_ICON_ID = 'man-thief'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class ManThiefAvatar(Solo48):
    icon_id = 'man-thief-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'thief', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(14,12),(34,12),radius_x=10,radius_y=8)
        for side,cx in [('left',14),('right',34)]:
            self.add_arc('lens-top-'+side,(cx,20),(cx,12),radius_x=6,radius_y=4)
            self.add_arc('lens-bottom-'+side,(cx,12),(cx,20),radius_x=6,radius_y=4)
            self.add_contour('lens-'+side,'lens-top-'+side,'lens-bottom-'+side,closed=True)
            self.relate('connect','crown','lens-'+side)
        self.add_line('bridge',(20,16),(28,16))
        self.relate('connect','bridge','lens-left')
        self.relate('connect','bridge','lens-right')
        self.add_arc('face',(34,20),(14,20),radius_x=10)
        self.relate('connect','face','lens-left')
        self.relate('connect','face','lens-right')
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
