"""One smooth looping P with a leaning pin stem. Rebuild the outer loop with coherent cubics and reduce the curled inner hook to a straight pin; preserve deliberate asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7bbd363-1987-4923-88fe-5de98036163a'
SOURCE_PATH = 'pictographic-primitives/logos/pinterest logo_f7bbd363-1987-4923-88fe-5de98036163a.svg'
AUTHOR = 'gpt-6'

class PinterestLogo(Solo48):
    icon_id = 'pinterest-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('pinterest', 'pin', 'letter-p', 'logo', 'brand', 'social', 'inspiration')

    def build(self):
        # Plan: One smooth looping P with a leaning pin stem. Rebuild the outer loop with coherent cubics and reduce the curled inner hook to a straight pin; preserve deliberate asymmetry.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_bezier('loop',(8,29),((8,27),(8,22),(8,20)),((8,10),(14,4),(24,4)),((34,4),(40,10),(40,20)),((40,28),(36,33),(30,33)),((26,33),(24,31),(24,28)))
        self.add_polyline('pin',(28,12),(24,28),(20,44))
        self.relate('connect','loop','pin')

