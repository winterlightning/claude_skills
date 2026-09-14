"""A large pointed droplet occupies the upper center of the image. Four detached spray strokes spread downward beneath it, with the outer pair slanting farther outward.

Reduced four spray marks to three and rebuilt a complete droplet; bilateral symmetry.
Construction reference: No useful exact local match; paired tangent arc teardrop.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50c9772d-4b0e-5b7b-b887-32b3170d0404'
SOURCE_PATH = 'pictographic-primitives/weather/pressure cleaning_50c9772d-4b0e-5b7b-b887-32b3170d0404.svg'
AUTHOR = 'gpt-6'

class WaterSpray(Solo48):
    icon_id = 'water-spray'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('water', 'spray', 'cleaning', 'pressure', 'droplet', 'wash')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_line('drop-top-1', (16, 19), (24, 8))
        self.add_line('drop-top-2', (24, 8), (32, 19))
        self.add_arc('drop-bottom', (32, 19), (16, 19), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('drop', 'drop-top-1', 'drop-top-2', 'drop-bottom', closed=True)
        self.add_line('spray-left', (10, 31), (6, 40))
        self.add_line('spray-middle', (24, 36), (24, 40))
        self.add_line('spray-right', (38, 31), (42, 40))
