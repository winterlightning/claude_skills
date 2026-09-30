"""Move the camera band upward, keeping the lens and flash rays.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (smartphone-front-camera-flash VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class SmartphoneFrontCameraFlash(Container64):
    icon_id = 'smartphone-front-camera-flash'
    keyshape = Keyshape.VRECT_M
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_arc('body-0', (46, 12), (52, 18), radius_x=6)
        self.add_line('body-1', (52, 18), (52, 54))
        self.add_arc('body-2', (52, 54), (46, 60), radius_x=6)
        self.add_line('body-3', (46, 60), (18, 60))
        self.add_arc('body-4', (18, 60), (12, 54), radius_x=6)
        self.add_line('body-5', (12, 54), (12, 18))
        self.add_arc('body-6', (12, 18), (18, 12), radius_x=6)
        self.add_line('divider', (12, 22), (52, 22))
        self.add_dot('camera', (32, 14))
        self.add_line('ray-top', (32, 4), (32, 6))
        self.add_line('ray-left', (23, 4), (25, 6))
        self.add_line('ray-right', (41, 4), (39, 6))
        self.add_line('ray-west', (24, 14), (26, 14))
        self.add_line('ray-east', (38, 14), (40, 14))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6')
        self.relate('connect', 'divider', 'body')
