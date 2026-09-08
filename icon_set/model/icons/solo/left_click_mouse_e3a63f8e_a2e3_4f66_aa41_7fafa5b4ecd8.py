"""Capsule mouse and left button with one concentric click arcs. Lucide mouse semicircular ends. Offset body reserves signal space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3a63f8e-a2e3-4f66-aa41-7fafa5b4ecd8'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/left click mouse_e3a63f8e-a2e3-4f66-aa41-7fafa5b4ecd8.svg'
AUTHOR = 'astra-chatgpt'

class LeftClickMouse(Solo48):
    icon_id = 'left-click-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('mouse', 'click', 'left click', 'cursor', 'pointer', 'input', 'peripheral', 'computer')

    def build(self) -> None:
        self.add_arc('upper-right', (28, 10), (40, 22), radius_x=12, radius_y=12, sweep=True)
        self.add_line('right', (40, 22), (40, 34))
        self.add_arc('lower', (40, 34), (16, 34), radius_x=12, radius_y=12, sweep=True)
        self.add_line('left', (16, 34), (16, 22))
        self.add_arc('upper-left', (16, 22), (28, 10), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('body', 'upper-right', 'right', 'lower', 'left', 'upper-left', closed=True)
        self.add_line('button-v', (28, 10), (28, 18))
        self.add_arc('button-turn', (28, 18), (24, 22), radius_x=4, radius_y=4, sweep=True)
        self.add_line('button-h', (24, 22), (16, 22))
        self.add_contour('button', 'button-v', 'button-turn', 'button-h', closed=False)
        self.relate('connect', 'body', 'button')
        self.add_arc('click', (8, 22), (28, 2), radius_x=20, radius_y=20, sweep=True)
