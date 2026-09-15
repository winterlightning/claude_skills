"""Moved capsule end centers inward with unchanged circular radius; retained the wheel.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: mouse: tangent capsule ends.
"""
# Independent repair of middle-click-mouse; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cf403615-f73e-5946-a667-219e0a5bdbbe'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/middle click mouse_cf403615-f73e-5946-a667-219e0a5bdbbe.svg'
AUTHOR = 'gpt-6'

class MiddleClickMouse(Solo48):
    icon_id = 'middle-click-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('mouse', 'middle click', 'scroll wheel', 'click', 'cursor', 'input', 'peripheral', 'computer')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_arc('top', (8, 20), (40, 20), radius_x=16, radius_y=16, sweep=True)
        self.add_line('right', (40, 20), (40, 28))
        self.add_arc('bottom', (40, 28), (8, 28), radius_x=16, radius_y=16, sweep=True)
        self.add_line('left', (8, 28), (8, 20))
        self.add_contour('body', 'top', 'right', 'bottom', 'left', closed=True)
        self.add_line('wheel', (24, 13), (24, 21))
