"""The USB trident stands alone with arrow, circle and square terminals.

VRECT_L visible bounds (6, 0)-(42, 48), centerlines (8, 2)-(40, 46).
Lucide usb informs the branching shaft and distinct terminal shapes. Rebuilt
upright on SOLO48 from the supplied reference, with its open arrowhead.
The different branch terminals preserve the symbol's intentional asymmetry.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62d28cec-8386-49e8-9825-a759c8b2ae50'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/usb port_62d28cec-8386-49e8-9825-a759c8b2ae50.svg'


class UsbSymbol(Solo48):
    icon_id = 'usb-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ('usb-trident',)
    keywords = ('usb', 'port', 'symbol', 'connector', 'trident', 'data', 'plug', 'computer')

    def build(self) -> None:
        self.add_polyline('shaft', (24, 2), (24, 28), (24, 36))
        self.add_polyline('arrowhead', (18, 8), (24, 2), (30, 8))
        self.relate('connect', 'shaft', 'arrowhead')

        self.add_arc('root-ne', (24, 36), (29, 41), radius_x=5)
        self.add_arc('root-se', (29, 41), (24, 46), radius_x=5)
        self.add_arc('root-sw', (24, 46), (19, 41), radius_x=5)
        self.add_arc('root-nw', (19, 41), (24, 36), radius_x=5)
        self.add_contour('root', 'root-ne', 'root-se', 'root-sw', 'root-nw', closed=True)
        self.relate('connect', 'shaft', 'root')

        self.add_arc('circle-ne', (12, 14), (16, 18), radius_x=4)
        self.add_arc('circle-se', (16, 18), (12, 22), radius_x=4)
        self.add_arc('circle-sw', (12, 22), (8, 18), radius_x=4)
        self.add_arc('circle-nw', (8, 18), (12, 14), radius_x=4)
        self.add_contour('circle', 'circle-ne', 'circle-se', 'circle-sw', 'circle-nw', closed=True)
        self.add_polyline('left-branch', (12, 22), (12, 24), (24, 28))
        self.add_polyline('square', (32, 14), (40, 14), (40, 22), (36, 22), (32, 22), closed=True)
        self.add_polyline('right-branch', (36, 22), (36, 24), (24, 28))
        self.relate('connect', 'circle', 'left-branch')
        self.relate('connect', 'square', 'right-branch')
        self.relate('connect', 'shaft', 'left-branch')
        self.relate('connect', 'shaft', 'right-branch')
        self.relate('connect', 'left-branch', 'right-branch')
