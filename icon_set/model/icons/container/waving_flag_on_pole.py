"""A gently waving banner with a notched fly on a tall pole.

Keyshape VRECT_XL, bounds (4, 0, 60, 64): chosen for the reference proportions.
Lucide construction: flag: continuous waving edges with a joined pole; directional asymmetry retained. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus blocked, heart blocked, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class WavingFlagOnPole(Container64):
    icon_id = 'waving-flag-on-pole'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('waving', 'flag', 'on', 'pole')

    def build(self) -> None:
        self.add_line('pole', (6, 2), (6, 62))
        self.add_arc('banner-0', (6, 8), (32, 8), radius_x=34, radius_y=34, sweep=False)
        self.add_arc('banner-1', (32, 8), (58, 8), radius_x=34, radius_y=34, sweep=True)
        self.add_line('banner-2', (58, 8), (52, 28))
        self.add_line('banner-3', (52, 28), (58, 48))
        self.add_arc('banner-4', (58, 48), (32, 48), radius_x=34, radius_y=34, sweep=False)
        self.add_arc('banner-5', (32, 48), (6, 48), radius_x=34, radius_y=34, sweep=True)
        self.add_contour('banner', 'banner-0', 'banner-1', 'banner-2', 'banner-3', 'banner-4', 'banner-5', closed=False)
        self.relate("connect", 'pole', 'banner')
