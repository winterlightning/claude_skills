# Variant of baby-head; parent file remains unchanged.
"""A blank baby portrait with curled hair, ear bumps and broad shoulders; Lucide baby informs the continuous face contour."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '454b702c-a035-5fa0-a3ec-ac065587fca8'
SOURCE_PATH = 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'
AUTHOR = 'gpt-6'

class BabyHeadVariant2(Solo48):
    icon_id = 'baby-head-v2'
    variant_of = 'baby-head'
    variant_label = 'Simplify'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('baby', 'head', 'infant', 'nursery')

    def build(self) -> None:
        # SQUARE extremes (6,6)-(42,42): plain circular head and a single curl.
        self.add_arc('head-left', (24,6), (24,42), radius_x=22, sweep=False)
        self.add_arc('head-right', (24,42), (24,6), radius_x=22, sweep=False)
        self.add_contour('head', 'head-left', 'head-right', closed=True)
        self.add_arc('curl-down', (24,6), (32,10), radius_x=8)
        self.add_arc('curl-in', (32,10), (26,16), radius_x=6)
        self.add_contour('curl', 'curl-down', 'curl-in')
        self.relate('connect', 'head', 'curl')
