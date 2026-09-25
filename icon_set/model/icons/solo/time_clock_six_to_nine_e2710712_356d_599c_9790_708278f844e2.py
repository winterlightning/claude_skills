"""Time clock six to nine (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2710712-356d-599c-9790-708278f844e2'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time clock six to nine_e2710712-356d-599c-9790-708278f844e2.svg'
AUTHOR = 'gpt-6'

class TimeClockSixToNine(Solo48):
    icon_id = 'time-clock-six-to-nine'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('time', 'clock', 'six', 'to', 'nine', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (13, 24), (25, 24))
        self.add_line('e1', (25, 24), (25, 33))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0', 'e1'), closed=False)
        self.add_contour('e2', *('e2-top', 'e2-bottom'), closed=True)
