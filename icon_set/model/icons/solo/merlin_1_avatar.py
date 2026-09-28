"""merlin-1: robe bands with reference headwear/hair silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 30, shoulders 34, zero painted gap. human_ref/user.svg supplies
curved shoulders; Lucide user-round original and atomic-debug guide arcs.
Fine trim is omitted for clarity at 48; body cue: robe bands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c21f0eb9-2d96-5109-bfbe-e9bed09ca220'
SOURCE_PATH = 'pictographic-primitives/avatars/merlin_c21f0eb9-2d96-5109-bfbe-e9bed09ca220.svg'
SOURCE_HEAD_ICON_ID = 'merlin-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class Merlin1Avatar(Solo48):
    icon_id = 'merlin-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('merlin', '1', 'portrait', 'bust')
    def build(self):
        self.add_polyline('hat',(12,20),(24,4),(36,20))
        self.add_polyline('brim',(8,20),(12,20),(14,20),(34,20),(36,20),(40,20))
        self.relate('connect','hat','brim')
        self.add_arc('face',(34,20),(14,20),radius_x=10)
        self.relate('connect','face','brim')
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
