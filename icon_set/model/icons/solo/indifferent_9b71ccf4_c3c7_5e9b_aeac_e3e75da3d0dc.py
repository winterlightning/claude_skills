"""Indifferent (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b71ccf4-c3c7-5e9b-aeac-e3e75da3d0dc'
SOURCE_PATH = 'pictographic-primitives/smileys/indifferent_9b71ccf4-c3c7-5e9b-aeac-e3e75da3d0dc.svg'
AUTHOR = 'gpt-6'

class Indifferent(Solo48):
    icon_id = 'indifferent'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('indifferent', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (13, 20), (20, 20))
        self.add_line('e1', (28, 20), (35, 20))
        self.add_line('e2', (16, 32), (32, 32))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('e3', *('e3-top', 'e3-bottom'), closed=True)
