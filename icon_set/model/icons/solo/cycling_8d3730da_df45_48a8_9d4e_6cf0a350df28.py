"""Cycling. Retains the rider and two equal wheels; no spokes or frame are added.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide bike: two equal wheels, detached head and angular rider; source contains no bicycle frame.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d3730da-df45-48a8-9d4e-6cf0a350df28'
SOURCE_PATH = 'pictographic-primitives/symbol/cycling_8d3730da-df45-48a8-9d4e-6cf0a350df28.svg'
AUTHOR = 'gpt-6'


class Cycling(Solo48):
    icon_id = 'cycling'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('cycling', 'bicycle', 'bike', 'cyclist', 'sport', 'ride', 'exercise', 'transport')

    def build(self) -> None:
        self.add_arc('rear-wheel-right', (11, 32), (11, 42), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('rear-wheel-left', (11, 42), (11, 32), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('rear-wheel', 'rear-wheel-right', 'rear-wheel-left', closed=True)
        self.add_arc('front-wheel-right', (37, 32), (37, 42), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('front-wheel-left', (37, 42), (37, 32), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('front-wheel', 'front-wheel-right', 'front-wheel-left', closed=True)
        self.add_arc('head-right', (34, 6), (34, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-left', (34, 14), (34, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-right', 'head-left', closed=True)
        self.add_polyline('rider', (22, 18), (16, 24), (24, 28), (24, 31))
        self.add_polyline('arm', (22, 18), (30, 23), (38, 23))
        self.relate("connect", 'rider', 'arm')
