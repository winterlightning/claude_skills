"""Restaurant fork knife (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24a6b06c-3fec-43a0-aca0-b205c99c496b'
SOURCE_PATH = 'pictographic-primitives/food/restaurant fork knife_24a6b06c-3fec-43a0-aca0-b205c99c496b.svg'
AUTHOR = 'gpt-6'

class RestaurantForkKnife(Solo48):
    icon_id = 'restaurant-fork-knife'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('restaurant', 'fork', 'knife', 'food')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (16, 4), (15, 19))
        self.add_line('e1', (8, 4), (8, 12))
        self.add_line('e2', (16, 44), (15, 19))
        self.add_line('e3', (23, 4), (23, 12))
        self.add_line('e4', (32, 44), (32, 28))
        self.add_line('e5', (32, 4), (32, 28))
        self.add_line('e6', (32, 28), (39, 28))
        self.add_line('e7', (40, 22), (39, 15))
        self.add_arc('e8', (8, 12), (15, 19), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('e9', (23, 12), (15, 19), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('e10-1', (39, 28), (40, 24))
        self.add_arc('e10-2', (40, 24), (40, 22), radius_x=26, radius_y=26, large_arc=False, sweep=True)
        self.add_arc('e11', (39, 15), (32, 4), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1', 'e8'), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3', 'e9'), closed=False)
        self.add_contour('c4', *('e4',), closed=False)
        self.add_contour('c5', *('e5', 'e6', 'e10-1', 'e10-2', 'e7', 'e11'), closed=True)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c0', 'c3'))
        self.relate('connect', *('c1', 'c2'))
        self.relate('connect', *('c1', 'c3'))
        self.relate('connect', *('c2', 'c3'))
        self.relate('connect', *('c4', 'c5'))
