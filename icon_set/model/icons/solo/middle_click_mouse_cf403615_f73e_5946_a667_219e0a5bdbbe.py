"""Mouse with central wheel stroke; Lucide mouse semicircular ends. Wheel capsule simplified to round line. Intended extremes (8,2)-(40,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf403615-f73e-5946-a667-219e0a5bdbbe'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/middle click mouse_cf403615-f73e-5946-a667-219e0a5bdbbe.svg'

class MiddleClickMouse(Solo48):
    icon_id = 'middle-click-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('mouse', 'middle click', 'scroll wheel', 'click', 'cursor', 'input', 'peripheral', 'computer')

    def build(self) -> None:
        self.add_arc('top', (8, 18), (40, 18), radius_x=16, radius_y=16, sweep=True)
        self.add_line('right', (40, 18), (40, 30))
        self.add_arc('bottom', (40, 30), (8, 30), radius_x=16, radius_y=16, sweep=True)
        self.add_line('left', (8, 30), (8, 18))
        self.add_contour('body', 'top', 'right', 'bottom', 'left', closed=True)
        self.add_line('wheel', (24, 13), (24, 21))
