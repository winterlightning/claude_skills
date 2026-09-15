"""Five separated starburst rays with a dominant upper-left arm. Reduce triangular petal outlines to strokes while retaining their count, asymmetric lengths and open center."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '414ac9a8-a23e-46a8-9cc7-1d58c982d119'
SOURCE_PATH = 'pictographic-primitives/logos/yelp logo_414ac9a8-a23e-46a8-9cc7-1d58c982d119.svg'
AUTHOR = 'gpt-6'

class YelpLogo(Solo48):
    icon_id = 'yelp-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('yelp', 'reviews', 'restaurants', 'burst', 'logo', 'brand', 'local')

    def build(self):
        # Plan: Five separated starburst rays with a dominant upper-left arm. Reduce triangular petal outlines to strokes while retaining their count, asymmetric lengths and open center.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        for j,(a,b) in enumerate([((20,20),(12,6)),((30,18),(40,12)),((32,28),(42,34)),((24,34),(22,42)),((14,30),(6,26))]):self.add_line('petal-'+str(j),a,b)

