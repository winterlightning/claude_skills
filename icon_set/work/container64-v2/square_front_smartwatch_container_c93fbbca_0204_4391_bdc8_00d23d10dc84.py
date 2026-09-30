"""Taller watch face with matching shorter strap ends.
Independent review variant of square-front-smartwatch-container. VRECT_L CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 32]. See container-fit-repair report for measured hosting results.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-front-smartwatch-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'c93fbbca-0204-4391-bdc8-00d23d10dc84'
SOURCE_PATH = 'pictographic-primitives/devices/smart watch square_c93fbbca-0204-4391-bdc8-00d23d10dc84.svg'
AUTHOR = 'claude-opus-5-5'


class SquareFrontSmartwatchContainer(Container64):
    icon_id = 'square-front-smartwatch-container'
    keyshape = Keyshape.VRECT_M
    category = 'devices'
    categories = ('devices', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('square', 'front', 'smartwatch', 'container')

    def build(self) -> None:
        self.add_line('face-0', (18, 12), (46, 12))
        self.add_arc('face-1', (46, 12), (52, 18), radius_x=6)
        self.add_line('face-2', (52, 18), (52, 46))
        self.add_arc('face-3', (52, 46), (46, 52), radius_x=6)
        self.add_line('face-4', (46, 52), (18, 52))
        self.add_arc('face-5', (18, 52), (12, 46), radius_x=6)
        self.add_line('face-6', (12, 46), (12, 18))
        self.add_arc('face-7', (12, 18), (18, 12), radius_x=6)
        self.add_line('top-strap-1', (22, 12), (24, 4))
        self.add_line('top-strap-2', (24, 4), (40, 4))
        self.add_line('top-strap-3', (40, 4), (42, 12))
        self.add_line('bottom-strap-1', (22, 52), (24, 60))
        self.add_line('bottom-strap-2', (24, 60), (40, 60))
        self.add_line('bottom-strap-3', (40, 60), (42, 52))
        self.add_contour('face', 'face-0', 'face-1', 'face-2', 'face-3', 'face-4', 'face-5', 'face-6', 'face-7', closed=True)
        self.add_contour('top-strap', 'top-strap-1', 'top-strap-2', 'top-strap-3')
        self.add_contour('bottom-strap', 'bottom-strap-1', 'bottom-strap-2', 'bottom-strap-3')
        self.relate('connect', 'face', 'top-strap')
        self.relate('connect', 'face', 'bottom-strap')
