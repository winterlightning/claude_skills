"""Symmetric bowl cradle on a shallow rocker; Lucide rocking-chair informs the open rocker. Two feet reduced to a central support."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f95a7c1-39ba-51c6-8b4f-e4358cd82d8e'
SOURCE_PATH = 'pictographic-primitives/babies/rocking babies bed_5f95a7c1-39ba-51c6-8b4f-e4358cd82d8e.svg'
AUTHOR = 'gpt-6'


class RockingCradle(Solo48):
    icon_id = 'rocking-cradle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby"
    aliases = ()
    keywords = ('rocking', 'cradle', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Centerline keyshape: HRECT_L; Symmetric bowl cradle on a shallow rocker; Lucide rocking-chair informs the open rocker. Two feet reduced to a central support.
        self.add_polyline('rim', (5, 8), (5, 15), (43, 15), (43, 8), closed=False)
        self.add_arc('bowl-left', (5, 15), (24, 33), radius_x=19, radius_y=18, sweep=False)
        self.add_arc('bowl-right', (24, 33), (43, 15), radius_x=19, radius_y=18, sweep=False)
        self.add_contour('bowl', 'bowl-left', 'bowl-right', closed=False)
        self.relate("connect", 'rim', 'bowl')
        self.add_line('stand', (24, 33), (24, 40))
        self.add_arc('rocker-left', (2, 32), (24, 40), radius_x=30, radius_y=12, sweep=False)
        self.add_arc('rocker-right', (24, 40), (46, 32), radius_x=30, radius_y=12, sweep=False)
        self.add_contour('rocker', 'rocker-left', 'rocker-right', closed=False)
        self.relate("connect", 'stand', 'bowl')
        self.relate("connect", 'stand', 'rocker')
