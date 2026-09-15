"""A round chemistry flask with a short neck and a rounded lip.

Keyshape VRECT_L: (8, 0, 56, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide flask-round informs the bulb, neck and separate lip; no liquid line added.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart does not clear, check does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class RoundBottomChemistryFlaskRoundedRim(Container64):
    icon_id = 'round-bottom-chemistry-flask-rounded-rim'
    keyshape = Keyshape.VRECT_L
    aliases = ('round-flask-rounded-rim',)
    keywords = ('round', 'bottom', 'chemistry', 'flask', 'rounded', 'rim')

    def build(self) -> None:
        self.add_line('neck-left', (24, 10), (24, 18))
        self.add_arc('bulb-left-top', (24, 18), (10, 40), radius_x=14, radius_y=22, sweep=False, large_arc=False)
        self.add_arc('bulb-bottom', (10, 40), (54, 40), radius_x=22, radius_y=22, sweep=False, large_arc=False)
        self.add_arc('bulb-right-top', (54, 40), (40, 18), radius_x=14, radius_y=22, sweep=False, large_arc=False)
        self.add_line('neck-right', (40, 18), (40, 10))
        self.add_contour('vessel', 'neck-left', 'bulb-left-top', 'bulb-bottom', 'bulb-right-top', 'neck-right', closed=False)
        self.add_line('rim0', (24, 2), (40, 2))
        self.add_arc('rim1', (40, 2), (44, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('rim2', (44, 6), (44, 6))
        self.add_arc('rim3', (44, 6), (40, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('rim4', (40, 10), (24, 10))
        self.add_arc('rim5', (24, 10), (20, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('rim6', (20, 6), (20, 6))
        self.add_arc('rim7', (20, 6), (24, 2), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('rim', 'rim0', 'rim1', 'rim2', 'rim3', 'rim4', 'rim5', 'rim6', 'rim7', closed=True)
        self.relate("connect", 'rim', 'vessel')
