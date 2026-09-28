"""Smirk (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b2da279-812c-5533-9f31-a920f7b8d2ab'
SOURCE_PATH = 'pictographic-primitives/smileys/smirk_9b2da279-812c-5533-9f31-a920f7b8d2ab.svg'
AUTHOR = 'gpt-6'

class Smirk(Solo48):
    icon_id = 'smirk'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('smirk', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1', (22, 35), (34, 30), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('e2', (14, 18), (20, 19), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e3', (28, 21), (35, 20), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('e4', (18, 27), (18, 28), radius_x=29, radius_y=29, large_arc=False, sweep=False)
        self.add_contour('c0', *('e1',), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
        self.add_contour('c3', *('e4',), closed=False)
        self.add_contour('e0', *('e0-top', 'e0-bottom'), closed=True)
