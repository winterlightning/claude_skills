"""Suspended basket and scalloped canopy; two broad scallops replace three, cords are vertical for clear space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cac28c98-7a13-413c-8246-fe935c1db139'
SOURCE_PATH = 'pictographic-primitives/babies/rocking crib basket swing bed_cac28c98-7a13-413c-8246-fe935c1db139.svg'
AUTHOR = 'gpt-6'


class HangingBassinet(Solo48):
    icon_id = 'hanging-bassinet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "babies"
    categories = ("babies", "primitives")
    aliases = ()
    keywords = ('hanging', 'bassinet', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Centerline keyshape: VRECT_L; Suspended basket and scalloped canopy; two broad scallops replace three, cords are vertical for clear space.
        self.add_line('roof', (13, 4), (35, 4))
        self.add_arc('roof-right', (35, 4), (40, 10), radius_x=5, radius_y=6, sweep=True)
        self.add_arc('scallop-right', (40, 10), (24, 10), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('scallop-left', (24, 10), (8, 10), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('roof-left', (8, 10), (13, 4), radius_x=5, radius_y=6, sweep=True)
        self.add_contour('canopy', 'roof', 'roof-right', 'scallop-right', 'scallop-left', 'roof-left', closed=True)
        self.add_polyline('cord-left', (8, 10), (8, 28), (8, 44), closed=False)
        self.add_polyline('cord-right', (40, 10), (40, 28), (40, 44), closed=False)
        self.add_polyline('rim', (8, 28), (10, 28), (38, 28), (40, 28), closed=False)
        self.add_arc('basket-left', (8, 28), (24, 44), radius_x=16, radius_y=16, sweep=False)
        self.add_arc('basket-right', (24, 44), (40, 28), radius_x=16, radius_y=16, sweep=False)
        self.add_contour('basket', 'basket-left', 'basket-right', closed=False)
        self.relate("connect", 'rim', 'basket')
        self.relate("connect", 'cord-left', 'canopy')
        self.relate("connect", 'cord-left', 'rim')
        self.relate("connect", 'cord-left', 'basket')
        self.relate("connect", 'cord-right', 'canopy')
        self.relate("connect", 'cord-right', 'rim')
        self.relate("connect", 'cord-right', 'basket')
