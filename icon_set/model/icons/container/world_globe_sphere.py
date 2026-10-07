"""A globe with polar meridians and an open central latitude band.

Keyshape CIRCLE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: globe: radial outer circle and mirrored meridians; reference central band stays open. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus blocked, heart blocked, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (world-globe-sphere CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class WorldGlobeSphere(Container64):
    icon_id = 'world-globe-sphere'
    keyshape = Keyshape.CIRCLE
    aliases = ()
    keywords = ('world', 'globe', 'sphere')

    def build(self) -> None:
        # Latitude lines moved toward the poles (13 and 51, were 16 and 48) with the meridian caps above and below
        # them, so the open band holds a symbol of 26 with a 4 px gap (was 20).
        self.add_arc('sphere-0', (32, 4), (60, 32), radius_x=28)
        self.add_arc('sphere-1', (60, 32), (32, 60), radius_x=28)
        self.add_arc('sphere-2', (32, 60), (4, 32), radius_x=28)
        self.add_arc('sphere-3', (4, 32), (32, 4), radius_x=28)
        self.add_line('north-latitude', (12, 13), (52, 13))
        self.add_arc('north-west', (32, 4), (24, 13), radius_x=39)
        self.add_arc('north-east', (32, 4), (40, 13), radius_x=39, sweep=False)
        self.add_line('south-latitude', (12, 51), (52, 51))
        self.add_arc('south-west', (32, 60), (24, 51), radius_x=39, sweep=False)
        self.add_arc('south-east', (32, 60), (40, 51), radius_x=39)
        self.add_contour('sphere', 'sphere-0', 'sphere-1', 'sphere-2', 'sphere-3', closed=True)
        self.relate('connect', 'sphere', 'north-latitude')
        self.relate('connect', 'sphere', 'north-west')
        self.relate('connect', 'north-latitude', 'north-west')
        self.relate('connect', 'sphere', 'north-east')
        self.relate('connect', 'north-latitude', 'north-east')
        self.relate('connect', 'north-west', 'north-east')
        self.relate('connect', 'sphere', 'south-latitude')
        self.relate('connect', 'sphere', 'south-west')
        self.relate('connect', 'south-latitude', 'south-west')
        self.relate('connect', 'sphere', 'south-east')
        self.relate('connect', 'south-latitude', 'south-east')
        self.relate('connect', 'south-west', 'south-east')
