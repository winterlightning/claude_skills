"""Shrink (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b7da143-8b5a-4a81-adf1-224493bbe35d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/shrink_8b7da143-8b5a-4a81-adf1-224493bbe35d.svg'
AUTHOR = 'gpt-6'

class Shrink(Solo48):
    icon_id = 'shrink'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('shrink', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (42, 6), (27, 21))
        self.add_line('e1', (27, 9), (27, 21))
        self.add_line('e2', (39, 21), (27, 21))
        self.add_line('e3', (11, 27), (21, 27))
        self.add_line('e4', (6, 42), (21, 27))
        self.add_line('e5', (22, 36), (21, 27))
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3',), closed=False)
        self.add_contour('c4', *('e4',), closed=False)
        self.add_contour('c5', *('e5',), closed=False)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
        self.relate('connect', *('c3', 'c4'))
        self.relate('connect', *('c3', 'c5'))
        self.relate('connect', *('c4', 'c5'))
