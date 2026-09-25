"""Lucide store: sloping canopy, repeated rounded scallops and simple facade. Reduced four scallops to three; source wall marking preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b4fbca27-9be1-465c-821d-8b7db21f4d87'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_b4fbca27-9be1-465c-821d-8b7db21f4d87.svg'
AUTHOR = 'gpt-6'

class StorefrontOpenFacade(Solo48):
    icon_id = 'storefront-open-facade'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    aliases = ()
    keywords = ('shop', 'storefront', 'store', 'awning', 'retail', 'building', 'market')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42); three equal scallops for native readability.
        self.add_line('canopy-1',(6, 16),(10, 6))
        self.add_line('canopy-2',(10, 6),(38, 6))
        self.add_line('canopy-3',(38, 6),(42, 16))
        for index,x in enumerate((42,30,18)):
            self.add_arc(f'scallop-{index}',(x,16),(x-12,16),radius_x=6,sweep=True)
        self.add_contour('awning','canopy-1','canopy-2','canopy-3','scallop-0','scallop-1','scallop-2',closed=True)
        self.add_polyline('wall',(6,16),(6,42),(24,42),(42,42),(42,16))
        self.relate('connect','wall','awning')
