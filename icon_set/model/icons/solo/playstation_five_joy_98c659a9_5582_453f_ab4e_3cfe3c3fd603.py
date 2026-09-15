"""Playstation five joy (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98c659a9-5582-453f-ab4e-3cfe3c3fd603'
SOURCE_PATH = 'pictographic-primitives/video-games/playstation five joy_98c659a9-5582-453f-ab4e-3cfe3c3fd603.svg'
AUTHOR = 'gpt-6'

class PlaystationFiveJoy(Solo48):
    icon_id = 'playstation-five-joy'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('playstation', 'five', 'joy', 'video-games')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('sym-e0', (29, 20), (33, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (33, 20), (29, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (19, 20), (15, 20), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('sym-e3', (15, 20), (19, 20), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e4', (24, 8), (36, 8))
        self.add_arc('sym-e5', (36, 8), (40, 14), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e6', (40, 14), (44, 34))
        self.add_line('sym-e7', (44, 34), (44, 35))
        self.add_arc('sym-e8', (44, 35), (40, 40), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e11', (40, 40), (38, 39))
        self.add_line('sym-e12', (38, 39), (32, 33))
        self.add_line('sym-e13', (32, 33), (31, 31))
        self.add_line('sym-e14', (31, 31), (24, 31))
        self.add_line('sym-e15', (24, 31), (17, 31))
        self.add_line('sym-e16', (17, 31), (16, 33))
        self.add_line('sym-e17', (16, 33), (10, 39))
        self.add_arc('sym-e18', (10, 39), (8, 40), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('sym-e21', (8, 40), (4, 35), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e22', (4, 35), (4, 34))
        self.add_line('sym-e23', (4, 34), (8, 14))
        self.add_arc('sym-e24', (8, 14), (12, 8), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e25', (12, 8), (24, 8))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1'), closed=True)
        self.add_contour('sym-c1', *('sym-e2', 'sym-e3'), closed=True)
        self.add_contour('sym-c2', *('sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25'), closed=True)
