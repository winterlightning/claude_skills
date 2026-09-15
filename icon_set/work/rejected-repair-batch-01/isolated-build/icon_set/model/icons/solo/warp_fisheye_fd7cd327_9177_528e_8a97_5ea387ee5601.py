"""Warp fisheye (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd7cd327-9177-528e-8a97-5ea387ee5601'
SOURCE_PATH = 'pictographic-primitives/design/warp fisheye_fd7cd327-9177-528e-8a97-5ea387ee5601.svg'
AUTHOR = 'gpt-6'

class WarpFisheye(Solo48):
    icon_id = 'warp-fisheye'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'fisheye', 'design')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('sym-e0', (15, 24), (33, 24), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (33, 24), (15, 24), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('sym-e2', (6, 24), (6, 8))
        self.add_arc('sym-e4', (6, 8), (8, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e6', (8, 6), (40, 6))
        self.add_line('sym-e8', (40, 6), (42, 7))
        self.add_line('sym-e9', (42, 7), (42, 8))
        self.add_line('sym-e10', (42, 8), (42, 24))
        self.add_line('sym-e11', (42, 24), (42, 40))
        self.add_arc('sym-e12', (42, 40), (42, 41), radius_x=40, radius_y=40, large_arc=False, sweep=False)
        self.add_line('sym-e13', (42, 41), (40, 42))
        self.add_line('sym-e15', (40, 42), (8, 42))
        self.add_arc('sym-e17', (8, 42), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e19', (6, 40), (6, 24))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1'), closed=True)
        self.add_contour('sym-c1', *('sym-e2', 'sym-e4', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e17', 'sym-e19'), closed=True)
