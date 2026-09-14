"""Dial with Single Hand. Keeps the short pivot tick and single diagonal hand.

CIRCLE visible extremes (2, 2, 46, 46); centerlines (4, 4, 44, 44).
Lucide clock, inspected in batch 06: circular dial with a simple joined hand.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '598944a9-8659-4310-9c2d-94ae3b706b3c'
SOURCE_PATH = 'pictographic-primitives/symbol/disc_598944a9-8659-4310-9c2d-94ae3b706b3c.svg'
AUTHOR = 'gpt-6'


class DialSingleHand(Solo48):
    icon_id = 'dial-single-hand'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('dial', 'gauge', 'disc', 'meter', 'timer', 'speed', 'clock', 'indicator')

    def build(self) -> None:
        self.add_arc('dial-right', (24, 4), (24, 44), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('dial-left', (24, 44), (24, 4), radius_x=20, radius_y=20, sweep=True)
        self.add_contour('dial', 'dial-right', 'dial-left', closed=True)
        self.add_polyline('hand', (22, 23), (24, 25), (32, 17))
