"""Two unequal flat-topped desert buttes under a sun; chips omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa9f7543-3be2-4d00-b10f-ec2a5720e862'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/grand canyon usa_aa9f7543-3be2-4d00-b10f-ec2a5720e862.svg'
AUTHOR = 'gpt-6'

class CanyonButtesWithSun(Solo48):
    icon_id = 'canyon-buttes-with-sun'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('canyon', 'butte', 'mesa', 'rock', 'desert', 'usa', 'landscape', 'nature', 'sun')

    def build(self) -> None:
        # HRECT_XL centerline extremes (6,6)-(42,42).
        self.add_polyline('buttes', (6, 42), (7, 17), (17, 17), (22, 42), (29, 42), (33, 28), (41, 28), (42, 42))
        self.add_line('ground', (6, 42), (42, 42))
        self.relate('connect', 'buttes', 'ground')
        self.add_arc('sun-top', (28, 10), (38, 10), radius_x=5, sweep=True)
        self.add_arc('sun-bottom', (38, 10), (28, 10), radius_x=5, sweep=True)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
