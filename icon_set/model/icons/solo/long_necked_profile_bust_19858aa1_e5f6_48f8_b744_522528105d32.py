"""Blank frontal user bust, adapted to the current avatar construction rule.
VRECT_L (8,4)-(40,44) budgets a circular head and broad curved shoulders.
Human reference user.svg owns proportions and open bottom; Lucide user-round
confirms circle/shoulder vocabulary. Source supplies the blank frontal bust.
Replace the long oval neck silhouette with the required circular touching head;
omit the closed baseline. Mirrored shoulders share radius and contact level.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '19858aa1-e5f6-48f8-b744-522528105d32'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/neutral 1_19858aa1-e5f6-48f8-b744-522528105d32.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'long-necked-profile-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ('User Profile Avatar',)
    keywords = ('bust','avatar','person','profile','head','shoulders')
    def build(self):
        cx,cy,r=24,12,8
        self.add_arc('head-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc('face',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour('head','head-top','face',closed=True)
        top=cy+r+HEAD_BODY_CENTERLINE_GAP
        sr=12
        self.add_line('body-left-side',(8,44),(8,top+sr))
        self.add_arc('body-left-shoulder',(8,top+sr),(20,top),radius_x=sr)
        self.add_line('body-top',(20,top),(28,top))
        self.add_arc('body-right-shoulder',(28,top),(40,top+sr),radius_x=sr)
        self.add_line('body-right-side',(40,top+sr),(40,44))
        self.add_contour('body','body-left-side','body-left-shoulder','body-top','body-right-shoulder','body-right-side')
        self.relate('connect','head','body')
