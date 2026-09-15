"""Circular badge with an open lowercase e counter. Remove the redundant concentric inner ring to preserve the letter and its openings."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d2e1164-c681-4ad7-9b46-c338df0dec27'
SOURCE_PATH = 'pictographic-primitives/logos/trusted shops logo_2d2e1164-c681-4ad7-9b46-c338df0dec27.svg'
AUTHOR = 'gpt-6'

class TrustedShopsLogo(Solo48):
    icon_id = 'trusted-shops-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('trusted-shops', 'trustmark', 'e-commerce', 'letter-e', 'logo', 'brand', 'shopping')

    def build(self):
        # Plan: Circular badge with an open lowercase e counter. Remove the redundant concentric inner ring to preserve the letter and its openings.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        circle('badge',24,24,20)
        self.add_arc('e-upper',(14,24),(34,24),radius_x=10)
        self.add_line('e-bar',(34,24),(14,24));self.add_contour('e-counter','e-upper','e-bar',closed=True)
        self.add_bezier('e-lower',(14,24),((14,34),(25,37),(32,31)));self.relate('connect','e-counter','e-lower')

