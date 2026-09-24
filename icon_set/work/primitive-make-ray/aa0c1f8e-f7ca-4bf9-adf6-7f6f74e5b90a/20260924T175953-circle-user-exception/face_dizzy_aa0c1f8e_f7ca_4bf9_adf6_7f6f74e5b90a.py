"""Complete circular emoji with small internal eye symbols.
User explicitly prefers the circular enclosure and smaller symbols even when the rules fail.
Keep numerical findings; this is a user-authorized visual exception, not an automatic pass.
Plan: circular head at (24,24), radius20; mirrored eyes centered at x16 and32.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='aa0c1f8e-f7ca-4bf9-adf6-7f6f74e5b90a'
SOURCE_PATH='pictographic-primitives/_uncategorized_17/face dizzy_aa0c1f8e-f7ca-4bf9-adf6-7f6f74e5b90a.svg'
AUTHOR='gpt-6'
USER_APPROVAL='Keep circular faces and draw smaller heart, star and spiral eyes even if rules are broken.'
class Drawing(Solo48):
    icon_id='dizzy-face-with-spiral-eyes'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/expressions'
    aliases=()
    keywords=('emoji','face')
    def build(self):
        self.add_arc('head-top',(4,24),(44,24),radius_x=20)
        self.add_arc('head-bottom',(44,24),(4,24),radius_x=20)
        self.add_contour('head','head-top','head-bottom',closed=True)
        for i,(x,s) in enumerate(((16,1),(32,-1))):
            q=lambda dx,y:(x+s*dx,y)
            self.add_bezier(f'spiral-{i}',q(-5,19),(q(-5,12),q(6,12),q(6,19)),(q(6,26),q(-3,26),q(-3,20)),(q(-3,16),q(2,16),q(2,20)))
        self.add_bezier('open-mouth',(20,35),((18,28),(30,28),(28,35)),((27,37),(26,34),(24,34)),((22,34),(21,37),(20,35)))
        self.add_contour('mouth','open-mouth',closed=True)
