"""Suspended basket and scalloped canopy; two broad scallops replace three, cords are vertical for clear space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cac28c98-7a13-413c-8246-fe935c1db139'
SOURCE_PATH = 'pictographic-primitives/babies/rocking crib basket swing bed_cac28c98-7a13-413c-8246-fe935c1db139.svg'
AUTHOR = 'gpt-6'


class HangingBassinet(Solo48):
    icon_id = 'hanging-bassinet'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby"
    aliases = ()
    keywords = ('hanging', 'bassinet', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Centerline keyshape: VRECT_XL; Suspended basket and scalloped canopy; two broad scallops replace three, cords are vertical for clear space.
        self.add_line('roof', (13, 2), (35, 2))
        self.add_arc('roof-right', (35, 2), (43, 10), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('scallop-right', (43, 10), (24, 10), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('scallop-left', (24, 10), (5, 10), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('roof-left', (5, 10), (13, 2), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('canopy', 'roof', 'roof-right', 'scallop-right', 'scallop-left', 'roof-left', closed=True)
        self.add_polyline('cord-left', (5, 10), (5, 28), (5, 46), closed=False)
        self.add_polyline('cord-right', (43, 10), (43, 28), (43, 46), closed=False)
        self.add_polyline('rim', (5, 28), (10, 28), (38, 28), (43, 28), closed=False)
        self.add_arc('basket-left', (5, 28), (24, 43), radius_x=19, radius_y=15, sweep=False)
        self.add_arc('basket-right', (24, 43), (43, 28), radius_x=19, radius_y=15, sweep=False)
        self.add_contour('basket', 'basket-left', 'basket-right', closed=False)
        self.relate("connect", 'rim', 'basket')
        self.relate("connect", 'cord-left', 'canopy')
        self.relate("connect", 'cord-left', 'rim')
        self.relate("connect", 'cord-left', 'basket')
        self.relate("connect", 'cord-right', 'canopy')
        self.relate("connect", 'cord-right', 'rim')
        self.relate("connect", 'cord-right', 'basket')
