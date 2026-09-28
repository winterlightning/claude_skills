"""man-japan: swept hair and rounded tunic neck.
Distinct-avatar plan: preserve reference identity; use swept hair and rounded tunic neck.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 24; shoulder top 28; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '3c937449-3b63-4517-a7b7-4088598ee58d'
SOURCE_PATH = 'pictographic-primitives/avatars/man japan_3c937449-3b63-4517-a7b7-4088598ee58d.svg'
SOURCE_HEAD_ICON_ID = 'man-japan'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class ManJapanAvatar(Solo48):
    icon_id = 'man-japan-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'japan', 'portrait', 'bust')
    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('crown', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
        self.add_arc('jaw', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('head', 'crown', 'jaw', closed=True)
        self.add_bezier('fringe', (14, 14), ((16, 14), (19, 12), (21, 9)), ((24, 12), (28, 16), (34, 14)))
        self.relate('connect', 'head', 'fringe')

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

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
