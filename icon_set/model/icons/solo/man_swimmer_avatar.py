"""man-swimmer: rounded swimsuit neckline with reference hair/headwear.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 30, shoulders 34, zero painted gap. Curved shoulders follow
human_ref/user.svg; Lucide user-round original and atomic-debug guide arcs.
Fine trim omitted at 48; clothing cue: rounded swimsuit neckline. Source asymmetry is retained
in headwear while the face stays centered.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'f875f41c-ce24-4c42-b39e-be3923b31ffa'
SOURCE_PATH = 'pictographic-primitives/avatars/man swimmer_f875f41c-ce24-4c42-b39e-be3923b31ffa.svg'
SOURCE_HEAD_ICON_ID = 'man-swimmer'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class ManSwimmerAvatar(Solo48):
    icon_id = 'man-swimmer-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'swimmer', 'portrait', 'bust')
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
        self.add_line('body-top',(18,top),(24,top))
        self.add_line('body-top-right',(24,top),(30,top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_arc('body-neckline',(18,top),(30,top),radius_x=6,radius_y=6,sweep=False)
        self.relate('connect','body-neckline','body-top')
        self.relate('connect','body-neckline','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
