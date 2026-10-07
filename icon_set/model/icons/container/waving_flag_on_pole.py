"""A gently waving banner with a notched fly on a tall pole.

Keyshape VRECT_XL, bounds (4, 0, 60, 64): chosen for the reference proportions.
Lucide construction: flag: continuous waving edges with a joined pole; directional asymmetry retained. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus blocked, heart blocked, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (waving-flag-on-pole VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
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
        # Taller banner (7..49, was 10..46) with gentler waves and a shallower fly-end notch, so the banner holds a
        # symbol of 26 with a 4 px gap (was 19).
        self.add_line('pole', (10, 4), (10, 60))
        self.add_arc('banner-0', (10, 7), (32, 7), radius_x=30, sweep=False)
        self.add_arc('banner-1', (32, 7), (54, 7), radius_x=26)
        self.add_line('banner-2', (54, 7), (51, 28))
        self.add_line('banner-3', (51, 28), (54, 49))
        self.add_arc('banner-4', (54, 49), (32, 49), radius_x=30, sweep=False)
        self.add_arc('banner-5', (32, 49), (10, 49), radius_x=26)
        self.add_contour('banner', 'banner-0', 'banner-1', 'banner-2', 'banner-3', 'banner-4', 'banner-5')
        self.relate('connect', 'pole', 'banner')
