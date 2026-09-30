"""Increase van body height, retaining the stepped roof, sloping windshield and wheels.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (delivery-van-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '3179d20f-4838-4c26-a054-f8bbabbc255f'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_3179d20f-4838-4c26-a054-f8bbabbc255f.svg'
AUTHOR = 'claude-opus-5-5'


class DeliveryVanContainer(Container64):
    icon_id = 'delivery-van-container'
    keyshape = Keyshape.SQUARE
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('body-0', (12, 51), (6, 51))
        self.add_line('body-1', (6, 51), (6, 6))
        self.add_line('body-2', (6, 6), (42, 6))
        self.add_line('body-3', (42, 6), (42, 22))
        self.add_line('body-4', (42, 22), (46, 22))
        self.add_line('body-5', (46, 22), (58, 34))
        self.add_line('body-6', (58, 34), (58, 51))
        self.add_line('body-7', (58, 51), (51, 51))
        self.add_line('sill', (26, 51), (37, 51))
        self.add_line('window', (47, 34), (58, 34))
        self.add_arc('wheel-15-0', (12, 51), (26, 51), radius_x=7)
        self.add_arc('wheel-15-1', (26, 51), (12, 51), radius_x=7)
        self.add_arc('wheel-48-0', (37, 51), (51, 51), radius_x=7)
        self.add_arc('wheel-48-1', (51, 51), (37, 51), radius_x=7)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7')
        self.add_contour('wheel-15', 'wheel-15-0', 'wheel-15-1', closed=True)
        self.add_contour('wheel-48', 'wheel-48-0', 'wheel-48-1', closed=True)
        self.relate('connect', 'window', 'body')
        self.relate('connect', 'body', 'wheel-15')
        self.relate('connect', 'sill', 'wheel-15')
        self.relate('connect', 'body', 'wheel-48')
        self.relate('connect', 'sill', 'wheel-48')
