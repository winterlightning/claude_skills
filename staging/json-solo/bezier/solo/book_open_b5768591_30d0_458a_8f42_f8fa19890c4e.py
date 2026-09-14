"""Book open (content), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5768591-30d0-458a-8f42-f8fa19890c4e'
SOURCE_PATH = 'icons-json/content/book open_b5768591-30d0-458a-8f42-f8fa19890c4e.json'
AUTHOR = 'json_to_solo'

class BookOpen(Solo48):
    icon_id = 'book-open'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (4, 11), (4, 33))
        self.add_line('e1', (7, 36), (16, 37))
        self.add_line('e2', (44, 11), (44, 29))
        self.add_line('e3', (42, 36), (30, 37))
        self.add_bezier('e4', (24, 13), ((21.218, 9.783), (17.827, 9.204), (13.655, 8.531)), ((12.664, 8.371), (11.655, 8.008), (10.645, 8.008)), ((10.565, 8.008), (10.484, 8), (10.395, 8)), ((10.394, 8), (10.392, 8), (10.391, 8)), ((10.327, 8), (10.264, 8.008), (10.2, 8.008)), ((9.409, 8.008), (8.609, 8.202), (7.827, 8.295)), ((6.427, 8.455), (4, 8.362), (4, 10.282)), ((4, 10.366), (4, 10.924), (4, 11)))
        self.add_bezier('e5', (4, 33), ((4, 33.177), (4, 33.625), (4, 33.802)), ((4, 33.954), (4.136, 34.173), (4.173, 34.324)), ((4.509, 35.545), (5.827, 35.891), (7, 36)))
        self.add_bezier('e6', (16, 37), ((19.009, 37.278), (21.645, 38.366), (24, 40)))
        self.add_bezier('e7', (24, 13), ((24.664, 12.217), (25.327, 11.554), (26.209, 10.973)), ((29.464, 8.825), (34.355, 8.446), (38.218, 8.253)), ((39.355, 8.194), (40.5, 8), (41.636, 8)), ((42.945, 8), (43.991, 9.112), (43.991, 10.282)), ((43.991, 10.358), (44, 10.916), (44, 11)))
        self.add_bezier('e8', (44, 29), ((44, 30.305), (43.982, 31.655), (43.982, 32.96)), ((43.982, 34.392), (43.345, 35.225), (42, 36)))
        self.add_bezier('e9', (30, 37), ((27.664, 37.337), (25.836, 38.678), (24, 40)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e6')
        self.add_contour('c1', 'e7', 'e2', 'e8', 'e3', 'e9')
