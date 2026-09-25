"""Navigation down circle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18069a19-0b23-40e6-a387-d8413a5d55b4'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation down circle_18069a19-0b23-40e6-a387-d8413a5d55b4.svg'
AUTHOR = 'gpt-6'

class NavigationDownCircle(Solo48):
    icon_id = 'navigation-down-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'down', 'circle', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 13), (24, 35))
        self.add_line('e1', (16, 27), (24, 35))
        self.add_line('e2', (32, 27), (24, 35))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('e3', *('e3-top', 'e3-bottom'), closed=True)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
