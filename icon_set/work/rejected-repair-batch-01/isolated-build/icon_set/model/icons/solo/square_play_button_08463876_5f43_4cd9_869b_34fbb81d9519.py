"""Square play button (medias), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08463876-5f43-4cd9-869b-34fbb81d9519'
SOURCE_PATH = 'pictographic-primitives/medias/square play button_08463876-5f43-4cd9-869b-34fbb81d9519.svg'
AUTHOR = 'gpt-6'

class SquarePlayButton(Solo48):
    icon_id = 'square-play-button'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'medias'
    aliases = ()
    keywords = ('square', 'play', 'button', 'medias')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('sym-e0', (41, 8), (7, 8))
        self.add_arc('sym-e1', (7, 8), (4, 11), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e2', (4, 11), (4, 24))
        self.add_line('sym-e3', (4, 24), (4, 37))
        self.add_arc('sym-e4', (4, 37), (7, 40), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e5', (7, 40), (41, 40))
        self.add_arc('sym-e6', (41, 40), (44, 37), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e7', (44, 37), (44, 24))
        self.add_line('sym-e8', (44, 24), (44, 11))
        self.add_arc('sym-e9', (44, 11), (41, 8), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e10', (29, 22), (20, 17))
        self.add_arc('sym-e11', (20, 17), (18, 19), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e13', (18, 19), (18, 24))
        self.add_line('sym-e14', (18, 24), (18, 29))
        self.add_arc('sym-e16', (18, 29), (20, 31), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e17', (20, 31), (29, 26))
        self.add_line('sym-e18', (29, 26), (31, 24))
        self.add_line('sym-e19', (31, 24), (29, 22))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9'), closed=True)
        self.add_contour('sym-c1', *('sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19'), closed=True)
