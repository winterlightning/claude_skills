"""Exponential (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1195ed25-2865-5967-8377-ba7934eebadd'
SOURCE_PATH = 'icons-json/interface-essential/exponential_1195ed25-2865-5967-8377-ba7934eebadd.json'
AUTHOR = 'gpt-6'

class Exponential(Solo48):
    icon_id = 'exponential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('exponential', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (40, 13), (31, 21))
        self.add_line('e1', (31, 21), (42, 21))
        self.add_line('e2', (6, 21), (24, 42))
        self.add_line('e3', (7, 41), (23, 22))
        self.add_line('e4-1', (32, 9), (34, 7))
        self.add_line('e4-2', (34, 7), (38, 6))
        self.add_arc('e4-3', (38, 6), (42, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e4-4', (42, 10), (40, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('c0', *('e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0', 'e1'), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
