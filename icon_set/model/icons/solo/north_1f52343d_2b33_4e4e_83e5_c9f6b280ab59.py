"""North (weather), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f52343d-2b33-4e4e-83e5-c9f6b280ab59'
SOURCE_PATH = 'pictographic-primitives/weather/north_1f52343d-2b33-4e4e-83e5-c9f6b280ab59.svg'
AUTHOR = 'gpt-6'

class North(Solo48):
    icon_id = 'north'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('north', 'weather')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 7), (24, 4))
        self.add_line('e1', (41, 24), (44, 24))
        self.add_line('e2', (24, 41), (24, 44))
        self.add_line('e3', (7, 24), (4, 24))
        self.add_line('e4', (24, 15), (31, 33))
        self.add_line('e5', (31, 33), (24, 30))
        self.add_line('e6', (24, 30), (17, 33))
        self.add_line('e7', (17, 33), (24, 15))
        self.add_arc('e8-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e8-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3',), closed=False)
        self.add_contour('c4', *('e4', 'e5', 'e6', 'e7'), closed=True)
        self.add_contour('e8', *('e8-top', 'e8-bottom'), closed=True)
        self.relate('connect', *('c0', 'e8'))
        self.relate('connect', *('c1', 'e8'))
        self.relate('connect', *('c2', 'e8'))
        self.relate('connect', *('c3', 'e8'))
