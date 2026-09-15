"""Lesbian lgbt symbol (romance), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '180dee8c-f605-55c4-bd03-4306640eb7bc'
SOURCE_PATH = 'pictographic-primitives/romance/lesbian lgbt symbol_180dee8c-f605-55c4-bd03-4306640eb7bc.svg'
AUTHOR = 'gpt-6'

class LesbianLgbtSymbol(Solo48):
    icon_id = 'lesbian-lgbt-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('lesbian', 'lgbt', 'symbol', 'romance')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (16, 42), (16, 28))
        self.add_line('e1', (10, 36), (19, 36))
        self.add_line('e2', (32, 28), (32, 42))
        self.add_line('e3', (27, 36), (36, 36))
        self.add_line('e4', (18, 19), (23, 25))
        self.add_line('e5', (25, 25), (30, 19))
        self.add_arc('e6-1', (23, 25), (15, 28), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e6-2', (15, 28), (6, 17), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('e6-3', (6, 17), (7, 12))
        self.add_arc('e6-4', (7, 12), (12, 7), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('e6-5', (12, 7), (16, 6), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e6-6', (16, 6), (20, 7), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e7-1', (28, 7), (32, 6), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e7-2', (32, 6), (36, 7), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e7-3', (36, 7), (42, 17), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('e7-4', (42, 17), (33, 28), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('e7-5', (33, 28), (25, 25), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('e8', (23, 25), (25, 25))
        self.add_arc('e9-1', (30, 19), (30, 13), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('e9-2', (30, 13), (24, 14), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('e9-3', (24, 14), (20, 12), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('e9-4', (20, 12), (18, 19), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6'), closed=False)
        self.add_contour('c3', *('e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5'), closed=False)
        self.add_contour('c4', *('e2',), closed=False)
        self.add_contour('c5', *('e3',), closed=False)
        self.add_contour('c6', *('e4', 'e8', 'e5', 'e9-1', 'e9-2', 'e9-3', 'e9-4'), closed=True)
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c4', 'c3'))
        self.relate('connect', *('c2', 'c6'))
        self.relate('connect', *('c3', 'c6'))
