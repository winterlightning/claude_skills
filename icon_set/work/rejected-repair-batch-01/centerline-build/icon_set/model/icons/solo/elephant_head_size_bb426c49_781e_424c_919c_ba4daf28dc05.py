"""elephant-head-profile: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb426c49-781e-424c-919c-ba4daf28dc05'
SOURCE_PATH = 'pictographic-primitives/animals/elephant head size_bb426c49-781e-424c-919c-ba4daf28dc05.svg'
AUTHOR = 'gpt-6'


class ElephantHeadProfile(Solo48):
    icon_id = 'elephant-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('elephant', 'head', 'profile', 'trunk', 'tusk', 'ear', 'animal', 'wildlife')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('head-trunk-1', (6, 12), (14, 6), radius_x=12, radius_y=7, large_arc=False, sweep=True)
        self.add_bezier('head-trunk-2', (14, 6), *(((21.9089568, 6), (28.47275448, 12.1086174), (29, 20)),))
        self.add_arc('head-trunk-3', (29, 20), (35, 26), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('head-trunk-4', (35, 26), (39, 22), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('head-trunk-5', (39, 22), (38, 7), radius_x=30, radius_y=30, large_arc=False, sweep=False)
        self.add_line('head-trunk-6', (38, 7), (42, 8))
        self.add_bezier('head-trunk-7', (42, 8), *(((42, 11.09401077), (42, 14.90598923), (42, 18)),))
        self.add_bezier('head-trunk-8', (42, 18), *(((42, 26.00256917), (39.04103628, 33.34105076), (34, 36)),))
        self.add_line('head-trunk-9', (34, 36), (24, 33))
        self.add_arc('ear-1', (13, 16), (6, 31), radius_x=10, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('jaw-1', (24, 33), (16, 36), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('jaw-2', (16, 36), (10, 42), radius_x=6, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('tusk-1', (24, 33), (35, 42), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('eye', (21, 21), (21, 21))
        self.add_contour('head-trunk', *('head-trunk-1', 'head-trunk-2', 'head-trunk-3', 'head-trunk-4', 'head-trunk-5', 'head-trunk-6', 'head-trunk-7', 'head-trunk-8', 'head-trunk-9'), closed=False)
        self.add_contour('ear', *('ear-1',), closed=False)
        self.add_contour('jaw', *('jaw-1', 'jaw-2'), closed=False)
        self.add_contour('tusk', *('tusk-1',), closed=False)
        self.relate('connect', *('jaw', 'head-trunk'))
        self.relate('connect', *('tusk', 'head-trunk'))
        self.relate('connect', *('tusk', 'jaw'))
