"""Inset the arrow and root circle without changing branch terminals.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: usb: branching shaft and distinct terminals; intentional asymmetry.
"""
# Independent repair of usb-symbol; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '62d28cec-8386-49e8-9825-a759c8b2ae50'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/usb port_62d28cec-8386-49e8-9825-a759c8b2ae50.svg'
AUTHOR = 'gpt-6'

class UsbSymbol(Solo48):
    icon_id = 'usb-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ('usb-trident',)
    keywords = ('usb', 'port', 'symbol', 'connector', 'trident', 'data', 'plug', 'computer')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_polyline('shaft', (24, 4), (24, 28), (24, 34))
        self.add_polyline('arrowhead', (18, 8), (24, 4), (30, 8))
        self.relate('connect', 'shaft', 'arrowhead')
        self.add_arc('root-ne', (24, 34), (29, 39), radius_x=5)
        self.add_arc('root-se', (29, 39), (24, 44), radius_x=5)
        self.add_arc('root-sw', (24, 44), (19, 39), radius_x=5)
        self.add_arc('root-nw', (19, 39), (24, 34), radius_x=5)
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
