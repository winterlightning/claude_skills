"""Left-facing broadcast van carrying a roof-mounted dish. Lucide truck informs attached wheel/body boundaries; satellite-dish informs the dish chord and receiver. Windows omitted to preserve the dish and wheels.

SOLO48 SQUARE, live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '493ede0a-6fdc-424e-ac62-2775797bcb36'
SOURCE_PATH = 'pictographic-primitives/symbol/radio van_493ede0a-6fdc-424e-ac62-2775797bcb36.svg'
AUTHOR = 'gpt-6'


class BroadcastVanDish(Solo48):
    icon_id = 'broadcast-van-dish'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('broadcast', 'van', 'satellite', 'dish', 'news', 'media', 'vehicle', 'outside-broadcast')

    def build(self) -> None:

        self.add_polyline('body',(8,38),(6,38),(6,33),(10,27),(24,27),(42,27),(42,38),(40,38))
        self.add_line('chassis',(16,38),(32,38))
        for side,cx in [('front',12),('rear',36)]:
            self.add_arc(side+'-wheel-top',(cx-4,38),(cx+4,38),radius_x=4)
            self.add_arc(side+'-wheel-bottom',(cx+4,38),(cx-4,38),radius_x=4)
            self.add_contour(side+'-wheel',side+'-wheel-top',side+'-wheel-bottom',closed=True)
            self.relate('connect',side+'-wheel','body')
            self.relate('connect',side+'-wheel','chassis')
        self.add_arc('dish-bowl-left',(14,8),(24,18),radius_x=10,sweep=False)
        self.add_arc('dish-bowl-right',(24,18),(32,14),radius_x=10,sweep=False)
        self.add_line('dish-rim-low',(32,14),(23,11))
        self.add_line('dish-rim-high',(23,11),(14,8))
        self.add_contour('dish','dish-bowl-left','dish-bowl-right','dish-rim-low','dish-rim-high',closed=True)
        self.add_line('receiver',(23,11),(29,6))
        self.add_line('mast',(24,18),(24,27))
        self.relate('connect','dish','receiver')
        self.relate('connect','dish','mast')
        self.relate('connect','mast','body')
