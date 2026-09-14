"""A hand truck carrying a box. VRECT_L extremes (8,6)-(40,42). Lucide truck informs a round wheel attached at explicit silhouette endpoints; no exact hand-truck match. Narrow the cargo to retain clearance from the wheel and upright."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23e62360-beb2-4bfa-84c6-4545003b32a4'
SOURCE_PATH = 'pictographic-primitives/symbol/logistic_23e62360-beb2-4bfa-84c6-4545003b32a4.svg'
AUTHOR = 'gpt-6'


class HandTruckBox(Solo48):
    icon_id = 'hand-truck-box'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('hand-truck', 'dolly', 'logistics', 'delivery', 'box', 'moving', 'cargo', 'warehouse')

    def build(self) -> None:
        pts=[(14,32),(20,38),(14,42),(8,38)]
        for i,p in enumerate(pts):
            self.add_arc(f'wheel-{i}',p,pts[(i+1)%4],radius_x=6)
        self.add_contour('wheel',*(f'wheel-{i}' for i in range(4)),closed=True)
        self.add_line('grip',(8,6),(10,6))
        self.add_arc('handle-turn',(10,6),(14,8),radius_x=4)
        self.add_line('upright',(14,8),(14,32))
        self.add_contour('handle','grip','handle-turn','upright')
        self.relate('connect','wheel','handle')
        self.add_polyline('box',(29,38),(29,16),(40,16),(40,38),(29,38),closed=True)
        self.add_line('platform',(20,38),(29,38))
        self.relate('connect','wheel','platform')
        self.relate('connect','box','platform')
