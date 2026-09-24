"""Marketplace cart: three shared-wall hexagonal packages, open cart basket, paired circular wheels."""
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
        # Three equal hexagonal cells share actual edges; basket and wheels remain separate.
        self.add_polyline('cells',(24,6),(32,10),(32,18),(40,22),(40,30),(32,34),(24,30),(16,34),(8,30),(8,22),(16,18),(16,10),closed=True)
        self.add_polyline('junction',(16,18),(24,22),(32,18))
        self.add_line('seam',(24,22),(24,30))
        self.relate('connect','cells','junction')
        self.relate('connect','cells','seam')
        self.relate('connect','junction','seam')
        self.add_polyline('basket',(6,16),(6,36),(42,36),(42,6))
        self.add_arc('wheel-left-a',(12,42),(16,42),radius_x=2)
        self.add_arc('wheel-left-b',(16,42),(12,42),radius_x=2)
        self.add_contour('wheel-left','wheel-left-a','wheel-left-b',closed=True)
        self.add_arc('wheel-right-a',(32,42),(36,42),radius_x=2)
        self.add_arc('wheel-right-b',(36,42),(32,42),radius_x=2)
        self.add_contour('wheel-right','wheel-right-a','wheel-right-b',closed=True)
