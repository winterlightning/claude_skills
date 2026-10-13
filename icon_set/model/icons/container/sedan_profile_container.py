"""v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (sedan-profile-container HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '1fdb13eb-bc4d-44a6-bca4-d87dd2adb768'
SOURCE_PATH = 'pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg'
AUTHOR = 'claude-opus-5-5'


class SedanProfileContainer(Container64):
    icon_id = 'sedan-profile-container'
    keyshape = Keyshape.HRECT_M
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('sedan', 'profile', 'container')

    def build(self) -> None:
        self.add_line('body-0', (12, 46), (8, 47))
        self.add_arc('body-1', (8, 47), (4, 44), radius_x=4, radius_y=3)
        self.add_line('body-2', (4, 44), (4, 28))
        self.add_arc('body-3', (4, 28), (8, 24), radius_x=4)
        self.add_line('body-4', (8, 24), (14, 24))
        self.add_line('body-5', (14, 24), (24, 12))
        self.add_line('body-6', (24, 12), (36, 12))
        self.add_line('body-7', (36, 12), (46, 24))
        self.add_line('body-8', (46, 24), (56, 26))
        self.add_arc('body-9', (56, 26), (60, 30), radius_x=4)
        self.add_line('body-10', (60, 30), (60, 47))
        self.add_line('body-11', (60, 47), (52, 46))
        self.add_line('sill', (24, 46), (40, 46))
        self.add_arc('wheel-16-0', (12, 46), (24, 46), radius_x=6)
        self.add_arc('wheel-16-1', (24, 46), (12, 46), radius_x=6)
        self.add_arc('wheel-48-0', (40, 46), (52, 46), radius_x=6)
        self.add_arc('wheel-48-1', (52, 46), (40, 46), radius_x=6)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11')
        self.add_contour('wheel-16', 'wheel-16-0', 'wheel-16-1', closed=True)
        self.add_contour('wheel-48', 'wheel-48-0', 'wheel-48-1', closed=True)
        self.relate('connect', 'body', 'wheel-16')
        self.relate('connect', 'sill', 'wheel-16')
        self.relate('connect', 'body', 'wheel-48')
        self.relate('connect', 'sill', 'wheel-48')
