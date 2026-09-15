"""Wink (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dd8865b-3604-51e7-a9f8-21d3178f09a9'
SOURCE_PATH = 'pictographic-primitives/smileys/wink_8dd8865b-3604-51e7-a9f8-21d3178f09a9.svg'
AUTHOR = 'gpt-6'

class Wink(Solo48):
    icon_id = 'wink'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('wink', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1', (16, 20), (19, 20), radius_x=2, radius_y=2, large_arc=True, sweep=True)
        self.add_arc('e2', (28, 20), (35, 20), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e3', (15, 29), (34, 29), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_contour('c0', *('e1',), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
        self.add_contour('e0', *('e0-top', 'e0-bottom'), closed=True)
