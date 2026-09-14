"""Amazon workdocs (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2d8430c-6c7b-4487-912e-4dca17690e6b'
SOURCE_PATH = 'icons-json/_uncategorized_03/amazon workdocs_d2d8430c-6c7b-4487-912e-4dca17690e6b.json'
AUTHOR = 'json_to_solo'

class AmazonWorkdocsUncategorized03(Solo48):
    icon_id = 'amazon-workdocs-uncategorized-03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('amazon', 'workdocs', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (25, 31), (25, 42))
        self.add_line('e1', (27, 6), (42, 21))
        self.add_line('e2', (27, 6), (27, 21))
        self.add_line('e3', (27, 21), (42, 21))
        self.add_line('e4', (27, 6), (8, 6))
        self.add_line('e5', (6, 8), (6, 40))
        self.add_line('e6', (8, 42), (25, 42))
        self.add_line('e7', (42, 21), (42, 40))
        self.add_line('e8', (40, 42), (25, 42))
        self.add_bezier('e9', (8, 6), ((6.871, 6.491), (6.581, 6.855), (6, 8)))
        self.add_bezier('e10', (6, 40), ((6.458, 41.154), (6.871, 41.55), (8, 42)))
        self.add_bezier('e11', (42, 40), ((41.55, 41.006), (41.023, 41.566), (40, 42)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.add_contour('c4', 'e7', 'e11', 'e8')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
