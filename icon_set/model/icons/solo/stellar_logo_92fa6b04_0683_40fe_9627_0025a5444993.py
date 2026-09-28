"""Two parallel diagonal orbit strokes and opposite circle arcs. Use shared diagonal offsets and leave the circle open where the orbit crosses."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92fa6b04-0683-40fe-9627-0025a5444993'
SOURCE_PATH = 'pictographic-primitives/logos/stellar logo_92fa6b04-0683-40fe-9627-0025a5444993.svg'
AUTHOR = 'gpt-6'

class StellarLogo(Solo48):
    icon_id = 'stellar-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('stellar', 'xlm', 'cryptocurrency', 'blockchain', 'logo', 'brand', 'planet')

    def build(self):
        # Plan: Two parallel diagonal orbit strokes and opposite circle arcs. Use shared diagonal offsets and leave the circle open where the orbit crosses.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_line('upper-orbit',(4,30),(44,8))
        self.add_line('lower-orbit',(4,40),(44,18))
        self.add_bezier('upper-ring',(8,16),((8,8),(18,8),(26,8)))
        self.add_bezier('lower-ring',(40,32),((40,40),(30,40),(22,40)))

