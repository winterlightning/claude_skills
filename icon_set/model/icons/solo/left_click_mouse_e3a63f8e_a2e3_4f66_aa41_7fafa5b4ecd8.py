"""Capsule mouse and left button with one separate click arc. Lucide mouse semicircular ends. Offset body reserves signal space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3a63f8e-a2e3-4f66-aa41-7fafa5b4ecd8'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/left click mouse_e3a63f8e-a2e3-4f66-aa41-7fafa5b4ecd8.svg'
AUTHOR = 'gpt-6'

class LeftClickMouse(Solo48):
    icon_id = 'left-click-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "computers"
    categories = ("computers", "primitives")
    aliases = ()
    keywords = ('mouse', 'click', 'left click', 'cursor', 'pointer', 'input', 'peripheral', 'computer')

    def build(self) -> None:
        self.add_arc('upper-right', (29, 13), (40, 24), radius_x=11, radius_y=11, sweep=True)
        self.add_line('right', (40, 24), (40, 33))
        self.add_arc('lower', (40, 33), (18, 33), radius_x=11, radius_y=11, sweep=True)
        self.add_line('left', (18, 33), (18, 24))
        self.add_arc('upper-left', (18, 24), (29, 13), radius_x=11, radius_y=11, sweep=True)
        self.add_contour('body', 'upper-right', 'right', 'lower', 'left', 'upper-left', closed=True)
        self.add_line('button-v', (29, 13), (29, 20))
        self.add_arc('button-turn', (29, 20), (25, 24), radius_x=4, radius_y=4, sweep=True)
        self.add_line('button-h', (25, 24), (18, 24))
        self.add_contour('button', 'button-v', 'button-turn', 'button-h', closed=False)
        self.relate('connect', 'body', 'button')
        self.add_arc('click', (8, 24), (28, 4), radius_x=20, radius_y=20, sweep=True)
