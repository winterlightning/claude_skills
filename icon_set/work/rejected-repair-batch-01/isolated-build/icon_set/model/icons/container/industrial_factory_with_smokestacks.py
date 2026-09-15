"""A factory enclosure with a gabled roof between two tapering smokestacks.

Keyshape SQUARE: centerline extremes recorded in build below.
Lucide factory informs connected roof/body geometry; the supplied reference sets the mirrored stacks.
Hosting (compose.py): plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class IndustrialFactoryWithSmokestacks(Container64):
    icon_id = 'industrial-factory-with-smokestacks'
    keyshape = Keyshape.SQUARE
    aliases = ('factory-building',)
    keywords = ('industrial', 'factory', 'with', 'smokestacks')

    def build(self) -> None:
        # SQUARE centerline extremes: (2,2)-(62,62).
        self.add_polyline("building", (2,62), (2,34), (18,34), (32,24), (46,34), (62,34), (62,62), closed=True)
        self.add_polyline("stack-left", (4,34), (6,2), (14,2), (18,34))
        self.add_polyline("stack-right", (46,34), (50,2), (58,2), (60,34))
        self.relate("connect", "building", "stack-left")
        self.relate("connect", "building", "stack-right")
