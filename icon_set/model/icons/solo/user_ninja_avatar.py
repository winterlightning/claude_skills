"""user-ninja: wrapped tunic with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 28, shoulder top 32, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: wrapped tunic. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-11/references/user-ninja.svg'
SOURCE_HEAD_ICON_ID = 'user-ninja'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class UserNinjaAvatar(Solo48):
    icon_id = 'user-ninja-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'ninja', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(14,18),(34,18),radius_x=10)
        self.add_arc('face',(34,18),(14,18),radius_x=10)
        self.add_contour('head','crown','face',closed=True)
        self.add_line('mask',(14,18),(34,18))
        self.relate('connect','mask','head')
        self.add_polyline('tie',(8,4),(14,18),(8,18))
        self.relate('connect','tie','head')
        self.relate('connect','tie','mask')
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
