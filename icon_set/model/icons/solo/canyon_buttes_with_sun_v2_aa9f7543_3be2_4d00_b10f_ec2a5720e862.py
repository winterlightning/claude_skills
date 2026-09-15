"""Square envelope; moved the sun down one unit without changing its radius or the buttes.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aa9f7543-3be2-4d00-b10f-ec2a5720e862'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/grand canyon usa_aa9f7543-3be2-4d00-b10f-ec2a5720e862.svg'
AUTHOR = 'gpt-6'

class CanyonButtesWithSunVariant2(Solo48):
    icon_id = 'canyon-buttes-with-sun-v2'
    variant_of = 'canyon-buttes-with-sun'
    variant_label = 'Shared ink reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('canyon', 'butte', 'mesa', 'rock', 'desert', 'usa', 'landscape', 'nature', 'sun')

    def build(self) -> None:
        """Centerline review: preserve the silhouette; remove duplicated ink and split real attachments into shared nodes."""
        self.add_polyline('buttes', (6, 42), (7, 17), (17, 17), (22, 42))
        self.add_polyline('right-butte', (29, 42), (33, 28), (41, 28), (42, 42))
        self.add_polyline('ground', (6, 42), (22, 42), (29, 42), (42, 42))
        self.relate('connect', 'right-butte', 'ground')
        self.relate('connect', 'buttes', 'ground')
        self.add_arc('sun-top', (28, 11), (38, 11), radius_x=5, sweep=True)
        self.add_arc('sun-bottom', (38, 11), (28, 11), radius_x=5, sweep=True)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
