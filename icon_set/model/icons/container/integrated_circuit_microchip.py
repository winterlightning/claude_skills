"""A square chip enclosure with two connector pins on each side.

Keyshape SQUARE: centerline extremes recorded in build below.
Lucide microchip informs rounded package corners and straight, attached pins; the reference supplies the square, eight-pin layout.
Hosting (compose.py): plus review, heart review, check review.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (integrated-circuit-microchip SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class IntegratedCircuitMicrochip(Container64):
    icon_id = 'integrated-circuit-microchip'
    keyshape = Keyshape.SQUARE
    aliases = ('processor-chip',)
    keywords = ('integrated', 'circuit', 'microchip')

    def build(self) -> None:
        self.add_line('package-0', (20, 14), (44, 14))
        self.add_arc('package-1', (44, 14), (50, 20), radius_x=6)
        self.add_line('package-2', (50, 20), (50, 44))
        self.add_arc('package-3', (50, 44), (44, 50), radius_x=6)
        self.add_line('package-4', (44, 50), (20, 50))
        self.add_arc('package-5', (20, 50), (14, 44), radius_x=6)
        self.add_line('package-6', (14, 44), (14, 20))
        self.add_arc('package-7', (14, 20), (20, 14), radius_x=6)
        self.add_line('pin-top-22', (24, 6), (24, 14))
        self.add_line('pin-bottom-22', (24, 50), (24, 58))
        self.add_line('pin-left-22', (6, 24), (14, 24))
        self.add_line('pin-right-22', (50, 24), (58, 24))
        self.add_line('pin-top-42', (40, 6), (40, 14))
        self.add_line('pin-bottom-42', (40, 50), (40, 58))
        self.add_line('pin-left-42', (6, 40), (14, 40))
        self.add_line('pin-right-42', (50, 40), (58, 40))
        self.add_contour('package', 'package-0', 'package-1', 'package-2', 'package-3', 'package-4', 'package-5', 'package-6', 'package-7', closed=True)
        self.relate('connect', 'package', 'pin-top-22')
        self.relate('connect', 'package', 'pin-bottom-22')
        self.relate('connect', 'package', 'pin-left-22')
        self.relate('connect', 'package', 'pin-right-22')
        self.relate('connect', 'package', 'pin-top-42')
        self.relate('connect', 'package', 'pin-bottom-42')
        self.relate('connect', 'package', 'pin-left-42')
        self.relate('connect', 'package', 'pin-right-42')
