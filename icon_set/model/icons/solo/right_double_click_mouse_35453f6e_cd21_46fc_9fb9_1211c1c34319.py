"""A capsule mouse isolates its right button beside two click arcs.

Keyshape VRECT_XL: visible extremes (3, 0, 45, 48).
Lucide mouse: tangent capsule sides and equal end radii. Source right-button division and click count retained. Asymmetry reserves space for right-side feedback."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35453f6e-cd21-46fc-9fb9-1211c1c34319'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/right double click mouse_35453f6e-cd21-46fc-9fb9-1211c1c34319.svg'
AUTHOR = 'astra-chatgpt'


class RightDoubleClickMouse(Solo48):
    icon_id = 'right-double-click-mouse'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('mouse', 'double click', 'right click', 'cursor', 'pointer', 'input', 'peripheral', 'computer')

    def build(self) -> None:
        self.add_arc('body-ne', (17, 16), (29, 28), radius_x=12, sweep=True)
        self.add_line('body-r', (29, 28), (29, 34))
        self.add_arc('body-se', (29, 34), (17, 46), radius_x=12, sweep=True)
        self.add_arc('body-sw', (17, 46), (5, 34), radius_x=12, sweep=True)
        self.add_line('body-l', (5, 34), (5, 28))
        self.add_arc('body-nw', (5, 28), (17, 16), radius_x=12, sweep=True)
        self.add_contour('body', 'body-ne', 'body-r', 'body-se', 'body-sw', 'body-l', 'body-nw', closed=True)
        self.add_line('button-v', (17, 16), (17, 24))
        self.add_arc('button-round', (17, 24), (21, 28), radius_x=4, sweep=False)
        self.add_line('button-h', (21, 28), (29, 28))
        self.add_contour('button', 'button-v', 'button-round', 'button-h', closed=False)
        self.relate("connect", 'body', 'button')
        self.add_arc('click-inner', (17, 9), (36, 28), radius_x=19, sweep=True)
        self.add_arc('click-outer', (17, 2), (43, 28), radius_x=26, sweep=True)
