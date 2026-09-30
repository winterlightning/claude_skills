"""A gently waving banner with a notched fly on a tall pole.

Keyshape VRECT_XL, bounds (4, 0, 60, 64): chosen for the reference proportions.
Lucide construction: flag: continuous waving edges with a joined pole; directional asymmetry retained. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus blocked, heart blocked, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (waving-flag-on-pole VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class WavingFlagOnPole(Container64):
    icon_id = 'waving-flag-on-pole'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('waving', 'flag', 'on', 'pole')

    def build(self) -> None:
        self.add_line('pole', (10, 4), (10, 60))
        self.add_arc('banner-0', (10, 10), (32, 10), radius_x=25, sweep=False)
        self.add_arc('banner-1', (32, 10), (54, 10), radius_x=22)
        self.add_line('banner-2', (54, 10), (48, 29))
        self.add_line('banner-3', (48, 29), (54, 46))
        self.add_arc('banner-4', (54, 46), (32, 46), radius_x=25, sweep=False)
        self.add_arc('banner-5', (32, 46), (10, 46), radius_x=22)
        self.add_contour('banner', 'banner-0', 'banner-1', 'banner-2', 'banner-3', 'banner-4', 'banner-5')
        self.relate('connect', 'pole', 'banner')
