"""Smile (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83cd55ce-7a5d-588c-85a9-6b8cc54ce8fc'
SOURCE_PATH = 'pictographic-primitives/smileys/smile_83cd55ce-7a5d-588c-85a9-6b8cc54ce8fc.svg'
AUTHOR = 'gpt-6'

class Smile83cd55ce(Solo48):
    icon_id = 'smile-83cd55ce'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('smile', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1-1', (14, 20), (17, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e1-2', (17, 17), (19, 20), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e2-1', (29, 19), (32, 17), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e2-2', (32, 17), (34, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e3', (14, 29), (33, 29), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_contour('c0', *('e1-1', 'e1-2'), closed=False)
        self.add_contour('c1', *('e2-1', 'e2-2'), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
        self.add_contour('e0', *('e0-top', 'e0-bottom'), closed=True)
