"""Vectors add anchor (internet), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb962df2-7d7e-4704-b588-8cea12d18d62'
SOURCE_PATH = 'pictographic-primitives/internet/vectors add anchor_eb962df2-7d7e-4704-b588-8cea12d18d62.svg'
AUTHOR = 'gpt-6'

class VectorsAddAnchor(Solo48):
    icon_id = 'vectors-add-anchor'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    categories = ('internet', 'primitives')
    aliases = ()
    keywords = ('vectors', 'add', 'anchor', 'internet')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 40), (14, 29))
        self.add_line('e1', (14, 24), (32, 24))
        self.add_line('e2', (24, 10), (14, 21))
        self.add_arc('e3-top', (24, 40), (30, 40), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e3-bottom', (30, 40), (24, 40), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e4-top', (34, 24), (40, 24), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e4-bottom', (40, 24), (34, 24), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e5-top', (24, 8), (30, 8), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e5-bottom', (30, 8), (24, 8), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e6-top', (8, 24), (14, 24), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e6-bottom', (14, 24), (8, 24), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('e6', *('e6-top', 'e6-bottom'), closed=True)
        self.add_contour('e3', *('e3-top', 'e3-bottom'), closed=True)
        self.add_contour('e4', *('e4-top', 'e4-bottom'), closed=True)
        self.add_contour('e5', *('e5-top', 'e5-bottom'), closed=True)
        self.relate('connect', *('c0', 'e3'))
        self.relate('connect', *('c0', 'e6'))
        self.relate('connect', *('c1', 'e6'))
        self.relate('connect', *('c1', 'e4'))
        self.relate('connect', *('c2', 'e5'))
        self.relate('connect', *('c2', 'e6'))
