"""Standalone percent symbol as explicitly briefed. Lucide percent: equal open circles and diagonal slash; rotational symmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca0114c5-9aec-5dda-8cd8-5bd89ae0332a'
SOURCE_PATH = 'pictographic-primitives/shopping/discount_ca0114c5-9aec-5dda-8cd8-5bd89ae0332a.svg'
AUTHOR = 'gpt-6'

class PercentSymbolOpenCircles(Solo48):
    icon_id = 'percent-symbol-open-circles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('percent', 'discount', 'sale', 'percentage', 'rate', 'offer', 'symbol')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42).
        self.add_line('slash',(6,42),(42,6))
        radius = 6
        for index, center in enumerate(((6+radius,6+radius),(42-radius,42-radius))):
            x,y=center
            self.add_arc(f'ring-{index}-a',(x-radius,y),(x+radius,y),radius_x=radius)
            self.add_arc(f'ring-{index}-b',(x+radius,y),(x-radius,y),radius_x=radius)
            self.add_contour(f'ring-{index}',f'ring-{index}-a',f'ring-{index}-b',closed=True)
