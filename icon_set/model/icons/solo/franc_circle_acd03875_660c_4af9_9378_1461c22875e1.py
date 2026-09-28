"""Franc circle (money), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'acd03875-660c-4af9-9378-1461c22875e1'
SOURCE_PATH = 'pictographic-primitives/money/franc circle_acd03875-660c-4af9-9378-1461c22875e1.svg'
AUTHOR = 'gpt-6'

class FrancCircle(Solo48):
    icon_id = 'franc-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('primitives', 'money')
    aliases = ()
    keywords = ('franc', 'circle', 'money')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (30, 14), (19, 14))
        self.add_line('e1', (19, 14), (19, 24))
        self.add_line('e2', (19, 34), (19, 24))
        self.add_line('e3', (28, 24), (19, 24))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0', 'e1'), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
        self.add_contour('e4', *('e4-top', 'e4-bottom'), closed=True)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
