"""A circular lens with a diagonal handle extending to the lower right.

SQUARE: (0, 0, 64, 64); chosen for the source silhouette.
Lucide search: circular lens and radial handle; intentional directional asymmetry; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SearchMagnifyingGlass(Container64):
    icon_id = 'search-magnifying-glass'
    keyshape = Keyshape.SQUARE
    aliases = ('search-magnifying-glass-icon', 'magnifier')
    keywords = ('search', 'magnifying', 'glass')

    def build(self) -> None:
        self.add_arc('lens-0', (42, 47), (2, 27), radius_x=25, radius_y=25, sweep=True)
        self.add_arc('lens-1', (2, 27), (52, 27), radius_x=25, radius_y=25, sweep=True)
        self.add_arc('lens-2', (52, 27), (42, 47), radius_x=25, radius_y=25, sweep=True)
        self.add_contour('lens', 'lens-0', 'lens-1', 'lens-2', closed=True)
        self.add_line('handle-0', (42, 47), (62, 62))
        self.add_contour('handle', 'handle-0', closed=False)
        self.relate("connect", "lens", "handle")
