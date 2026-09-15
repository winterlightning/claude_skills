"""A circular sun sits at the center of eight evenly spaced straight rays. The rays alternate between upright, horizontal, and diagonal directions around the empty round center.

Eight paired rays share the disk center; no features dropped.
Construction reference: Lucide sun: circular disk and eight radial straight rays.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08d492fb-d883-4e25-9423-f3721a0a418f'
SOURCE_PATH = 'pictographic-primitives/weather/weather sun_08d492fb-d883-4e25-9423-f3721a0a418f.svg'
AUTHOR = 'gpt-6'

class Sun(Solo48):
    icon_id = 'sun'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
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
