"""Complete WOO lettering reflowed with W above two matching O counters. Omit the speech-bubble enclosure so the letters retain their open interiors."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa4e485d-4871-499a-a933-05cab3ad6561'
SOURCE_PATH = 'pictographic-primitives/logos/woocommerce logo_fa4e485d-4871-499a-a933-05cab3ad6561.svg'
AUTHOR = 'gpt-6'

class WoocommerceLogo(Solo48):
    icon_id = 'woocommerce-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('woocommerce', 'wordpress', 'e-commerce', 'speech-bubble', 'logo', 'brand', 'shop')

    def build(self):
        # Plan: Complete WOO lettering reflowed with W above two matching O counters. Omit the speech-bubble enclosure so the letters retain their open interiors.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('w',(6,6),(15,18),(24,6),(33,18),(42,6))
        for j,x in enumerate((13,35)):
            self.add_arc('o-top-'+str(j),(x-6,36),(x+6,36),radius_x=6,radius_y=6)
            self.add_arc('o-bottom-'+str(j),(x+6,36),(x-6,36),radius_x=6,radius_y=6)
            self.add_contour('o-'+str(j),'o-top-'+str(j),'o-bottom-'+str(j),closed=True)

