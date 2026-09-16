"""A circular towel holder hangs beneath a centered bracket and wall bar.

SQUARE fits the wide bar and hanging ring: ink (0,0)-(64,64),
centerline (2,2)-(62,62). Reference: supplied failed SVG; Lucide circle original
and atomic-debug informed the circular ring. No direct towel-ring match was
used. A longer hanger and smaller ring give the bracket 9 units of centerline
clearance. All parts remain centered on x=32; no identifying detail was removed.

Hosting (compose.py): plus, heart valid; check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'towel-ring'
SOURCE_PATH = 'icon_set/dist/failed/container64/towel-ring.svg'
AUTHOR = 'gpt-6'


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
        # Plan: centered bracket, hanger and circle share one axis; 9u clearance.
        axis, ring_top, ring_bottom = 32, 24, 62
        ring_radius = (ring_bottom - ring_top) // 2
        hanger_start, ring_join = (axis, 15), (axis, ring_top)
        self.add_line('hanger', hanger_start, ring_join)
        self.relate('connect', 'hanger', 'bracket')
        self.add_arc('ring-right', ring_join, (axis, ring_bottom), radius_x=ring_radius)
        self.add_arc('ring-left', (axis, ring_bottom), ring_join, radius_x=ring_radius)
        self.add_contour('ring', 'ring-right', 'ring-left', closed=True)
        self.relate('connect', 'hanger', 'ring')
