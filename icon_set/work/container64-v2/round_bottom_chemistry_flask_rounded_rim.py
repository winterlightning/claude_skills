"""A round chemistry flask with a short neck and a rounded lip.

Keyshape VRECT_L: (8, 0, 56, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide flask-round informs the bulb, neck and separate lip; no liquid line added.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (round-bottom-chemistry-flask-rounded-rim VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class RoundBottomChemistryFlaskRoundedRim(Container64):
    icon_id = 'round-bottom-chemistry-flask-rounded-rim'
    keyshape = Keyshape.VRECT_M
    aliases = ('round-flask-rounded-rim',)
    keywords = ('round', 'bottom', 'chemistry', 'flask', 'rounded', 'rim')

    def build(self) -> None:
        self.add_line('neck-left', (25, 12), (25, 20))
        self.add_arc('bulb-left-top', (25, 20), (12, 38), radius_x=13, radius_y=18, sweep=False)
        self.add_arc('bulb-bottom', (12, 38), (52, 38), radius_x=20, radius_y=22, sweep=False)
        self.add_arc('bulb-right-top', (52, 38), (39, 20), radius_x=13, radius_y=18, sweep=False)
        self.add_line('neck-right', (39, 20), (39, 12))
        self.add_line('rim0', (25, 4), (39, 4))
        self.add_arc('rim1', (39, 4), (43, 8), radius_x=4)
        self.add_dot('rim2', (43, 8))
        self.add_arc('rim3', (43, 8), (39, 12), radius_x=4)
        self.add_line('rim4', (39, 12), (25, 12))
        self.add_arc('rim5', (25, 12), (21, 8), radius_x=4)
        self.add_dot('rim6', (21, 8))
        self.add_arc('rim7', (21, 8), (25, 4), radius_x=4)
        self.add_contour('vessel', 'neck-left', 'bulb-left-top', 'bulb-bottom', 'bulb-right-top', 'neck-right')
        self.add_contour('rim', 'rim0', 'rim1', 'rim2', 'rim3', 'rim4', 'rim5', 'rim6', 'rim7', closed=True)
        self.relate('connect', 'rim', 'vessel')
