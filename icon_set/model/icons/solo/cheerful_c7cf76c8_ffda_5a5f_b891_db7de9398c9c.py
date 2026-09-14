"""Cheerful (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7cf76c8-ffda-5a5f-b891-db7de9398c9c'
SOURCE_PATH = 'icons-json/smileys/cheerful_c7cf76c8-ffda-5a5f-b891-db7de9398c9c.json'
AUTHOR = 'gpt-6'

class Cheerful(Solo48):
    icon_id = 'cheerful'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('cheerful', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (15, 27), (19, 28))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e2-1', (33, 27), (24, 35), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e2-2', (24, 35), (15, 27), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e3-1', (19, 28), (33, 27), radius_x=54, radius_y=54, large_arc=False, sweep=False)
        self.add_line('e3-2', (33, 27), (32, 29))
        self.add_arc('e4-1', (14, 19), (17, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e4-2', (17, 16), (19, 19), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e5-1', (28, 19), (31, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e5-2', (31, 16), (34, 19), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('c0', *('e2-1', 'e2-2', 'e0', 'e3-1', 'e3-2'), closed=False)
        self.add_contour('c1', *('e4-1', 'e4-2'), closed=False)
        self.add_contour('c2', *('e5-1', 'e5-2'), closed=False)
        self.add_contour('e1', *('e1-top', 'e1-bottom'), closed=True)
