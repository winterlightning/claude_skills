"""man-snake-charmer-1: wrapped robe with reference hair/headwear.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 28, shoulders 32, zero painted gap. Curved shoulders follow
human_ref/user.svg; Lucide user-round original and atomic-debug guide arcs.
Fine trim omitted at 48; clothing cue: wrapped robe. Source asymmetry is retained
in headwear while the face stays centered.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'a45128b3-9b9f-5483-84f4-3984d1c82ec3'
SOURCE_PATH = 'pictographic-primitives/avatars/man snake charmer_a45128b3-9b9f-5483-84f4-3984d1c82ec3.svg'
SOURCE_HEAD_ICON_ID = 'man-snake-charmer-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class ManSnakeCharmer1Avatar(Solo48):
    icon_id = 'man-snake-charmer-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'snake', 'charmer', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown-left',(14,18),(24,8),radius_x=10)
        self.add_arc('crown-right',(24,8),(34,18),radius_x=10)
        self.add_arc('jaw',(34,18),(14,18),radius_x=10)
        self.add_contour('head','crown-left','crown-right','jaw',closed=True)
        self.add_bezier('turban-fold',(14,18),((20,18),(26,14),(30,10)))
        self.relate('connect','head','turban-fold')
        self.add_arc('plume',(24,8),(28,4),radius_x=4)
        self.relate('connect','head','plume')
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
        self.add_polyline('body-wrap', (18,top), (30,44))
        self.relate('connect', 'body-wrap', 'body-top')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
