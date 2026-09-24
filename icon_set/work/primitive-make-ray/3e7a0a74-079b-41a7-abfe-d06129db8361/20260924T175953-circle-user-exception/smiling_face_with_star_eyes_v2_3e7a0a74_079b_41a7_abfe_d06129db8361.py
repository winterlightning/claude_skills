"""Complete circular emoji with small internal eye symbols.
User explicitly prefers the circular enclosure and smaller symbols even when the rules fail.
Keep numerical findings; this is a user-authorized visual exception, not an automatic pass.
Plan: circular head at (24,24), radius20; mirrored eyes centered at x16 and32.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3e7a0a74-079b-41a7-abfe-d06129db8361'
SOURCE_PATH='pictographic-primitives/_uncategorized_17/face grin stars_3e7a0a74-079b-41a7-abfe-d06129db8361.svg'
AUTHOR='gpt-6'
USER_APPROVAL='Keep circular faces and draw smaller heart, star and spiral eyes even if rules are broken.'
class Drawing(Solo48):
    icon_id='smiling-face-with-star-eyes'
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
        self.add_bezier('smile',(16,31),((20,37),(28,37),(32,31)))
