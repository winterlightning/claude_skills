"""Rebalance inside radial envelope, simplifying wheel interiors to solid wheel marks."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = 'b98df773-88b9-4b59-bf8f-31bdee2160b2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon web service marketplaces cart_b98df773-88b9-4b59-bf8f-31bdee2160b2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-web-service-marketplaces-cart'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.CIRCLE.bounds_for(Profile.SOLO48)
    def build(self):
        # CIRCLE radial envelope permits a wide cart bowl and the lower wheel baseline.
        self.add_polyline('cells',(24,4),(29,7),(29,13),(34,16),(34,22),(29,25),(24,22),(19,25),(14,22),(14,16),(19,13),(19,7),closed=True)
        self.add_polyline('junction',(19,13),(24,16),(29,13))
        self.add_line('seam',(24,16),(24,22))
        self.relate('connect','cells','junction')
        self.relate('connect','cells','seam')
        self.relate('connect','junction','seam')
        self.add_arc('bowl',(4,24),(44,24),radius_x=20,radius_y=10,sweep=False)
        self.add_line('left',(5,18),(4,24))
        self.add_line('handle',(44,24),(43,18))
        self.add_contour('basket','left','bowl','handle')
        self.add_dot('wheel-left',(17,42))
        self.add_dot('wheel-right',(31,42))
