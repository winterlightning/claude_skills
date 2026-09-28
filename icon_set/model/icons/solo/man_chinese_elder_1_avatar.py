"""man-chinese-elder-1: robe lapel with reference hair/headwear.
Plan: SOLO48 VRECT_L, ink (6,2)-(42,46); circular face x24,
head bottom 26, shoulders 30, zero painted gap. Shared human_ref/user.svg
supplies curved shoulders; Lucide user-round original and atomic-debug guide
cardinal arcs. Fine trim and the tiny internal beard detail omitted at 48. Body cue: robe lapel.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'bc3bae42-c42e-4c1b-af47-3e748a678e13'
SOURCE_PATH = 'pictographic-primitives/avatars/man chinese elder_bc3bae42-c42e-4c1b-af47-3e748a678e13.svg'
SOURCE_HEAD_ICON_ID = 'man-chinese-elder-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class ManChineseElder1Avatar(Solo48):
    icon_id = 'man-chinese-elder-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'chinese', 'elder', '1', 'portrait', 'bust')
    def build(self):
        self.add_polyline('hat',(8,16),(24,4),(40,16),(8,16))
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','face','hat')
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

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
