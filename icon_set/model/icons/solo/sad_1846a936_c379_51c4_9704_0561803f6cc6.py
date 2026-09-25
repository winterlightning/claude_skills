"""Sad (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1846a936-c379-51c4-9704-0561803f6cc6'
SOURCE_PATH = 'pictographic-primitives/smileys/sad_1846a936-c379-51c4-9704-0561803f6cc6.svg'
AUTHOR = 'gpt-6'

class Sad(Solo48):
    icon_id = 'sad'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('sad', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1', (16, 32), (32, 32), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e2', (13, 21), (20, 18), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e3', (29, 19), (35, 22), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_contour('c0', *('e1',), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
        self.add_contour('e0', *('e0-top', 'e0-bottom'), closed=True)
