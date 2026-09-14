"""Bookmarks document (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8aff800c-f21e-5d80-8a99-6aecc047841b'
SOURCE_PATH = 'icons-json/interface-essential/bookmarks document_8aff800c-f21e-5d80-8a99-6aecc047841b.json'
AUTHOR = 'json_to_solo'

class BookmarksDocumentInterfaceEssential(Solo48):
    icon_id = 'bookmarks-document-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('bookmarks', 'document', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 25), (33, 19))
        self.add_line('e1', (33, 19), (26, 24))
        self.add_line('e2', (26, 24), (26, 4))
        self.add_line('e3', (36, 44), (12, 44))
        self.add_line('e4', (8, 40), (8, 9))
        self.add_line('e5', (11, 4), (36, 4))
        self.add_line('e6', (40, 9), (40, 40))
        self.add_bezier('e7', (12, 44), ((11.81, 44), (11.63, 43.982), (11.44, 43.982)), ((9.41, 43.982), (8, 41.691), (8, 40)))
        self.add_bezier('e8', (8, 9), ((8, 8.773), (8.01, 8.1), (8.01, 7.873)), ((8.01, 6.5), (9.16, 4), (11, 4)))
        self.add_bezier('e9', (36, 4), ((36.12, 4), (36.24, 4), (36.36, 4)), ((38.36, 4), (39.98, 5.664), (39.98, 7.445)), ((39.98, 7.864), (40, 8.291), (40, 8.718)), ((40, 8.964), (40, 8.755), (40, 9)))
        self.add_bezier('e10', (40, 40), ((39.99, 40.155), (39.99, 40.664), (39.98, 40.818)), ((39.98, 42.618), (37.86, 44), (36, 44)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
