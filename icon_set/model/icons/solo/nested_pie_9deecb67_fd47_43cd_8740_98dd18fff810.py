"""Nested pie (business), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9deecb67-fd47-43cd-8740-98dd18fff810'
SOURCE_PATH = 'pictographic-primitives/business/nested pie_9deecb67-fd47-43cd-8740-98dd18fff810.svg'
AUTHOR = 'gpt-6'

class NestedPie(Solo48):
    icon_id = 'nested-pie'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('nested', 'pie', 'business')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 22), (24, 9))
        self.add_line('e1', (4, 24), (12, 24))
        self.add_line('e2', (24, 36), (24, 44))
        self.add_line('e3', (24, 9), (24, 4))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e5-top', (12, 24), (36, 24), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('e5-bottom', (36, 24), (12, 24), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('e6', (17, 30), (24, 22), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_contour('c0', *('e6', 'e0'), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3',), closed=False)
        self.add_contour('e4', *('e4-top', 'e4-bottom'), closed=True)
        self.add_contour('e5', *('e5-top', 'e5-bottom'), closed=True)
        self.relate('connect', *('c0', 'c3'))
        self.relate('connect', *('c0', 'e5'))
        self.relate('connect', *('c3', 'e5'))
        self.relate('connect', *('c1', 'e4'))
        self.relate('connect', *('c1', 'e5'))
        self.relate('connect', *('c2', 'e5'))
        self.relate('connect', *('c2', 'e4'))
        self.relate('connect', *('c3', 'e4'))
