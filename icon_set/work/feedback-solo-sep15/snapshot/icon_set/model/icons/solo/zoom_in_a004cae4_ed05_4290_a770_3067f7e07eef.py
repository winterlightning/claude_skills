"""Zoom in (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a004cae4-ed05-4290-a770-3067f7e07eef'
SOURCE_PATH = 'pictographic-primitives/interface-essential/zoom in_a004cae4-ed05-4290-a770-3067f7e07eef.svg'
AUTHOR = 'gpt-6'

class ZoomIn(Solo48):
    icon_id = 'zoom-in'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zoom', 'in', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (42, 42), (29, 31))
        self.add_line('e1', (20, 15), (20, 20))
        self.add_line('e2', (15, 20), (20, 20))
        self.add_line('e3', (20, 25), (20, 20))
        self.add_line('e4', (25, 20), (20, 20))
        self.add_arc('e5-top', (6, 20), (34, 20), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('e5-bottom', (34, 20), (6, 20), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3',), closed=False)
        self.add_contour('c4', *('e4',), closed=False)
        self.add_contour('e5', *('e5-top', 'e5-bottom'), closed=True)
        self.relate('connect', *('c1', 'c2'))
        self.relate('connect', *('c1', 'c3'))
        self.relate('connect', *('c1', 'c4'))
        self.relate('connect', *('c2', 'c3'))
        self.relate('connect', *('c2', 'c4'))
        self.relate('connect', *('c3', 'c4'))
        self.relate('connect', *('c0', 'e5'))
