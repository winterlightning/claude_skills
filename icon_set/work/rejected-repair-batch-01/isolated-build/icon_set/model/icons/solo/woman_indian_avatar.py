"""woman-indian: tunic fastening with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 32, shoulder top 36, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: tunic fastening. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '00932023-8394-5a44-a022-548441776c82'
SOURCE_PATH = 'pictographic-primitives/avatars/woman indian_00932023-8394-5a44-a022-548441776c82.svg'
SOURCE_HEAD_ICON_ID = 'woman-indian'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 32
class WomanIndianAvatar(Solo48):
    icon_id = 'woman-indian-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('woman', 'indian', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(10,18),(38,18),radius_x=14)
        self.add_arc('jaw',(38,18),(10,18),radius_x=14)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_bezier('fringe',(10,18),((18,18),(22,14),(24,12)),((26,14),(30,18),(38,18)))
        self.relate('connect','fringe','head')
        self.add_dot('bindi',(24,23))
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
        self.add_line('body-fastening',(24,top),(24,44))
        self.relate('connect','body-fastening','body-top')
        self.relate('connect','body-fastening','body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
