"""An open circular enclosure with a captive bead at six o’clock.

CIRCLE: radius 30 about (32,32), visible radius 32. The detached bead
keeps the reference’s clear opening. Lucide crosshair informs the circular
construction; no useful local jewelry match was found. Both references
reduce to this one concept. No essential features dropped.
Batch 01 hosting measured with compose.py: none pass. plus, heart, check do not pass (including uncertified review).

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (captive-bead-ring CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: hoop rebuilt from cardinal r28 arcs (r28 has no diagonal integer points); bead r8.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class CaptiveBeadRing(Container64):
    icon_id = 'captive-bead-ring'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('captive-bead-piercing-ring', 'captive-bead-ring-piercing')
    keywords = ('captive', 'bead', 'ring')

    def build(self) -> None:
        self.add_arc('hoop-left', (15, 54), (4, 32), radius_x=28)
        self.add_arc('hoop-top', (4, 32), (60, 32), radius_x=28)
        self.add_arc('hoop-right', (60, 32), (49, 54), radius_x=28)
        self.add_contour('hoop', 'hoop-left', 'hoop-top', 'hoop-right')
        self.add_arc('bead-top', (24, 52), (40, 52), radius_x=8)
        self.add_arc('bead-bottom', (40, 52), (24, 52), radius_x=8)
        self.add_contour('bead', 'bead-top', 'bead-bottom', closed=True)
