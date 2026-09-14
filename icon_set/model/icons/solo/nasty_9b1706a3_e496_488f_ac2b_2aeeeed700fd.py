"""Nasty (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b1706a3-e496-488f-ac2b-2aeeeed700fd'
SOURCE_PATH = 'icons-json/smileys/nasty_9b1706a3-e496-488f-ac2b-2aeeeed700fd.json'
AUTHOR = 'gpt-6'

class Nasty(Solo48):
    icon_id = 'nasty'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('nasty', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (14, 18), (20, 21))
        self.add_line('e1', (28, 21), (34, 18))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e3', (17, 33), (31, 33), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
        self.add_contour('e2', *('e2-top', 'e2-bottom'), closed=True)
