"""Expand horizontal 3 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82dd91e0-2890-49f9-b3c3-5d44c6568951'
SOURCE_PATH = 'icons-json/interface-essential/expand horizontal 3_82dd91e0-2890-49f9-b3c3-5d44c6568951.json'
AUTHOR = 'gpt-6'

class ExpandHorizontal3(Solo48):
    icon_id = 'expand-horizontal-3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'horizontal', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 24), (6, 24))
        self.add_line('sym-e1', (6, 24), (11, 19))
        self.add_line('sym-e2', (24, 24), (42, 24))
        self.add_line('sym-e4', (42, 24), (37, 19))
        self.add_line('sym-e5', (24, 6), (24, 42))
        self.add_line('sym-e7', (11, 29), (6, 24))
        self.add_line('sym-e8', (37, 29), (42, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=False)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e4', closed=False)
        self.add_contour('sym-c2', 'sym-e5', closed=False)
        self.add_contour('sym-c3', 'sym-e7', closed=False)
        self.add_contour('sym-c4', 'sym-e8', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
