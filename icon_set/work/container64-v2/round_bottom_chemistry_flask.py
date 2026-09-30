"""Widen the round bulb and shorten the neck while retaining the flask silhouette.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (round-bottom-chemistry-flask VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class RoundBottomChemistryFlask(Container64):
    icon_id = 'round-bottom-chemistry-flask'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('vessel-0', (26, 4), (26, 13))
        self.add_arc('vessel-1', (26, 13), (10, 36), radius_x=16, radius_y=23, sweep=False)
        self.add_arc('vessel-2', (10, 36), (54, 36), radius_x=22, radius_y=24, sweep=False)
        self.add_arc('vessel-3', (54, 36), (38, 13), radius_x=16, radius_y=23, sweep=False)
        self.add_line('vessel-4', (38, 13), (38, 4))
        self.add_line('rim', (22, 4), (42, 4))
        self.add_contour('vessel', 'vessel-0', 'vessel-1', 'vessel-2', 'vessel-3', 'vessel-4')
        self.relate('connect', 'rim', 'vessel')
