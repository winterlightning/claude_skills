"""v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (sedan-profile-container HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.



v3 (2026-10-07): simplified car with the wheels centred on the body line (container-combination64): a symbol of 20/24 fits.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '1fdb13eb-bc4d-44a6-bca4-d87dd2adb768'
SOURCE_PATH = 'pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg'
AUTHOR = 'claude-opus-5-5'


class SedanProfileContainer(Container64):
    icon_id = 'sedan-profile-container'
    keyshape = Keyshape.SQUARE
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('sedan', 'profile', 'container')

    def build(self) -> None:
        # SQUARE: a tall cabin (roof 18..46 at 6, shoulders at 26) on a body whose bottom line (52) runs between
        # and around the wheels; the wheels (r6 at x 18 and 46) sit centred on that line and reach the keyshape at
        # 58. Mirrored about x = 32. Holds a symbol of 22 with a 4 px gap.
        self.add_line('body-0', (12, 52), (10, 52))
        self.add_arc('body-1', (10, 52), (6, 48), radius_x=4)
        self.add_line('body-2', (6, 48), (6, 30))
        self.add_arc('body-3', (6, 30), (10, 26), radius_x=4)
        self.add_line('body-4', (10, 26), (12, 26))
        self.add_line('body-5', (12, 26), (18, 6))
        self.add_line('body-6', (18, 6), (46, 6))
        self.add_line('body-7', (46, 6), (52, 26))
        self.add_line('body-8', (52, 26), (54, 26))
        self.add_arc('body-9', (54, 26), (58, 30), radius_x=4)
        self.add_line('body-10', (58, 30), (58, 48))
        self.add_arc('body-11', (58, 48), (54, 52), radius_x=4)
        self.add_line('body-12', (54, 52), (52, 52))
        self.add_line('sill', (24, 52), (40, 52))
        self.add_arc('wheel-18-0', (12, 52), (24, 52), radius_x=6)
        self.add_arc('wheel-18-1', (24, 52), (12, 52), radius_x=6)
        self.add_arc('wheel-46-0', (40, 52), (52, 52), radius_x=6)
        self.add_arc('wheel-46-1', (52, 52), (40, 52), radius_x=6)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12')
        self.add_contour('wheel-18', 'wheel-18-0', 'wheel-18-1', closed=True)
        self.add_contour('wheel-46', 'wheel-46-0', 'wheel-46-1', closed=True)
        self.relate('connect', 'body', 'wheel-18')
        self.relate('connect', 'body', 'wheel-46')
        self.relate('connect', 'sill', 'wheel-18')
        self.relate('connect', 'sill', 'wheel-46')
