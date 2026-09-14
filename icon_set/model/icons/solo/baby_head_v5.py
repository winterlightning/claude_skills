# Review candidate; original preserved.
"""A blank baby portrait with curled hair, ear bumps and broad shoulders; Lucide baby informs the continuous face contour."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '454b702c-a035-5fa0-a3ec-ac065587fca8'
SOURCE_PATH = 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'
AUTHOR = 'gpt-6'

class BabyHeadVariant5(Solo48):
    icon_id = 'baby-head-v5'
    variant_of = 'baby-head-v2'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('baby', 'head', 'infant', 'nursery')

    def build(self) -> None:
        """Opening repair: Rebuilt the intended round head and inward curl so the curl no longer crosses the forehead."""
        self.add_arc('head-left', (24, 6), (24, 42), radius_x=18, sweep=False)
        self.add_arc('head-right', (24, 42), (24, 6), radius_x=18, sweep=False)
        self.add_contour('head', 'head-left', 'head-right', closed=True)
        self.add_arc('curl-down', (24, 6), (30, 12), radius_x=6)
        self.add_arc('curl-in', (30, 12), (24, 18), radius_x=6)
        self.add_contour('curl', 'curl-down', 'curl-in')
        self.relate('connect', 'head', 'curl')
