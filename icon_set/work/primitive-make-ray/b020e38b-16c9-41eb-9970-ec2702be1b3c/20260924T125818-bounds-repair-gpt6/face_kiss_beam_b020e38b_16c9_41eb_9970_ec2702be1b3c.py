"""Kissing face with closed eyes and floating heart. Face and heart fit a radius22 visible-ink envelope about (24,24); open right-lower face behind heart."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b020e38b-16c9-41eb-9970-ec2702be1b3c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face kiss beam_b020e38b-16c9-41eb-9970-ec2702be1b3c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'face-kiss-beam'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
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
        self.add_polyline('kiss',(19,28),(21,30),(19,32))
        self.add_arc('heart-left',(35,33),(29,33),radius_x=3,sweep=False)
        self.add_bezier('heart-tip',(29,33),((29,35),(32,38),(35,40)),((38,38),(41,35),(41,33)))
        self.add_arc('heart-right',(41,33),(35,33),radius_x=3,sweep=False)
        self.add_contour('heart','heart-left','heart-tip','heart-right',closed=True)
        self.add_line('kiss-beam',(21,30),(29,33))
        self.relate('connect','kiss-beam','kiss')
        self.relate('connect','kiss-beam','heart')
