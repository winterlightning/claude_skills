"""A globe with polar meridians and an open central latitude band.

Keyshape CIRCLE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: globe: radial outer circle and mirrored meridians; reference central band stays open. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus blocked, heart blocked, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class WorldGlobeSphere(Container64):
    icon_id = 'world-globe-sphere'
    keyshape = Keyshape.CIRCLE
    aliases = ()
    keywords = ('world', 'globe', 'sphere')

    def build(self) -> None:
        self.add_arc('sphere-0', (32, 2), (62, 32), radius_x=30, radius_y=30, sweep=True)
        self.add_arc('sphere-1', (62, 32), (32, 62), radius_x=30, radius_y=30, sweep=True)
        self.add_arc('sphere-2', (32, 62), (2, 32), radius_x=30, radius_y=30, sweep=True)
        self.add_arc('sphere-3', (2, 32), (32, 2), radius_x=30, radius_y=30, sweep=True)
        self.add_contour('sphere', 'sphere-0', 'sphere-1', 'sphere-2', 'sphere-3', closed=True)
        self.add_line('north-latitude', (8, 14), (56, 14))
        self.relate("connect", 'sphere', 'north-latitude')
        self.add_arc('north-west', (32, 2), (20, 14), radius_x=40, radius_y=40, sweep=True)
        self.relate("connect", 'sphere', 'north-west')
        self.relate("connect", 'north-latitude', 'north-west')
        self.add_arc('north-east', (32, 2), (44, 14), radius_x=40, radius_y=40, sweep=False)
        self.relate("connect", 'sphere', 'north-east')
        self.relate("connect", 'north-latitude', 'north-east')
        self.relate("connect", 'north-west', 'north-east')
        self.add_line('south-latitude', (8, 50), (56, 50))
        self.relate("connect", 'sphere', 'south-latitude')
        self.add_arc('south-west', (32, 62), (20, 50), radius_x=40, radius_y=40, sweep=False)
        self.relate("connect", 'sphere', 'south-west')
        self.relate("connect", 'south-latitude', 'south-west')
        self.add_arc('south-east', (32, 62), (44, 50), radius_x=40, radius_y=40, sweep=True)
        self.relate("connect", 'sphere', 'south-east')
        self.relate("connect", 'south-latitude', 'south-east')
        self.relate("connect", 'south-west', 'south-east')
