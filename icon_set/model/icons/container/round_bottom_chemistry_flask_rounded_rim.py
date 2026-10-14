"""A round chemistry flask with a short neck and a rounded lip.

Keyshape VRECT_L: (8, 0, 56, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide flask-round informs the bulb, neck and separate lip; no liquid line added.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (round-bottom-chemistry-flask-rounded-rim VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RoundBottomChemistryFlaskRoundedRim(Container64):
    icon_id = 'round-bottom-chemistry-flask-rounded-rim'
    keyshape = Keyshape.VRECT_L
    aliases = ('round-flask-rounded-rim',)
    keywords = ('round', 'bottom', 'chemistry', 'flask', 'rounded', 'rim')

    def build(self) -> None:
        # VRECT_L (was VRECT_M): the round-bottom body of round-bottom-chemistry-flask (10..54, bottom at 60) under
        # a short neck and the rounded rim, so the bulb holds a symbol of 24 with a 4 px gap (was 20.5).
        self.add_line('neck-left', (26, 12), (26, 15))
        self.add_arc('bulb-left-top', (26, 15), (10, 38), radius_x=16, radius_y=23, sweep=False)
        self.add_arc('bulb-bottom', (10, 38), (54, 38), radius_x=22, sweep=False)
        self.add_arc('bulb-right-top', (54, 38), (38, 15), radius_x=16, radius_y=23, sweep=False)
        self.add_line('neck-right', (38, 15), (38, 12))
        self.add_line('rim0', (25, 4), (39, 4))
        self.add_arc('rim1', (39, 4), (39, 12), radius_x=4)
        self.add_line('rim2', (39, 12), (25, 12))
        self.add_arc('rim3', (25, 12), (25, 4), radius_x=4)
        self.add_contour('vessel', 'neck-left', 'bulb-left-top', 'bulb-bottom', 'bulb-right-top', 'neck-right')
        self.add_contour('rim', 'rim0', 'rim1', 'rim2', 'rim3', closed=True)
        self.relate('connect', 'vessel', 'rim')
