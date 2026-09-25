"""Rounded square frame holding a smooth central S. Keep the square brand enclosure and reduce outlined letter weight to one coherent stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3993bad-5890-425c-8beb-c02307af043a'
SOURCE_PATH = 'pictographic-primitives/logos/stripe logo_b3993bad-5890-425c-8beb-c02307af043a.svg'
AUTHOR = 'gpt-6'

class StripeLogo(Solo48):
    icon_id = 'stripe-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('stripe', 'payments', 'letter-s', 'logo', 'brand', 'finance', 'checkout')

    def build(self):
        # Plan: Rounded square frame holding a smooth central S. Keep the square brand enclosure and reduce outlined letter weight to one coherent stroke.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        for j,(a,b,c) in enumerate([((10,6),(38,6),(42,10)),((42,10),(42,38),(38,42)),((38,42),(10,42),(6,38)),((6,38),(6,10),(10,6))]):
            self.add_line('side-'+str(j),a,b);self.add_arc('corner-'+str(j),b,c,radius_x=4)
        self.add_contour('frame',*[x for j in range(4) for x in ('side-'+str(j),'corner-'+str(j))],closed=True)
        self.add_bezier('s',(30,18),((30,13),(18,13),(18,20)),((18,24),(30,24),(30,28)),((30,35),(18,35),(18,30)))

