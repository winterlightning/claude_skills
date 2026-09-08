"""A rounded square selection boundary made of separated strokes.

Keyshape SQUARE: chosen for the reference silhouette.
Lucide square-dashed: corner arcs and paired straight dashes; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class DashedRoundedSquare(Container64):
    icon_id = 'dashed-rounded-square'
    keyshape = Keyshape.SQUARE
    aliases = ("rounded-dashed-selection-box",)
    keywords = ('dashed', 'rounded', 'square')

    def build(self) -> None:
        self.add_arc('corner-0', (2, 10), (10, 2), radius_x=8, radius_y=8, sweep=True)
        self.add_line('dash-a-0', (20, 2), (27, 2))
        self.add_line('dash-b-0', (37, 2), (44, 2))
        self.add_arc('corner-1', (54, 2), (62, 10), radius_x=8, radius_y=8, sweep=True)
        self.add_line('dash-a-1', (62, 20), (62, 27))
        self.add_line('dash-b-1', (62, 37), (62, 44))
        self.add_arc('corner-2', (62, 54), (54, 62), radius_x=8, radius_y=8, sweep=True)
        self.add_line('dash-a-2', (44, 62), (37, 62))
        self.add_line('dash-b-2', (27, 62), (20, 62))
        self.add_arc('corner-3', (10, 62), (2, 54), radius_x=8, radius_y=8, sweep=True)
        self.add_line('dash-a-3', (2, 44), (2, 37))
        self.add_line('dash-b-3', (2, 27), (2, 20))
