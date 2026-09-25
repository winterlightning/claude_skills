"""Volume control (audio), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2722b0f-fff4-493b-8f5d-619316ae89e6'
SOURCE_PATH = 'pictographic-primitives/audio/volume control_f2722b0f-fff4-493b-8f5d-619316ae89e6.svg'
AUTHOR = 'gpt-6'

class VolumeControl(Solo48):
    icon_id = 'volume-control'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('volume', 'control', 'audio')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (13, 31), (8, 31))
        self.add_line('e1', (4, 28), (4, 20))
        self.add_line('e2', (7, 17), (13, 17))
        self.add_line('e3', (13, 31), (13, 17))
        self.add_line('e4', (13, 31), (27, 40))
        self.add_line('e5', (30, 38), (30, 10))
        self.add_line('e6', (27, 9), (13, 17))
        self.add_line('e7-1', (8, 31), (5, 30))
        self.add_line('e7-2', (5, 30), (4, 28))
        self.add_arc('e8', (4, 20), (7, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('e9-1', (27, 40), (29, 40))
        self.add_arc('e9-2', (29, 40), (30, 38), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('e10-1', (30, 10), (28, 8), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e10-2', (28, 8), (27, 9))
        self.add_arc('e11-1', (39, 16), (44, 24), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('e11-2', (44, 24), (39, 32), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0', 'e7-1', 'e7-2', 'e1', 'e8', 'e2'), closed=False)
        self.add_contour('c1', *('e3',), closed=False)
        self.add_contour('c2', *('e4', 'e9-1', 'e9-2', 'e5', 'e10-1', 'e10-2', 'e6'), closed=False)
        self.add_contour('c3', *('e11-1', 'e11-2'), closed=False)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
