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
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('wheel-0',(14, 32),*(((17.3137085, 32.0), (20.0, 34.85786438), (20, 39)),))
        self.add_bezier('wheel-1',(20, 39),*(((19.11368359, 42.15064767), (16.66752306, 44), (14, 44)),))
        self.add_bezier('wheel-2',(14, 44),*(((11.33247694, 44), (8.88631641, 42.15064767), (8, 39)),))
        self.add_bezier('wheel-3',(8, 39),*(((8, 34.85786438), (10.6862915, 32.0), (14, 32)),))
        self.add_line('grip',(8, 4),(10, 4))
        self.add_bezier('handle-turn',(10, 4),*(((11.6162858, 4), (13.19868669, 4.72578466), (14, 6)),))
        self.add_line('upright',(14, 6),(14, 32))
        self.add_line('box-1',(29, 39),(29, 16))
        self.add_line('box-2',(29, 16),(40, 16))
        self.add_line('box-3',(40, 16),(40, 39))
        self.add_line('box-4',(40, 39),(29, 39))
        self.add_line('box-5',(29, 39),(29, 39))
        self.add_line('platform',(20, 39),(29, 39))
        self.add_contour('wheel',*('wheel-0', 'wheel-1', 'wheel-2', 'wheel-3'),closed=True)
        self.add_contour('handle',*('grip', 'handle-turn', 'upright'),closed=False)
        self.add_contour('box',*('box-1', 'box-2', 'box-3', 'box-4', 'box-5'),closed=True)
        self.relate('connect',*('wheel', 'handle'))
        self.relate('connect',*('wheel', 'platform'))
        self.relate('connect',*('box', 'platform'))
