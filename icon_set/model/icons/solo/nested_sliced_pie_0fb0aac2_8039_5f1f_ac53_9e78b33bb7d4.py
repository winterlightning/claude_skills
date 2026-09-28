"""Nested sliced pie (business), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fb0aac2-8039-5f1f-ac53-9e78b33bb7d4'
SOURCE_PATH = 'pictographic-primitives/business/nested sliced pie_0fb0aac2-8039-5f1f-ac53-9e78b33bb7d4.svg'
AUTHOR = 'gpt-6'

class NestedSlicedPie(Solo48):
    icon_id = 'nested-sliced-pie'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('nested', 'sliced', 'pie', 'business')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 32), (24, 44))
        self.add_line('e1', (17, 28), (8, 36))
        self.add_line('e2', (16, 24), (4, 24))
        self.add_line('e3', (17, 20), (9, 11))
        self.add_line('e4', (39, 11), (31, 20))
        self.add_line('e5', (24, 4), (24, 16))
        self.add_arc('e6-top', (16, 24), (32, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('e6-bottom', (32, 24), (16, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('e7-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e7-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3',), closed=False)
        self.add_contour('c4', *('e4',), closed=False)
        self.add_contour('c5', *('e5',), closed=False)
        self.add_contour('e7', *('e7-top', 'e7-bottom'), closed=True)
        self.add_contour('e6', *('e6-top', 'e6-bottom'), closed=True)
        self.relate('connect', *('c0', 'e6'))
        self.relate('connect', *('c0', 'e7'))
        self.relate('connect', *('c1', 'e6'))
        self.relate('connect', *('c1', 'e7'))
        self.relate('connect', *('c2', 'e6'))
        self.relate('connect', *('c2', 'e7'))
        self.relate('connect', *('c3', 'e6'))
        self.relate('connect', *('c3', 'e7'))
        self.relate('connect', *('c4', 'e7'))
        self.relate('connect', *('c4', 'e6'))
        self.relate('connect', *('c5', 'e7'))
        self.relate('connect', *('c5', 'e6'))
