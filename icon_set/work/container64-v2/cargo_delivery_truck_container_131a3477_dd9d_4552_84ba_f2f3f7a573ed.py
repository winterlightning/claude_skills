"""Broaden and deepen the cargo box; keep a compact cab and both wheels.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (cargo-delivery-truck-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

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
        self.add_line('body-0', (13, 52), (6, 52))
        self.add_line('body-1', (6, 52), (6, 6))
        self.add_line('body-2', (6, 6), (40, 6))
        self.add_line('body-3', (40, 6), (40, 41))
        self.add_line('cab-0', (40, 25), (48, 25))
        self.add_arc('cab-1', (48, 25), (58, 34), radius_x=10, radius_y=9)
        self.add_line('cab-2', (58, 34), (58, 52))
        self.add_line('cab-3', (58, 52), (50, 52))
        self.add_line('windshield', (48, 34), (58, 34))
        self.add_line('axle', (25, 52), (38, 52))
        self.add_arc('wheel-15-0', (13, 52), (25, 52), radius_x=6)
        self.add_arc('wheel-15-1', (25, 52), (13, 52), radius_x=6)
        self.add_arc('wheel-48-0', (38, 52), (50, 52), radius_x=6)
        self.add_arc('wheel-48-1', (50, 52), (38, 52), radius_x=6)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3')
        self.add_contour('cab', 'cab-0', 'cab-1', 'cab-2', 'cab-3')
        self.add_contour('wheel-15', 'wheel-15-0', 'wheel-15-1', closed=True)
        self.add_contour('wheel-48', 'wheel-48-0', 'wheel-48-1', closed=True)
        self.relate('connect', 'body', 'cab')
        self.relate('connect', 'windshield', 'cab')
        self.relate('connect', 'axle', 'wheel-15')
        self.relate('connect', 'body', 'wheel-15')
        self.relate('connect', 'cab', 'wheel-48')
        self.relate('connect', 'axle', 'wheel-48')
