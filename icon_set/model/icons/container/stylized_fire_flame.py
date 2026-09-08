"""An asymmetric flame enclosure with two pointed tongues and a rounded base.

VRECT_L: (8, 0, 56, 64); chosen for the source silhouette.
Lucide flame: curved bowl and uneven flame tongues; asymmetry preserves upward movement; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class StylizedFireFlame(Container64):
    icon_id = 'stylized-fire-flame'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('stylized', 'fire', 'flame')

    def build(self) -> None:
        self.add_arc('flame-0', (30, 2), (54, 40), radius_x=55, radius_y=55, sweep=True)
        self.add_arc('flame-1', (54, 40), (32, 62), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('flame-2', (32, 62), (10, 40), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('flame-3', (10, 40), (18, 24), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('flame-4', (18, 24), (20, 10), radius_x=35, radius_y=35, sweep=False)
        self.add_arc('flame-5', (20, 10), (28, 16), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('flame-6', (28, 16), (30, 2), radius_x=28, radius_y=28, sweep=False)
        self.add_contour('flame', 'flame-0', 'flame-1', 'flame-2', 'flame-3', 'flame-4', 'flame-5', 'flame-6', closed=True)
