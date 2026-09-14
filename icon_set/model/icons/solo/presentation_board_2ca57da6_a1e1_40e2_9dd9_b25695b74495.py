'Presentation board: even header band, rounded board and a symmetric tripod.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ca57da6-a1e1-40e2-9dd9-b25695b74495'
SOURCE_PATH = 'icons-json/office/presentation board_2ca57da6-a1e1-40e2-9dd9-b25695b74495.json'
AUTHOR = 'gpt-6'

class PresentationBoard(Solo48):
    icon_id = 'presentation-board-office'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'board', 'office')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('board-0', (9, 6), (39, 6))
        self.add_arc('board-1', (39, 6), (42, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('board-2', (42, 9), (42, 27))
        self.add_arc('board-3', (42, 27), (39, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('board-4', (39, 30), (9, 30))
        self.add_arc('board-5', (9, 30), (6, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('board-6', (6, 27), (6, 9))
        self.add_arc('board-7', (6, 9), (9, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('header', (6, 14), (42, 14))
        self.add_line('stem', (24, 30), (24, 42))
        self.add_line('legs-1', (14, 42), (24, 30))
        self.add_line('legs-2', (24, 30), (34, 42))
        self.add_contour('board', *('board-0', 'board-1', 'board-2', 'board-3', 'board-4', 'board-5', 'board-6', 'board-7'), closed=True)
        self.add_contour('legs', *('legs-1', 'legs-2'), closed=False)
        self.relate('connect', *('header', 'board'))
        self.relate('connect', *('stem', 'board'))
        self.relate('connect', *('legs', 'board'))
        self.relate('connect', *('legs', 'stem'))
