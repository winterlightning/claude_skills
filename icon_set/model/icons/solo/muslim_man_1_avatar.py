"""muslim-man-1: diagonal robe fold with reference headwear/hair silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 24, shoulders 28, zero painted gap. human_ref/user.svg supplies
curved shoulders; Lucide user-round original and atomic-debug guide arcs.
Fine trim is omitted for clarity at 48; body cue: diagonal robe fold.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'e730d035-9a68-5080-b4a5-21d53943262b'
SOURCE_PATH = 'pictographic-primitives/avatars/muslim man_e730d035-9a68-5080-b4a5-21d53943262b.svg'
SOURCE_HEAD_ICON_ID = 'muslim-man-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class MuslimMan1Avatar(Solo48):
    icon_id = 'muslim-man-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('muslim', 'man', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('cap',(14,14),(34,14),radius_x=10)
        self.add_arc('face',(34,14),(14,14),radius_x=10)
        self.add_contour('head','cap','face',closed=True)
        self.add_polyline('brim',(8,14),(14,14),(34,14),(40,14))
        self.relate('connect','head','brim')
        self.add_line('drape-left',(14,14),(8,20))
        self.add_line('drape-right',(34,14),(40,20))
        self.relate('connect','head','drape-left')
        self.relate('connect','head','drape-right')
        self.relate('connect','brim','drape-left')
        self.relate('connect','brim','drape-right')
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
