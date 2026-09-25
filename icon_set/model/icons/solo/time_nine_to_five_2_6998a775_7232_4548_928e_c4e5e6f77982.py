"""Time nine to five 2 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6998a775-7232-4548-928e-c4e5e6f77982'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time nine to five 2_6998a775-7232-4548-928e-c4e5e6f77982.svg'
AUTHOR = 'gpt-6'

class TimeNineToFive2(Solo48):
    icon_id = 'time-nine-to-five-2'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('time', 'nine', 'to', 'five', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (13, 23), (24, 23))
        self.add_line('e1', (25, 24), (31, 33))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_line('e3', (24, 23), (25, 24))
        self.add_contour('c0', *('e0', 'e3', 'e1'), closed=False)
        self.add_contour('e2', *('e2-top', 'e2-bottom'), closed=True)
