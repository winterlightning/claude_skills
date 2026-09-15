"""Lowercase me wordmark. Repeated m arches share one radius and baseline; the e counter has a real shared bar junction. Preserve geometric round lettering with a taller fit."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e586f7da-06cf-42e6-ba54-28bde6b69e14'
SOURCE_PATH = 'pictographic-primitives/logos/social media about me logo_e586f7da-06cf-42e6-ba54-28bde6b69e14.svg'
AUTHOR = 'gpt-6'

class AboutMeLogo(Solo48):
    icon_id = 'about-me-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('about-me', 'profile', 'personal', 'wordmark', 'logo', 'brand', 'me')

    def build(self):
        # Plan: Lowercase me wordmark. Repeated m arches share one radius and baseline; the e counter has a real shared bar junction. Preserve geometric round lettering with a taller fit.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        for j,x in enumerate((4,12)):
            self.add_arc('m-arch-'+str(j),(x,12),(x+8,12),radius_x=4)
        for j,x in enumerate((4,12,20)):
            self.add_line('m-stem-'+str(j),(x,12),(x,40))
        for a,b in [('m-arch-0','m-stem-0'),('m-arch-0','m-stem-1'),('m-arch-1','m-stem-1'),('m-arch-1','m-stem-2'),('m-arch-0','m-arch-1')]:self.relate('connect',a,b)
        self.add_bezier('e-upper',(29,24),((29,14),(31,8),(36,8)),((41,8),(44,14),(44,24)))
        self.add_line('e-bar',(44,24),(29,24))
        self.add_contour('e-counter','e-upper','e-bar',closed=True)
        self.add_bezier('e-lower',(29,24),((29,34),(31,40),(36,40)),((40,40),(42,37),(44,34)))
        self.relate('connect','e-counter','e-lower')

