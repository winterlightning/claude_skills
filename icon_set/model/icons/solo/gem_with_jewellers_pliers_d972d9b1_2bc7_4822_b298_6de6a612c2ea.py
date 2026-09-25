"""Opened the gem facet band and inset the handle ends and joint.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: gem: pointed outline and a single broad facet.
"""
# Independent repair of gem-with-jewellers-pliers; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd972d9b1-2bc7-4822-b298-6de6a612c2ea'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/jewelry maker_d972d9b1-2bc7-4822-b298-6de6a612c2ea.svg'
AUTHOR = 'gpt-6'

class GemWithJewellersPliers(Solo48):
    icon_id = 'gem-with-jewellers-pliers'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('gem', 'with', 'jewellers', 'pliers')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:

        def line(n, a, b):
            self.add_line(n, a, b)

        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def contour(n, *parts, closed=False):
            self.add_contour(n, *parts, closed=closed)

        def connect(a, b):
            self.relate('connect', a, b)

        def circle(n, x, y, r, ry=None):
            arc(n + '-top', (x - r, y), (x + r, y), r, ry)
            arc(n + '-bottom', (x + r, y), (x - r, y), r, ry)
            contour(n, n + '-top', n + '-bottom', closed=True)
        self.add_polyline('gem', (8, 12), (14, 4), (34, 4), (40, 12), (24, 22), closed=True)
        line('facet', (8, 12), (40, 12))
        connect('gem', 'facet')
        self.add_polyline('pliers-left', (11, 44), (15, 29), (24, 35))
        self.add_polyline('pliers-right', (37, 44), (33, 29), (24, 35))
        connect('pliers-left', 'pliers-right')
        line('joint-post', (24, 35), (24, 38))
        connect('pliers-left', 'joint-post')
        connect('pliers-right', 'joint-post')
        circle('joint', 24, 41, 3)
        connect('joint-post', 'joint')
