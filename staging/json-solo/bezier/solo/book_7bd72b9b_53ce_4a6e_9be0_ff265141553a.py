"""Book (content), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bd72b9b-53ce-4a6e-9be0-ff265141553a'
SOURCE_PATH = 'icons-json/content/book_7bd72b9b-53ce-4a6e-9be0-ff265141553a.json'
AUTHOR = 'json_to_solo'

class Book7bd72b9b(Solo48):
    icon_id = 'book-7bd72b9b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'content')

    def build(self):
        self.add_line('e0', (8, 12), (10, 14))
        self.add_line('e1', (12, 15), (40, 15))
        self.add_line('e2', (40, 13), (40, 44))
        self.add_line('e3', (40, 44), (12, 44))
        self.add_line('e4', (8, 41), (8, 9))
        self.add_line('e5', (11, 4), (40, 4))
        self.add_bezier('e6', (10, 14), ((10.54, 14.318), (11.32, 15), (12, 15)))
        self.add_bezier('e7', (40, 4), ((40, 4.255), (39.99, 4.509), (39.99, 4.764)), ((39.99, 5.018), (39.48, 5.382), (39.39, 5.664)), ((39.11, 6.5), (39.07, 7.382), (39.04, 8.245)), ((39.01, 9.136), (39.11, 10.264), (39.43, 11.1)), ((39.68, 11.755), (40, 12.282), (40, 13)))
        self.add_bezier('e8', (12, 44), ((11.96, 44), (11.92, 44), (11.88, 44)), ((10.56, 44), (9.06, 42.9), (8.34, 42)), ((8.16, 41.764), (8.13, 41.236), (8, 41)))
        self.add_bezier('e9', (8, 9), ((8, 8.873), (8, 8.291), (8, 8.164)), ((8, 6.764), (8.99, 4.764), (10.45, 4.136)), ((10.63, 4.055), (10.82, 4.073), (11, 4)))
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e7', 'e2', 'e3', 'e8', 'e4', 'e9', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
