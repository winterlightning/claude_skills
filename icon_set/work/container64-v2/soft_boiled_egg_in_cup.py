"""Widen the egg crown and lower the cup rim while retaining an egg-shaped top.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (soft-boiled-egg-in-cup VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class SoftBoiledEggInCup(Container64):
    icon_id = 'soft-boiled-egg-in-cup'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_arc('egg-crown', (10, 49), (54, 49), radius_x=22, radius_y=45)
        self.add_line('cup-rim', (10, 49), (54, 49))
        self.add_arc('cup-bowl', (54, 49), (10, 49), radius_x=22, radius_y=11)
        self.relate('connect', 'egg-crown', 'cup-rim')
        self.relate('connect', 'cup-bowl', 'cup-rim')
