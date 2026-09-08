"""A rounded television cabinet with paired aerials and splayed feet.

Keyshape SQUARE: (0, 0, 64, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide tv informs the V aerial and rounded cabinet.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus does not clear, heart passes, check passes.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class RetroTelevisionWithAntenna(Container64):
    icon_id = 'retro-television-with-antenna'
    keyshape = Keyshape.SQUARE
    aliases = ('retro-tv', 'antenna-television')
    keywords = ('retro', 'television', 'with', 'antenna')

    def build(self) -> None:
        self.add_line('cabinet0', (12, 12), (52, 12))
        self.add_arc('cabinet1', (52, 12), (62, 22), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('cabinet2', (62, 22), (62, 44))
        self.add_arc('cabinet3', (62, 44), (52, 54), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('cabinet4', (52, 54), (12, 54))
        self.add_arc('cabinet5', (12, 54), (2, 44), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('cabinet6', (2, 44), (2, 22))
        self.add_arc('cabinet7', (2, 22), (12, 12), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('cabinet', 'cabinet0', 'cabinet1', 'cabinet2', 'cabinet3', 'cabinet4', 'cabinet5', 'cabinet6', 'cabinet7', closed=True)
        self.add_polyline('aerial', (22, 2), (32, 12), (42, 2), closed=False)
        self.relate("connect", 'aerial', 'cabinet')
        self.add_line('foot-left', (18, 54), (14, 62))
        self.add_line('foot-right', (46, 54), (50, 62))
        self.relate("connect", 'foot-left', 'cabinet')
        self.relate("connect", 'foot-right', 'cabinet')
