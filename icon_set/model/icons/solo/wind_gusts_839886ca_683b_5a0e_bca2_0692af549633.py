"""Three detached horizontal wind strokes sweep from left to right. The upper two curl upward at their right ends, while the shorter lower stroke curls downward.

Retained three gusts, removed tiny detached fragments; curls deliberately face with the source flow.
Construction reference: Lucide wind: tangent horizontal runs ending in semicircular curls.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '839886ca-683b-5a0e-bca2-0692af549633'
SOURCE_PATH = 'pictographic-primitives/weather/weather wind flow_839886ca-683b-5a0e-bca2-0692af549633.svg'
AUTHOR = 'gpt-6'

class WindGusts(Solo48):
    icon_id = 'wind-gusts'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('wind', 'gust', 'breeze', 'air', 'flow', 'weather')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_line('upper-run', (4, 18), (23, 18))
        self.add_arc('upper-curl', (23, 18), (23, 8), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_contour('upper', 'upper-run', 'upper-curl', closed=False)
        self.add_line('middle-run', (4, 27), (39, 27))
        self.add_arc('middle-curl', (39, 27), (39, 17), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_contour('middle', 'middle-run', 'middle-curl', closed=False)
        self.add_line('lower-run', (14, 36), (25, 36))
        self.add_arc('lower-curl', (25, 36), (25, 40), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('lower', 'lower-run', 'lower-curl', closed=False)
