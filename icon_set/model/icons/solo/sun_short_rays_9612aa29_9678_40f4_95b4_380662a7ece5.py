"""A circular sun is surrounded by eight detached straight rays arranged evenly around its center. The open round disk and opposing rays give the subject a balanced radial silhouette.

Eight paired rays share the disk center; no features dropped.
Construction reference: Lucide sun: circular disk and eight radial straight rays.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9612aa29-9678-40f4-95b4-380662a7ece5'
SOURCE_PATH = 'pictographic-primitives/weather/weather sun_9612aa29-9678-40f4-95b4-380662a7ece5.svg'
AUTHOR = 'gpt-6'

class SunShortRays(Solo48):
    icon_id = 'sun-short-rays'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('sun', 'sunshine', 'daylight', 'weather', 'solar', 'sky')

    def build(self) -> None:
        # Live CIRCLE visible bounds: (2, 2, 46, 46).
        self.add_arc('disk-top', (15, 24), (33, 24), radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('disk-bottom', (33, 24), (15, 24), radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_contour('disk', 'disk-top', 'disk-bottom', closed=True)
        self.add_line('ray-0', (24, 6), (24, 6))
        self.add_line('ray-1', (24, 42), (24, 42))
        self.add_line('ray-2', (6, 24), (6, 24))
        self.add_line('ray-3', (42, 24), (42, 24))
        self.add_line('ray-4', (10, 10), (11, 11))
        self.add_line('ray-5', (37, 37), (38, 38))
        self.add_line('ray-6', (10, 38), (11, 37))
        self.add_line('ray-7', (37, 11), (38, 10))
