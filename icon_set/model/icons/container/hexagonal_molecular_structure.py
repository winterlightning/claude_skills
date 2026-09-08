"""A hexagonal molecular enclosure with ring nodes at three alternating vertices.

VRECT_XL: visible bounds (4, 0, 60, 64); chosen for the source proportions.
Construction reference: Lucide hexagon: paired vertical sides and mirrored diagonal bonds. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class HexagonalMolecularStructure(Container64):
    icon_id = 'hexagonal-molecular-structure'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('hexagonal', 'molecular', 'structure')

    def build(self) -> None:
        self.add_arc('top-0', (28, 6), (32, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('top-1', (32, 2), (36, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('top-2', (36, 6), (32, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('top-3', (32, 10), (28, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('top', 'top-0', 'top-1', 'top-2', 'top-3', closed=True)
        self.add_arc('left-0', (6, 46), (10, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('left-1', (10, 42), (14, 46), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('left-2', (14, 46), (10, 50), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('left-3', (10, 50), (6, 46), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('left', 'left-0', 'left-1', 'left-2', 'left-3', closed=True)
        self.add_arc('right-0', (50, 46), (54, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('right-1', (54, 42), (58, 46), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('right-2', (58, 46), (54, 50), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('right-3', (54, 50), (50, 46), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('right', 'right-0', 'right-1', 'right-2', 'right-3', closed=True)
        self.add_polyline('upper-left',(28,6),(10,20),(10,42))
        self.add_polyline('upper-right',(36,6),(54,20),(54,42))
        self.add_polyline('bottom',(10,50),(32,62),(54,50))
        self.relate("connect",'top','upper-left')
        self.relate("connect",'top','upper-right')
        self.relate("connect",'left','upper-left')
        self.relate("connect",'left','bottom')
        self.relate("connect",'right','upper-right')
        self.relate("connect",'right','bottom')
