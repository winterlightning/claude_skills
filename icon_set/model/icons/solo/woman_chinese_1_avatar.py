"""woman-chinese-1: wrapped blouse with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 28, shoulder top 32, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: wrapped blouse. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c74508b7-5e91-446d-88e9-08c52d64ab75'
SOURCE_PATH = 'pictographic-primitives/avatars/woman chinese_c74508b7-5e91-446d-88e9-08c52d64ab75.svg'
SOURCE_HEAD_ICON_ID = 'woman-chinese-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class WomanChinese1Avatar(Solo48):
    icon_id = 'woman-chinese-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'chinese', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('hair-left',(14,18),(16,8),radius_x=2,radius_y=10)
        self.add_arc('hair-top',(16,8),(32,8),radius_x=8,radius_y=4)
        self.add_arc('hair-right',(32,8),(34,18),radius_x=2,radius_y=10)
        self.add_arc('face',(34,18),(14,18),radius_x=10)
        self.add_contour('head','hair-left','hair-top','hair-right','face',closed=True)
        for side,cx in [('left',12),('right',36)]:
            self.add_arc('bun-top-'+side,(cx-4,8),(cx+4,8),radius_x=4)
            self.add_arc('bun-bottom-'+side,(cx+4,8),(cx-4,8),radius_x=4)
            self.add_contour('bun-'+side,'bun-top-'+side,'bun-bottom-'+side,closed=True)
            self.relate('connect','bun-'+side,'head')
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
