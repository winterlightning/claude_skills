"""Winking kissing face: open arched eye and shallower wink, puckered lips, floating heart. Circular face and radial envelope retained; no beam."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '465fa6c6-5f8b-4335-a186-c938fe764751'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face kiss wink heart_465fa6c6-5f8b-4335-a186-c938fe764751.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kissing-face-wink-heart'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.CIRCLE.bounds_for(Profile.SOLO48)
    def build(self):
        # Circular face is open behind the floating heart. Radius19 at (24,23) fits CIRCLE radial envelope.
        self.add_arc('head-top',(5,23),(43,23),radius_x=19)
        self.add_arc('head-bottom',(24,42),(5,23),radius_x=19)
        self.relate('connect','head-top','head-bottom')
        self.add_arc('eye-left',(16,19),(20,19),radius_x=2,sweep=True)
        self.add_arc('wink-right',(28,18),(32,18),radius_x=2,radius_y=1,sweep=True)
        self.add_polyline('kiss',(19,28),(21,30),(19,32))
        self.add_arc('heart-left',(35,33),(29,33),radius_x=3,sweep=False)
        self.add_bezier('heart-tip',(29,33),((29,35),(32,38),(35,40)),((38,38),(41,35),(41,33)))
        self.add_arc('heart-right',(41,33),(35,33),radius_x=3,sweep=False)
        self.add_contour('heart','heart-left','heart-tip','heart-right',closed=True)
