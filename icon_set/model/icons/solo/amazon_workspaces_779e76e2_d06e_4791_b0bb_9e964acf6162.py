"""Amazon workspaces (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '779e76e2-d06e-4791-b0bb-9e964acf6162'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/amazon workspaces_779e76e2-d06e-4791-b0bb-9e964acf6162.svg'
AUTHOR = 'gpt-6'

class AmazonWorkspaces(Solo48):
    icon_id = 'amazon-workspaces'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('amazon', 'workspaces', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (25, 42), (42, 34))
        self.add_line('e1', (42, 34), (42, 15))
        self.add_line('e2', (24, 42), (24, 23))
        self.add_line('e3', (24, 42), (6, 33))
        self.add_line('e4', (6, 33), (6, 15))
        self.add_line('e5', (6, 15), (24, 23))
        self.add_line('e6', (6, 15), (24, 6))
        self.add_line('e7', (24, 6), (42, 15))
        self.add_line('e8', (42, 15), (24, 23))
        self.add_line('e9', (24, 42), (25, 42))
        self.add_contour('c0', 'e9', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', closed=False)
        self.add_contour('c2', 'e3', 'e4', closed=False)
        self.add_contour('c3', 'e5', closed=False)
        self.add_contour('c4', 'e6', 'e7', closed=False)
        self.add_contour('c5', 'e8', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
