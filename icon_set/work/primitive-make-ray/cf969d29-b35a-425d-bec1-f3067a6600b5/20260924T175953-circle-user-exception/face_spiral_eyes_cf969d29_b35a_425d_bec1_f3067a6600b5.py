"""Complete circular emoji with small internal eye symbols.
User explicitly prefers the circular enclosure and smaller symbols even when the rules fail.
Keep numerical findings; this is a user-authorized visual exception, not an automatic pass.
Plan: circular head at (24,24), radius20; mirrored eyes centered at x16 and32.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cf969d29-b35a-425d-bec1-f3067a6600b5'
SOURCE_PATH='pictographic-primitives/_uncategorized_18/face spiral eyes_cf969d29-b35a-425d-bec1-f3067a6600b5.svg'
AUTHOR='gpt-6'
USER_APPROVAL='Keep circular faces and draw smaller heart, star and spiral eyes even if rules are broken.'
class Drawing(Solo48):
    icon_id='dizzy-hypnotized-face'
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
        self.add_line('mouth',(19,33),(29,33))
