"""korean-woman-1: wrap blouse and reference headwear/hair silhouette.
SOLO48 VRECT_L ink bounds (6,2)-(42,46). Circular face centered x24;
head bottom 32, shoulders 36, zero visible contact gap. Curved shoulders
follow human_ref/user.svg; Lucide user-round original and atomic-debug inform
cardinal arcs. Fine face/trim details omitted at 48; body cue: wrap blouse.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'ef690c2c-a850-4b25-8f8e-888c762a8355'
SOURCE_PATH = 'pictographic-primitives/avatars/korean woman_ef690c2c-a850-4b25-8f8e-888c762a8355.svg'
SOURCE_HEAD_ICON_ID = 'korean-woman-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 32
class KoreanWoman1Avatar(Solo48):
    icon_id = 'korean-woman-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('korean', 'woman', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('bun-left',(24,12),(24,4),radius_x=4)
        self.add_arc('bun-right',(24,4),(24,12),radius_x=4)
        self.add_contour('bun','bun-left','bun-right',closed=True)
        self.add_arc('crown-left',(14,22),(24,12),radius_x=10)
        self.add_arc('crown-right',(24,12),(34,22),radius_x=10)
        self.add_arc('jaw',(34,22),(14,22),radius_x=10)
        self.add_contour('head','crown-left','crown-right','jaw',closed=True)
        self.relate('connect','bun','head')
        self.add_bezier('fringe',(14,22),((20,24),(24,20),(27,17)),((29,20),(32,22),(34,22)))
        self.relate('connect','head','fringe')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (16,top), (24, top))
        self.add_line('body-top-right', (24, top), (32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
        self.add_line('body-fastening',(24,top),(24,44))
        self.relate('connect','body-fastening','body-top')
        self.relate('connect','body-fastening','body-top-right')
        self.relate('connect','body-fastening','head')
