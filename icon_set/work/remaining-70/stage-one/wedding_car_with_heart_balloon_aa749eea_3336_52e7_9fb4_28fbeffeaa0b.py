# Repair: Move the car roof away from the heart balloon without altering either subject.
"""A right-facing wedding car tows a heart balloon; side decal, cans and ribbon details omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aa749eea-3336-52e7-9fb4-28fbeffeaa0b'
SOURCE_PATH = 'pictographic-primitives/romance/wedding car heart balloon_aa749eea-3336-52e7-9fb4-28fbeffeaa0b.svg'
AUTHOR = 'gpt-6'

class WeddingCarWithHeartBalloon(Solo48):
    icon_id = 'wedding-car-with-heart-balloon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/romance'
    aliases = ()
    keywords = ('car', 'wedding', 'balloon', 'heart', 'vehicle', 'celebration')

    def build(self) -> None:

        def heart(n, cx, y, r, tip):
            self.add_arc(n + '-l', (cx, y), (cx - 2 * r, y), radius_x=r, sweep=False)
            self.add_arc(n + '-shl', (cx - 2 * r, y), (cx - 2 * r + 2, y + 4), radius_x=5, sweep=False)
            self.add_line(n + '-sl', (cx - 2 * r + 2, y + 4), (cx, tip))
            self.add_line(n + '-sr', (cx, tip), (cx + 2 * r - 2, y + 4))
            self.add_arc(n + '-shr', (cx + 2 * r - 2, y + 4), (cx + 2 * r, y), radius_x=5, sweep=False)
            self.add_arc(n + '-r', (cx + 2 * r, y), (cx, y), radius_x=r, sweep=False)
            self.add_contour(n, n + '-l', n + '-shl', n + '-sl', n + '-sr', n + '-shr', n + '-r', closed=True)
        heart('balloon', 14, 10, 4, 20)
        self.add_arc('tether', (14, 20), (10, 28), radius_x=10, sweep=False)
        self.relate('connect', 'balloon', 'tether')
        self.add_polyline('body', (10, 28), (16, 28), (23, 24), (31, 24), (34, 28), (38, 28), (42, 32), (42, 38), (40, 38))
        self.relate('connect', 'body', 'tether')
        self.add_line('bumper-left', (8, 38), (6, 38))
        self.add_line('rear', (6, 38), (6, 32))
        self.add_arc('rear-corner', (6, 32), (10, 28), radius_x=4)
        self.add_contour('rear-body', 'bumper-left', 'rear', 'rear-corner')
        self.relate('connect', 'rear-body', 'body')
        for n, x in [('rear-wheel', 12), ('front-wheel', 36)]:
            self.add_arc(n + '-a', (x - 4, 38), (x + 4, 38), radius_x=4)
            self.add_arc(n + '-b', (x + 4, 38), (x - 4, 38), radius_x=4)
            self.add_contour(n, n + '-a', n + '-b', closed=True)
        self.add_line('sill', (16, 38), (32, 38))
        self.relate('connect', 'rear-wheel', 'rear-body')
        self.relate('connect', 'rear-wheel', 'sill')
        self.relate('connect', 'front-wheel', 'sill')
        self.relate('connect', 'front-wheel', 'body')
