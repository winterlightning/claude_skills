"""Kiss (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d7ea7dd-e49c-5a02-891f-cdbd627ace40'
SOURCE_PATH = 'pictographic-primitives/smileys/kiss_6d7ea7dd-e49c-5a02-891f-cdbd627ace40.svg'
AUTHOR = 'gpt-6'

class Kiss(Solo48):
    icon_id = 'kiss'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('kiss', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1-1', (25, 28), (28, 29), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e1-2', (28, 29), (28, 32), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e2', (28, 32), (25, 35), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e3', (28, 32), (27, 32), radius_x=26, radius_y=26, large_arc=False, sweep=False)
        self.add_arc('e4', (13, 20), (20, 20), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5', (29, 20), (35, 20), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('c0', *('e1-1', 'e1-2'), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
        self.add_contour('c3', *('e4',), closed=False)
        self.add_contour('c4', *('e5',), closed=False)
        self.add_contour('e0', *('e0-top', 'e0-bottom'), closed=True)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
