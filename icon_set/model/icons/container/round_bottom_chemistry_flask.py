"""A round chemistry flask with a short neck and a flat rim.

Keyshape VRECT_L: (8, 0, 56, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide flask-round informs the bulb, neck and separate lip; no liquid line added.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart does not clear, check does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class RoundBottomChemistryFlask(Container64):
    icon_id = 'round-bottom-chemistry-flask'
    keyshape = Keyshape.VRECT_L
    aliases = ('round-flask', 'laboratory-flask')
    keywords = ('round', 'bottom', 'chemistry', 'flask')

    def build(self) -> None:
        self.add_line('neck-left', (24, 2), (24, 18))
        self.add_arc('bulb-left-top', (24, 18), (10, 40), radius_x=14, radius_y=22, sweep=False, large_arc=False)
        self.add_arc('bulb-bottom', (10, 40), (54, 40), radius_x=22, radius_y=22, sweep=False, large_arc=False)
        self.add_arc('bulb-right-top', (54, 40), (40, 18), radius_x=14, radius_y=22, sweep=False, large_arc=False)
        self.add_line('neck-right', (40, 18), (40, 2))
        self.add_contour('vessel', 'neck-left', 'bulb-left-top', 'bulb-bottom', 'bulb-right-top', 'neck-right', closed=False)
        self.add_line('rim', (20, 2), (44, 2))
        self.relate("connect", 'rim', 'vessel')
