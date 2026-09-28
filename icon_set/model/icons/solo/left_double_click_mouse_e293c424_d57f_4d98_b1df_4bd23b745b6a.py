"""Double-click mouse with tangent capsule ends, informed by Lucide mouse.

The right version mirrors the left; the offset reserves room for both click arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e293c424-d57f-4d98-b1df-4bd23b745b6a'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/left double click mouse_e293c424-d57f-4d98-b1df-4bd23b745b6a.svg'
AUTHOR = 'gpt-6'

class LeftDoubleClickMouse(Solo48):
    icon_id = 'left-double-click-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "computers"
    categories = ("computers", "primitives")
    aliases = ()
    keywords = ('mouse', 'double click', 'left click', 'cursor', 'pointer', 'input', 'peripheral', 'computer')

    def build(self) -> None:
        # Plan: an elliptical capsule and attached button, with two nested
        # click arcs. Shared centres and 9-unit radius steps preserve clearance.
        # VRECT_L ink extremes: (6, 2)-(42, 46).
        cx, shoulder_y, lower_y = 33, 32, 34
        rx, ry, click_step = 7, 10, 9
        mirror = False

        def point(x, y):
            return (48 - x if mirror else x, y)

        def arc(name, start, end, radius_x, radius_y, sweep=True):
            self.add_arc(name, point(*start), point(*end),
                         radius_x=radius_x, radius_y=radius_y,
                         sweep=not sweep if mirror else sweep)

        arc('upper-right', (cx, shoulder_y - ry), (cx + rx, shoulder_y), rx, ry)
        self.add_line('right', point(cx + rx, shoulder_y), point(cx + rx, lower_y))
        arc('lower', (cx + rx, lower_y), (cx - rx, lower_y), rx, ry)
        self.add_line('left', point(cx - rx, lower_y), point(cx - rx, shoulder_y))
        arc('upper-left', (cx - rx, shoulder_y), (cx, shoulder_y - ry), rx, ry)
        self.add_contour('body', 'upper-right', 'right', 'lower', 'left', 'upper-left', closed=True)
        turn = 4
        self.add_line('button-v', point(cx, shoulder_y - ry), point(cx, shoulder_y - turn))
        arc('button-turn', (cx, shoulder_y - turn), (cx - turn, shoulder_y), turn, turn)
        self.add_line('button-h', point(cx - turn, shoulder_y), point(cx - rx, shoulder_y))
        self.add_contour('button', 'button-v', 'button-turn', 'button-h', closed=False)
        self.relate('connect', 'body', 'button')
        for index, name in enumerate(('click', 'second-click'), start=1):
            click_rx, click_ry = rx + index * click_step, ry + index * click_step
            arc(name, (cx - click_rx, shoulder_y), (cx, shoulder_y - click_ry), click_rx, click_ry)
