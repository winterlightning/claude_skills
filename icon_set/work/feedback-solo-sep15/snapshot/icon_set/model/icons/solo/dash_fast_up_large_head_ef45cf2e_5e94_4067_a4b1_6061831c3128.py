"""Dash fast up large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef45cf2e-5e94-4067-a4b1-6061831c3128'
SOURCE_PATH = 'pictographic-primitives/arrows/dash fast up large head_ef45cf2e-5e94-4067-a4b1-6061831c3128.svg'
AUTHOR = 'gpt-6'

class DashFastUpLargeHead(Solo48):
    icon_id = 'dash-fast-up-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('dash', 'fast', 'up', 'large', 'head', 'arrows')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (34, 14), (40, 8))
        self.add_line('e1', (39, 10), (40, 8))
        self.add_line('e2', (44, 17), (40, 8))
        self.add_line('e3', (4, 40), (9, 40))
        self.add_line('e4', (16, 32), (20, 32))
        self.add_arc('e5', (24, 39), (39, 10), radius_x=30, radius_y=30, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e5', 'e1'), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3',), closed=False)
        self.add_contour('c4', *('e4',), closed=False)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
