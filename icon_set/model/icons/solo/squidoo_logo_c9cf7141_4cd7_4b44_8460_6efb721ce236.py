"""Round squid head with a small eye and two flowing tentacle tips. Preserve the sweeping asymmetry and reduce the smallest third curl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9cf7141-4cd7-4b44-8460-6efb721ce236'
SOURCE_PATH = 'pictographic-primitives/logos/squidoo logo_c9cf7141-4cd7-4b44-8460-6efb721ce236.svg'
AUTHOR = 'gpt-6'

class SquidooLogo(Solo48):
    icon_id = 'squidoo-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('squidoo', 'squid', 'web', 'community', 'logo', 'brand', 'lenses')

    def build(self):
        # Plan: Round squid head with a small eye and two flowing tentacle tips. Preserve the sweeping asymmetry and reduce the smallest third curl.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_bezier('outline',(24,4),((24,14),(38,8),(32,22)),((32,25),(40,24),(40,32)),((40,39),(35,44),(28,44)),((21,44),(18,39),(18,34)),((18,28),(8,38),(8,24)))
        self.add_bezier('tentacle',(8,12),((20,8),(12,23),(23,23)))
        self.add_dot('eye',(29,34))

