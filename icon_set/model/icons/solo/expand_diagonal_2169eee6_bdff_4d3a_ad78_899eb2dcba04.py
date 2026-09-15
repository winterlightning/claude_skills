"""Expand diagonal (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2169eee6-bdff-4d3a-ad78-899eb2dcba04'
SOURCE_PATH = 'pictographic-primitives/design/expand diagonal_2169eee6-bdff-4d3a-ad78-899eb2dcba04.svg'
AUTHOR = 'gpt-6'

class ExpandDiagonal(Solo48):
    icon_id = 'expand-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('expand', 'diagonal', 'design')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (6, 28), (6, 9))
        self.add_line('e1', (9, 6), (22, 6))
        self.add_line('e2', (33, 6), (42, 6))
        self.add_line('e3', (31, 17), (42, 6))
        self.add_line('e4', (42, 14), (42, 6))
        self.add_line('e5', (22, 42), (39, 42))
        self.add_line('e6', (42, 39), (42, 24))
        self.add_line('e7', (14, 35), (9, 40))
        self.add_line('e8', (9, 40), (8, 41))
        self.add_line('e9', (8, 36), (8, 41))
        self.add_line('e10', (13, 41), (8, 41))
        self.add_arc('e11', (6, 9), (9, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e12', (39, 42), (42, 39), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0', 'e11', 'e1'), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
        self.add_contour('c3', *('e4',), closed=False)
        self.add_contour('c4', *('e5', 'e12', 'e6'), closed=False)
        self.add_contour('c5', *('e7', 'e8'), closed=False)
        self.add_contour('c6', *('e9',), closed=False)
        self.add_contour('c7', *('e10',), closed=False)
        self.relate('connect', *('c1', 'c2'))
        self.relate('connect', *('c1', 'c3'))
        self.relate('connect', *('c2', 'c3'))
        self.relate('connect', *('c5', 'c6'))
        self.relate('connect', *('c5', 'c7'))
        self.relate('connect', *('c6', 'c7'))
