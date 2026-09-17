"""A curved water droplet above three detached spray rays. Repaired in place from bad-stroke feedback."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50c9772d-4b0e-5b7b-b887-32b3170d0404'
SOURCE_PATH = 'pictographic-primitives/weather/pressure cleaning_50c9772d-4b0e-5b7b-b887-32b3170d0404.svg'
AUTHOR = 'gpt-6'

class WaterSpray(Solo48):
    icon_id = 'water-spray'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('water', 'spray', 'cleaning', 'pressure', 'droplet', 'wash')

    def build(self) -> None:
        # A curved, pointed droplet above three mirrored spray rays.
        # Lucide droplet informs curved shoulders rather than a triangular cap.
        # HRECT_L centerline extremes: (4, 8)-(44, 40).
        self.add_arc('drop-right', (24, 8), (32, 20), radius_x=14)
        self.add_arc('drop-bottom', (32, 20), (16, 20), radius_x=8)
        self.add_arc('drop-left', (16, 20), (24, 8), radius_x=14)
        self.add_contour('drop', 'drop-right', 'drop-bottom', 'drop-left', closed=True)
        for side, x1, x2 in [('left', 11, 4), ('right', 37, 44)]:
            self.add_line('spray-' + side, (x1, 31), (x2, 40))
        self.add_line('spray-middle', (24, 37), (24, 40))
