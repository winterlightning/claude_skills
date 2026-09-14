"""Book book pages (content), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '615824a7-abf4-5b8e-8b94-c28d2acde261'
SOURCE_PATH = 'icons-json/content/book book pages_615824a7-abf4-5b8e-8b94-c28d2acde261.json'
AUTHOR = 'json_to_solo'

class BookBookPagesContent(Solo48):
    icon_id = 'book-book-pages-content'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'pages', 'content')

    def build(self):
        self.add_line('e0', (24, 40), (24, 13))
        self.add_line('e1', (44, 11), (44, 34))
        self.add_line('e2', (42, 36), (30, 37))
        self.add_line('e3', (16, 37), (7, 36))
        self.add_line('e4', (4, 33), (4, 11))
        self.add_bezier('e5', (24, 13), ((27.291, 8.84), (33.345, 8.573), (38.464, 8.286)), ((39.536, 8.227), (40.582, 8), (41.655, 8)), ((42.827, 8), (44, 9.229), (44, 10.274)), ((44, 10.358), (44, 10.916), (44, 11)))
        self.add_bezier('e6', (44, 34), ((43.373, 35.036), (43.127, 35.427), (42, 36)))
        self.add_bezier('e7', (30, 37), ((28.336, 37.236), (26.873, 38.265), (25.436, 39.074)), ((25.045, 39.293), (24.773, 39.646), (24.4, 39.848)), ((24.264, 39.899), (24.136, 39.949), (24, 40)))
        self.add_bezier('e8', (24, 40), ((21.645, 38.366), (19.009, 37.278), (16, 37)))
        self.add_bezier('e9', (7, 36), ((5.827, 35.891), (4.509, 35.545), (4.173, 34.324)), ((4.136, 34.173), (4, 33.954), (4, 33.802)), ((4, 33.625), (4, 33.177), (4, 33)))
        self.add_bezier('e10', (4, 11), ((4, 10.924), (4, 10.366), (4, 10.282)), ((4, 8.362), (6.427, 8.455), (7.827, 8.295)), ((8.609, 8.202), (9.409, 8.008), (10.2, 8.008)), ((10.263, 8.008), (10.325, 8), (10.388, 8)), ((10.389, 8), (10.39, 8), (10.391, 8)), ((10.482, 8), (10.564, 8.008), (10.645, 8.008)), ((11.655, 8.008), (12.664, 8.371), (13.655, 8.531)), ((17.827, 9.204), (21.218, 9.783), (24, 13)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', closed=True)
        self.add_contour('c1', 'e8', 'e3', 'e9', 'e4', 'e10')
