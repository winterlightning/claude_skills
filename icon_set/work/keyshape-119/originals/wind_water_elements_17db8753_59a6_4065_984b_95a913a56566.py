"""Two droplet outlines sit diagonally apart, with the larger droplet at the lower right. Curled wind strokes occupy the upper-right space and a short diagonal stroke separates the drops.

Retained two full drops and a single upper curl; removed small detached stroke.
Construction reference: Lucide wind tangent curl; teardrops authored from paired outlines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17db8753-59a6-4065-984b-95a913a56566'
SOURCE_PATH = 'pictographic-primitives/weather/elements_17db8753-59a6-4065-984b-95a913a56566.svg'
AUTHOR = 'gpt-6'

class WindWaterElements(Solo48):
    icon_id = 'wind-water-elements'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('element', 'wind', 'water', 'droplet', 'air', 'weather')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_line('small-left', (6, 16), (12, 8))
        self.add_line('small-right', (12, 8), (20, 16))
        self.add_arc('small-bottom', (20, 16), (6, 16), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('small', 'small-left', 'small-right', 'small-bottom', closed=True)
        self.add_line('large-left', (24, 36), (34, 26))
        self.add_line('large-right', (34, 26), (42, 36))
        self.add_arc('large-bottom', (42, 36), (24, 36), radius_x=10, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('large', 'large-left', 'large-right', 'large-bottom', closed=True)
        self.add_line('wind-run', (30, 17), (40, 17))
        self.add_arc('wind-curl', (40, 17), (40, 9), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_contour('wind', 'wind-run', 'wind-curl', closed=False)
