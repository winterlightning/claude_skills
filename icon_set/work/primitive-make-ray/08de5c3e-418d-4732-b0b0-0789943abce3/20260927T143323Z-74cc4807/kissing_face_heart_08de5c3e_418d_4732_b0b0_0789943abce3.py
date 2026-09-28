"""Revision of the claimed reference after comparing original and rejected drawing."""
"""Closed-eye kissing face with a separate floating heart. Source distinction from beam version retained by omitting the emission line. CIRCLE radial envelope radius22 around24,24."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '08de5c3e-418d-4732-b0b0-0789943abce3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kissing-face-heart/20260927T142529Z-thuan-mac-1/reference/face kiss_08de5c3e-418d-4732-b0b0-0789943abce3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kissing-face-heart'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.CIRCLE.bounds_for(Profile.SOLO48)
    def build(self):
        # Circular face is open behind the floating heart. Radius19 at (24,23) fits CIRCLE radial envelope.
        self.add_arc('head-top',(5,23),(43,23),radius_x=19)
        self.add_arc('head-bottom',(24,42),(5,23),radius_x=19)
        self.relate('connect','head-top','head-bottom')
        for name,x in [('left',18),('right',30)]:
            self.add_arc('eye-'+name,(x-2,18),(x+2,18),radius_x=2,radius_y=1,sweep=False)
        self.add_arc('upper-lip',(18,28),(21,30),radius_x=3,radius_y=2,sweep=True)
        self.add_arc('lower-lip',(21,30),(18,33),radius_x=3,radius_y=3,sweep=True)
        self.add_contour('kiss','upper-lip','lower-lip')
        self.add_arc('heart-left',(35,33),(29,33),radius_x=3,sweep=False)
        self.add_bezier('heart-tip',(29,33),((29,35),(32,38),(35,40)),((38,38),(41,35),(41,33)))
        self.add_arc('heart-right',(41,33),(35,33),radius_x=3,sweep=False)
        self.add_contour('heart','heart-left','heart-tip','heart-right',closed=True)
