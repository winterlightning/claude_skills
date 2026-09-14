"""Oxygen (health), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53be8dfa-bf81-49e6-9db1-47746ac74ee9'
SOURCE_PATH = 'icons-json/health/oxygen_53be8dfa-bf81-49e6-9db1-47746ac74ee9.json'
AUTHOR = 'gpt-6'

class Oxygen(Solo48):
    icon_id = 'oxygen'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('oxygen', 'health')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1-top', (22, 18), (32, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e1-bottom', (32, 18), (22, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('e0', *('e0-top', 'e0-bottom'), closed=True)
        self.add_contour('e1', *('e1-top', 'e1-bottom'), closed=True)
