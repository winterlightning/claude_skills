"""Capsule mouse and left button with two concentric click arcs. Lucide mouse semicircular ends. Offset body reserves signal space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e293c424-d57f-4d98-b1df-4bd23b745b6a'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/left double click mouse_e293c424-d57f-4d98-b1df-4bd23b745b6a.svg'
AUTHOR = 'astra-chatgpt'

class LeftDoubleClickMouse(Solo48):
    icon_id = 'left-double-click-mouse'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('mouse', 'double click', 'left click', 'cursor', 'pointer', 'input', 'peripheral', 'computer')

    def build(self) -> None:
        self.add_arc('upper-right', (32, 18), (43, 29), radius_x=11, radius_y=11, sweep=True)
        self.add_line('right', (43, 29), (43, 35))
        self.add_arc('lower', (43, 35), (21, 35), radius_x=11, radius_y=11, sweep=True)
        self.add_line('left', (21, 35), (21, 29))
        self.add_arc('upper-left', (21, 29), (32, 18), radius_x=11, radius_y=11, sweep=True)
        self.add_contour('body', 'upper-right', 'right', 'lower', 'left', 'upper-left', closed=True)
        self.add_line('button-v', (32, 18), (32, 25))
        self.add_arc('button-turn', (32, 25), (28, 29), radius_x=4, radius_y=4, sweep=True)
        self.add_line('button-h', (28, 29), (21, 29))
        self.add_contour('button', 'button-v', 'button-turn', 'button-h', closed=False)
        self.relate('connect', 'body', 'button')
        self.add_arc('click', (13, 29), (32, 10), radius_x=19, radius_y=19, sweep=True)
        self.add_arc('second-click', (5, 29), (32, 2), radius_x=27, radius_y=27, sweep=True)
