"""Masked wrestler with singlet straps and curved shoulders.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46). Circular face centered x24,
radius15 at y19; head bottom34, shoulders38, zero painted gap.
The supplied wrestler reference informs the pointed mask; simplify the mouth
opening to preserve clear negative space at48. Human user.svg supplies curved
shoulders; Lucide user-round original and atomic-debug guide circular arcs.
Mirror mask lobes around x24 and retain broad singlet straps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'a8b18c9c-3d81-5936-bc42-db44661794e6'
SOURCE_PATH = 'pictographic-primitives/avatars/wrestler_a8b18c9c-3d81-5936-bc42-db44661794e6.svg'
SOURCE_HEAD_ICON_ID = 'wrestler-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 34
class Wrestler1Avatar(Solo48):
    icon_id = 'wrestler-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ('masked-wrestler-avatar',)
    keywords = ('wrestler','luchador','mask','singlet','sport','portrait')
    def build(self):
        self.add_arc('crown',(12,10),(36,10),radius_x=15)
        self.add_arc('right',(36,10),(39,19),radius_x=15)
        self.add_arc('jaw',(39,19),(9,19),radius_x=15)
        self.add_arc('left',(9,19),(12,10),radius_x=15)
        self.add_contour('head','crown','right','jaw','left',closed=True)
        self.add_line('mask-top-left',(12,10),(24,16))
        self.add_line('mask-top-right',(24,16),(36,10))
        self.add_bezier('mask-bottom',(36,10),((30,22),(28,22),(24,20)),((20,22),(18,22),(12,10)))
        self.add_contour('mask','mask-top-left','mask-top-right','mask-bottom',closed=True)
        self.relate('connect','mask','head')
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
        self.add_line('body-apron-left', (12,top), (18,44))
        self.add_line('body-apron-right', (36,top), (30,44))
        self.relate('connect', 'body-apron-left', 'body-top')
        self.relate('connect', 'body-apron-right', 'body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
