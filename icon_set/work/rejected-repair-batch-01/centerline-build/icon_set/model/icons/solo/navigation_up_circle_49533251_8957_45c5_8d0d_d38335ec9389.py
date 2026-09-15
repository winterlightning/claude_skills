"""Navigation up circle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49533251-8957-45c5-8d0d-d38335ec9389'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation up circle_49533251-8957-45c5-8d0d-d38335ec9389.svg'
AUTHOR = 'gpt-6'

class NavigationUpCircle(Solo48):
    icon_id = 'navigation-up-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'up', 'circle', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (16, 20), (24, 13))
        self.add_line('e1', (24, 35), (24, 13))
        self.add_line('e2', (32, 20), (24, 13))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('e3', *('e3-top', 'e3-bottom'), closed=True)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
