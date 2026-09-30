"""Narrow the folded side panels while retaining the curved panoramic outline.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (panoramic-360-degree-virtual-reality-view HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class Panoramic360DegreeVirtualRealityView(Container64):
    icon_id = 'panoramic-360-degree-virtual-reality-view'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_arc('outline-0', (4, 20), (60, 20), radius_x=28, radius_y=10)
        self.add_line('outline-1', (60, 20), (60, 44))
        self.add_arc('outline-2', (60, 44), (4, 44), radius_x=28, radius_y=10)
        self.add_line('outline-3', (4, 44), (4, 20))
        self.add_line('panel-left-1', (4, 20), (12, 24))
        self.add_line('panel-left-2', (12, 24), (12, 51))
        self.add_line('panel-right-1', (60, 20), (52, 24))
        self.add_line('panel-right-2', (52, 24), (52, 51))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', closed=True)
        self.add_contour('panel-left', 'panel-left-1', 'panel-left-2')
        self.add_contour('panel-right', 'panel-right-1', 'panel-right-2')
        self.relate('connect', 'panel-left', 'outline')
        self.relate('connect', 'panel-right', 'outline')
