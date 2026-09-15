"""Square frame with an attached squared P; all P junctions reuse shared nodes. Retain the asymmetric descending stem."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '837ac307-98d2-41d2-bc8e-c27262c09553'
SOURCE_PATH = 'pictographic-primitives/logos/pagekit logo_837ac307-98d2-41d2-bc8e-c27262c09553.svg'
AUTHOR = 'gpt-6'

class PagekitLogo(Solo48):
    icon_id = 'pagekit-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('pagekit', 'cms', 'letter-p', 'logo', 'brand', 'web', 'square')

    def build(self):
        # Plan: Square frame with an attached squared P; all P junctions reuse shared nodes. Retain the asymmetric descending stem.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('frame',(16,42),(6,42),(6,6),(42,6),(42,42),(16,42))
        self.add_polyline('bowl',(16,30),(16,16),(32,16),(32,30),(16,30))
        self.add_line('stem',(16,30),(16,42))
        self.relate('connect','stem','bowl')
        self.relate('connect','stem','frame')

