"""Spoked Wheel. Preserves exactly six spokes; integer 3:4:5 rim vertices give a balanced near-even arrangement.

CIRCLE visible extremes (2, 2, 46, 46); centerlines (4, 4, 44, 44).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1d7f358-4400-4823-8d56-c374015a05dd'
SOURCE_PATH = 'pictographic-primitives/symbol/eight spoke wheel_c1d7f358-4400-4823-8d56-c374015a05dd.svg'
AUTHOR = 'gpt-6'


class WheelSixSpokes(Solo48):
    icon_id = 'wheel-six-spokes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('wheel', 'spokes', 'circle', 'dharma', 'wagon', 'symbol', 'cycle', 'rim')

    def build(self) -> None:
        self.add_arc('rim-0', (24, 4), (40, 12), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('rim-1', (40, 12), (40, 36), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('rim-2', (40, 36), (24, 44), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('rim-3', (24, 44), (8, 36), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('rim-4', (8, 36), (8, 12), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('rim-5', (8, 12), (24, 4), radius_x=20, radius_y=20, sweep=True)
        self.add_contour('rim', 'rim-0', 'rim-1', 'rim-2', 'rim-3', 'rim-4', 'rim-5', closed=True)
        self.add_polyline('spoke-0', (24, 4), (24, 24), (24, 44))
        self.relate("connect", 'rim', 'spoke-0')
        self.add_polyline('spoke-1', (40, 12), (24, 24), (8, 36))
        self.relate("connect", 'rim', 'spoke-1')
        self.add_polyline('spoke-2', (40, 36), (24, 24), (8, 12))
        self.relate("connect", 'rim', 'spoke-2')
        self.relate("connect", 'spoke-0', 'spoke-1')
        self.relate("connect", 'spoke-0', 'spoke-2')
        self.relate("connect", 'spoke-1', 'spoke-2')
