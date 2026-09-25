"""Exponential (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0e23fae-9562-52b1-9db1-9c5e4e85aed2'
SOURCE_PATH = 'pictographic-primitives/interface-essential/exponential_f0e23fae-9562-52b1-9db1-9c5e4e85aed2.svg'
AUTHOR = 'gpt-6'

class ExponentialInterfaceEssential(Solo48):
    icon_id = 'exponential-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('exponential', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (43, 9), (35, 17))
        self.add_line('e1', (35, 8), (44, 18))
        self.add_line('e2', (4, 25), (9, 21))
        self.add_line('e3', (9, 21), (9, 40))
        self.add_line('e4', (4, 40), (13, 40))
        self.add_line('e5', (29, 31), (29, 26))
        self.add_arc('e6-1', (29, 26), (21, 22), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('e6-2', (21, 22), (18, 31), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('e6-3', (18, 31), (24, 37), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('e6-4', (24, 37), (29, 31), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2', 'e3'), closed=False)
        self.add_contour('c3', *('e4',), closed=False)
        self.add_contour('c4', *('e5', 'e6-1', 'e6-2', 'e6-3', 'e6-4'), closed=True)
        self.relate('connect', *('c2', 'c3'))
