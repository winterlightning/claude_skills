"""Complete circular emoji with small internal eye symbols.
User explicitly prefers the circular enclosure and smaller symbols even when the rules fail.
Keep numerical findings; this is a user-authorized visual exception, not an automatic pass.
Plan: circular head at (24,24), radius20; mirrored eyes centered at x16 and32.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='236451ca-3512-494c-8c17-87481ad251f8'
SOURCE_PATH='pictographic-primitives/_uncategorized_17/face awesome_236451ca-3512-494c-8c17-87481ad251f8.svg'
AUTHOR='gpt-6'
USER_APPROVAL='Keep circular faces and draw smaller heart, star and spiral eyes even if rules are broken.'
class Drawing(Solo48):
    icon_id='smiling-star-eyed-face'
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
        for i,x in enumerate((16,32)):
            self.add_polyline(f'star-{i}',(x,13),(x+2,17),(x+5,17),(x+3,20),(x+3,23),(x,21),(x-3,23),(x-3,20),(x-5,17),(x-2,17),closed=True)
        self.add_line('mouth-top',(16,31),(32,31))
        self.add_arc('mouth-bottom',(32,31),(16,31),radius_x=8,radius_y=6)
        self.add_contour('open-grin','mouth-top','mouth-bottom',closed=True)
