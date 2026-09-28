"""Revision from the claimed current drawing: preserve the subject and improve its distinguishing feature.
The original source is unavailable; the staged reference is the rejected drawing.
Human proportions follow icon_set/references/human_ref/user.svg.
"""
"""user-injured: sling across torso with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 30, shoulder top 34, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: sling across torso. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = "caae7e27-b4ac-57d4-af18-796cf00252f6"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__user-injured-avatar/20260926T181756Z-thuan-mac-1/reference/user-injured-avatar_caae7e27-b4ac-57d4-af18-796cf00252f6.svg"
SOURCE_HEAD_ICON_ID = 'user-injured'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class UserInjuredAvatar(Solo48):
    icon_id = 'user-injured-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'injured', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(11,17),(37,17),radius_x=13)
        self.add_arc('jaw',(37,17),(11,17),radius_x=13)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_line('bandage',(12,12),(36,22))
        self.relate('connect','bandage','head')
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
        self.add_polyline('body-wrap', (12,top), (24,44))
        self.relate('connect', 'body-wrap', 'body-top')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
