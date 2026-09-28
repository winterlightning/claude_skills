"""Time clock three to six (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09eace6e-ae79-411b-bc2d-e851b1530181'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time clock three to six_09eace6e-ae79-411b-bc2d-e851b1530181.svg'
AUTHOR = 'gpt-6'

class TimeClockThreeToSix(Solo48):
    icon_id = 'time-clock-three-to-six'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    aliases = ()
    keywords = ('time', 'clock', 'three', 'to', 'six', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (35, 23), (23, 23))
        self.add_line('e1', (23, 23), (23, 34))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0', 'e1'), closed=False)
        self.add_contour('e2', *('e2-top', 'e2-bottom'), closed=True)
