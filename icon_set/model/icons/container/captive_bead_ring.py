"""An open circular enclosure with a captive bead at six o’clock.

CIRCLE: radius 30 about (32,32), visible radius 32. The detached bead
keeps the reference’s clear opening. Lucide crosshair informs the circular
construction; no useful local jewelry match was found. Both references
reduce to this one concept. No essential features dropped.
Batch 01 hosting measured with compose.py: none pass. plus, heart, check do not pass (including uncertified review).
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class CaptiveBeadRing(Container64):
    icon_id = 'captive-bead-ring'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('captive-bead-piercing-ring', 'captive-bead-ring-piercing')
    keywords = ('captive', 'bead', 'ring')

    def build(self) -> None:
        self.add_arc("hoop", (14, 56), (50, 56), radius_x=30, large_arc=True)
        self.add_arc("bead-top", (23, 53), (41, 53), radius_x=9)
        self.add_arc("bead-bottom", (41, 53), (23, 53), radius_x=9)
        self.add_contour("bead", "bead-top", "bead-bottom", closed=True)
