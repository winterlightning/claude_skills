"""Zoom out (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd05e7aa2-4c1e-43d5-8943-5f63cebcd390'
SOURCE_PATH = 'icons-json/interface-essential/zoom out_d05e7aa2-4c1e-43d5-8943-5f63cebcd390.json'
AUTHOR = 'gpt-6'

class ZoomOut(Solo48):
    icon_id = 'zoom-out'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zoom', 'out', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (42, 42), (34, 34))
        self.add_line('e1', (15, 22), (29, 22))
        self.add_arc('e2-top', (6, 22), (38, 22), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('e2-bottom', (38, 22), (6, 22), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('e3', (34, 34), (33, 32))
        self.add_contour('c0', *('e0', 'e3'), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('e2', *('e2-top', 'e2-bottom'), closed=True)
        self.relate('connect', *('c0', 'e2'))
