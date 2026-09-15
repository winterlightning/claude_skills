"""Signal wave (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b320e1dd-5fff-5392-b1e9-42b786d6d39b'
SOURCE_PATH = 'pictographic-primitives/interface-essential/signal wave_b320e1dd-5fff-5392-b1e9-42b786d6d39b.svg'
AUTHOR = 'gpt-6'

class SignalWave(Solo48):
    icon_id = 'signal-wave'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('signal', 'wave', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-top', (8, 24), (20, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (20, 24), (8, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e1-1', (25, 38), (30, 23), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_arc('e1-2', (30, 23), (25, 9), radius_x=25, radius_y=25, large_arc=False, sweep=False)
        self.add_arc('e2-1', (32, 4), (40, 24), radius_x=29, radius_y=29, large_arc=False, sweep=True)
        self.add_arc('e2-2', (40, 24), (32, 44), radius_x=29, radius_y=29, large_arc=False, sweep=True)
        self.add_contour('c0', *('e1-1', 'e1-2'), closed=False)
        self.add_contour('c1', *('e2-1', 'e2-2'), closed=False)
        self.add_contour('e0', *('e0-top', 'e0-bottom'), closed=True)
