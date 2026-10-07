"""Broaden and deepen the cargo box; keep a compact cab and both wheels.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (cargo-delivery-truck-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '131a3477-dd9d-4552-84ba-f2f3f7a573ed'
SOURCE_PATH = 'pictographic-primitives/transportation/truck 1_131a3477-dd9d-4552-84ba-f2f3f7a573ed.svg'
AUTHOR = 'claude-opus-5-5'


class CargoDeliveryTruckContainer(Container64):
    icon_id = 'cargo-delivery-truck-container'
    keyshape = Keyshape.SQUARE
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Cargo box 6..44 (was 6..40) with a narrower cab and the front wheel under the cab corner, so the cargo
        # box holds a symbol of 26 with a 4 px gap (was 20).
        self.add_line('body-0', (13, 52), (6, 52))
        self.add_line('body-1', (6, 52), (6, 6))
        self.add_line('body-2', (6, 6), (44, 6))
        self.add_line('body-3', (44, 6), (44, 41))
        self.add_line('cab-0', (44, 25), (50, 25))
        self.add_arc('cab-1', (50, 25), (58, 33), radius_x=8)
        self.add_line('cab-2', (58, 33), (58, 52))
        self.add_line('windshield', (50, 33), (58, 33))
        self.add_line('axle', (25, 52), (46, 52))
        self.add_arc('wheel-rear-0', (13, 52), (25, 52), radius_x=6)
        self.add_arc('wheel-rear-1', (25, 52), (13, 52), radius_x=6)
        self.add_arc('wheel-front-0', (46, 52), (58, 52), radius_x=6)
        self.add_arc('wheel-front-1', (58, 52), (46, 52), radius_x=6)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3')
        self.add_contour('cab', 'cab-0', 'cab-1', 'cab-2')
        self.add_contour('wheel-rear', 'wheel-rear-0', 'wheel-rear-1', closed=True)
        self.add_contour('wheel-front', 'wheel-front-0', 'wheel-front-1', closed=True)
        self.relate('connect', 'body', 'cab')
        self.relate('connect', 'windshield', 'cab')
        self.relate('connect', 'axle', 'wheel-rear')
        self.relate('connect', 'body', 'wheel-rear')
        self.relate('connect', 'cab', 'wheel-front')
        self.relate('connect', 'axle', 'wheel-front')
