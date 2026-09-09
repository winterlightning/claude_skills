# Variant of baby-head; parent file remains unchanged.
"""A circular baby head with one inward hair arc and no ears or shoulders. CIRCLE center (24,24), centerline radius 22. Lucide baby informs the single curl; face details remain omitted as in the parent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '454b702c-a035-5fa0-a3ec-ac065587fca8'
SOURCE_PATH = 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'
AUTHOR = 'gpt-6'

class BabyHeadVariant3(Solo48):
    icon_id = 'baby-head-v3'
    variant_of = 'baby-head'
    variant_label = 'Circular head and single hair curve'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('baby', 'head', 'infant', 'nursery')

    def build(self) -> None:
        # Circle centered (24,24), centerline radius 22. Ears and shoulders removed.
        self.add_arc('head-right', (24,2), (24,46), radius_x=22)
        self.add_arc('head-left', (24,46), (24,2), radius_x=22)
        self.add_contour('head', 'head-right', 'head-left', closed=True)
        self.add_arc('hair', (24,2), (24,16), radius_x=7)
        self.relate('connect', 'head', 'hair')
