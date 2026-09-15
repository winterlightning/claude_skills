"""Repeated p bowls share width, baseline and descender length, around a tall h. Reduce slant to fit three separated glyphs; retain php wordmark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77122871-2f9f-498a-98fa-c84482b1670a'
SOURCE_PATH = 'pictographic-primitives/logos/php logo_77122871-2f9f-498a-98fa-c84482b1670a.svg'
AUTHOR = 'gpt-6'

class PhpLogo(Solo48):
    icon_id = 'php-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('php', 'programming', 'language', 'wordmark', 'logo', 'brand', 'web')

    def build(self):
        # Plan: Repeated p bowls share width, baseline and descender length, around a tall h. Reduce slant to fit three separated glyphs; retain php wordmark.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        for i,x in enumerate((4,37)):
            self.add_line('p-stem-'+str(i),(x,16),(x,40))
            self.add_arc('p-bowl-'+str(i),(x,16),(x,28),radius_x=7,radius_y=6)
            self.relate('connect','p-stem-'+str(i),'p-bowl-'+str(i))
        self.add_polyline('h-stem',(20,8),(20,20),(20,32))
        self.add_arc('h-arch',(20,20),(28,20),radius_x=4)
        self.add_line('h-leg',(28,20),(28,32))
        self.relate('connect','h-arch','h-leg')
        self.relate('connect','h-stem','h-arch')

