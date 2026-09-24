"""Rebalanced three shared-edge packages, retaining hexagonal holes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b98df773-88b9-4b59-bf8f-31bdee2160b2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon web service marketplaces cart_b98df773-88b9-4b59-bf8f-31bdee2160b2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-web-service-marketplaces-cart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Shared-wall honeycomb, coherent basket, paired wheels.
        self.add_polyline('cells',(24,6),(30,9),(30,15),(36,18),(36,24),(30,27),(24,24),(18,27),(12,24),(12,18),(18,15),(18,9),closed=True)
        self.add_polyline('junction',(18,15),(24,18),(30,15))
        self.add_line('seam',(24,18),(24,24))
        self.relate('connect','cells','junction')
        self.relate('connect','cells','seam')
        self.relate('connect','junction','seam')
        self.add_polyline('basket',(6,16),(6,32),(42,32),(42,6))
        self.add_arc('wheel-left-a',(12,40),(16,40),radius_x=2)
        self.add_arc('wheel-left-b',(16,40),(12,40),radius_x=2)
        self.add_contour('wheel-left','wheel-left-a','wheel-left-b',closed=True)
        self.add_arc('wheel-right-a',(32,40),(36,40),radius_x=2)
        self.add_arc('wheel-right-b',(36,40),(32,40),radius_x=2)
        self.add_contour('wheel-right','wheel-right-a','wheel-right-b',closed=True)
