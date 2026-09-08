"""A circular towel holder hangs beneath a centered bracket and wall bar.

Keyshape SQUARE; visible bounds (0, 0, 64, 64); centerline extremes (2, 2)-(62, 62).
Construction reference: Lucide crosshair: paired semicircles; no direct towel-ring match, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class TowelRing(Container64):
    icon_id = 'towel-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('circular-towel-ring-hanger',)
    keywords = ('towel', 'ring')

    def build(self) -> None:
        self.add_line('mount-left', (2, 6), (27, 6))
        self.add_line('mount-right', (37, 6), (62, 6))
        self.add_line('bracket-top', (27, 2), (37, 2))
        self.add_line('bracket-right', (37, 2), (37, 10))
        self.add_arc('bracket-bottom', (37, 10), (27, 10), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('bracket-left', (27, 10), (27, 2))
        self.add_contour('bracket', 'bracket-top', 'bracket-right', 'bracket-bottom', 'bracket-left', closed=True)
        self.relate("connect", 'mount-left', 'bracket')
        self.relate("connect", 'mount-right', 'bracket')
        self.add_line('hanger', (32, 15), (32, 18))
        self.relate("connect", 'hanger', 'bracket')
        self.add_arc('ring-right', (32, 18), (32, 62), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('ring-left', (32, 62), (32, 18), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_contour('ring', 'ring-right', 'ring-left', closed=True)
        self.relate("connect", 'hanger', 'ring')
