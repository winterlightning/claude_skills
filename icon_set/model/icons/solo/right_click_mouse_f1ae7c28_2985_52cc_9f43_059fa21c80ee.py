"""A capsule mouse isolates its right button beside one click arc.

Keyshape VRECT_L: visible extremes (6, 2, 42, 46).
Lucide mouse: tangent capsule sides and equal end radii. Source right-button division and click count retained. Asymmetry reserves space for right-side feedback."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1ae7c28-2985-52cc-9f43-059fa21c80ee'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/right click mouse_f1ae7c28-2985-52cc-9f43-059fa21c80ee.svg'
AUTHOR = 'gpt-6'


class RightClickMouse(Solo48):
    icon_id = 'right-click-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('mouse', 'click', 'right click', 'cursor', 'pointer', 'input', 'peripheral', 'computer')

    def build(self) -> None:
        self.add_arc('body-ne', (19, 13), (30, 24), radius_x=11, sweep=True)
        self.add_line('body-r', (30, 24), (30, 33))
        self.add_arc('body-se', (30, 33), (19, 44), radius_x=11, sweep=True)
        self.add_arc('body-sw', (19, 44), (8, 33), radius_x=11, sweep=True)
        self.add_line('body-l', (8, 33), (8, 24))
        self.add_arc('body-nw', (8, 24), (19, 13), radius_x=11, sweep=True)
        self.add_contour('body', 'body-ne', 'body-r', 'body-se', 'body-sw', 'body-l', 'body-nw', closed=True)
        self.add_line('button-v', (19, 13), (19, 20))
        self.add_arc('button-round', (19, 20), (23, 24), radius_x=4, sweep=False)
        self.add_line('button-h', (23, 24), (30, 24))
        self.add_contour('button', 'button-v', 'button-round', 'button-h', closed=False)
        self.relate("connect", 'body', 'button')
        self.add_arc('click', (20, 4), (40, 24), radius_x=20, sweep=True)
