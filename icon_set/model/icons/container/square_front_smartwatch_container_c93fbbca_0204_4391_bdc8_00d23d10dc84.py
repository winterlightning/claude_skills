"""Taller watch face with matching shorter strap ends.
Independent review variant of square-front-smartwatch-container. VRECT_L CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 32]. See container-fit-repair report for measured hosting results."""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'c93fbbca-0204-4391-bdc8-00d23d10dc84'
SOURCE_PATH = 'pictographic-primitives/devices/smart watch square_c93fbbca-0204-4391-bdc8-00d23d10dc84.svg'
AUTHOR = 'gpt-6'

class SquareFrontSmartwatchContainer(Container64):
    icon_id = 'square-front-smartwatch-container'
    category = 'devices'
    categories = ('devices', 'other', 'primitives-generate')
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('square', 'front', 'smartwatch', 'container')

    def build(self):
        face_top, face_bottom = (10, 54)
        rect(self, 'face', 10, face_top, 54, face_bottom, 6)
        self.add_polyline('top-strap', (20, face_top), (22, 2), (42, 2), (44, face_top))
        self.add_polyline('bottom-strap', (20, face_bottom), (22, 62), (42, 62), (44, face_bottom))
        self.relate('connect', 'face', 'top-strap')
        self.relate('connect', 'face', 'bottom-strap')
