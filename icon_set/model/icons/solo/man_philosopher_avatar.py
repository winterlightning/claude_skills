"""man-philosopher: scholarly coat lapels.
Distinct-avatar plan: preserve reference identity; use scholarly coat lapels.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 32; shoulder top 36; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-06/references/man-philosopher.svg'
SOURCE_HEAD_ICON_ID = 'man-philosopher'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 32
class ManPhilosopherAvatar(Solo48):
    icon_id = 'man-philosopher-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'philosopher', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(14,10),(34,10),radius_x=10,radius_y=6)
        for side,cx in [('left',14),('right',34)]:
            self.add_arc('lens-top-'+side,(cx,22),(cx,10),radius_x=6)
            self.add_arc('lens-bottom-'+side,(cx,10),(cx,22),radius_x=6)
            self.add_contour('lens-'+side,'lens-top-'+side,'lens-bottom-'+side,closed=True)
            self.relate('connect','crown','lens-'+side)
        self.add_line('bridge',(20,16),(28,16))
        self.relate('connect','bridge','lens-left')
        self.relate('connect','bridge','lens-right')
        self.add_arc('face',(34,22),(14,22),radius_x=10)
        self.relate('connect','face','lens-left')
        self.relate('connect','face','lens-right')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(12,top),radius_x=4,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (12, top), (24, top))
        self.add_line('body-top-right', (24, top), (36, top))
        self.add_arc('body-right-shoulder',(36,top),(40,42),radius_x=4,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_polyline('body-tie', (12, top), (24,44), (36, top))
        self.relate('connect', 'body-tie', 'body-top')
        self.relate('connect', 'body-tie', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
