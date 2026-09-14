"""Common file horizontal (files), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2da1f41-1d77-5a50-a868-201009ba3c2a'
SOURCE_PATH = 'icons-json/files/common file horizontal_f2da1f41-1d77-5a50-a868-201009ba3c2a.json'
AUTHOR = 'json_to_solo'

class CommonFileHorizontalFiles(Solo48):
    icon_id = 'common-file-horizontal-files'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('common', 'file', 'horizontal', 'files')

    def build(self):
        self.add_line('e0', (4, 38), (4, 11))
        self.add_line('e1', (6, 8), (35, 8))
        self.add_line('e2', (44, 18), (44, 37))
        self.add_line('e3', (42, 40), (7, 40))
        self.add_bezier('e4', (7, 40), ((6.909, 40), (6.536, 40), (6.445, 40)), ((6.145, 40), (5.855, 40), (5.555, 40)), ((4.673, 40), (4.264, 38.67), (4, 38)))
        self.add_bezier('e5', (4, 11), ((4, 10.8), (4.009, 10.61), (4.009, 10.41)), ((4.009, 9.29), (4.836, 8), (6, 8)))
        self.add_bezier('e6', (35, 8), ((35.082, 8), (35.082, 8.01), (35.164, 8.01)), ((36.518, 8.01), (37.327, 9.17), (38.191, 10.12)), ((39.573, 11.63), (40.936, 13.17), (42.291, 14.71)), ((42.682, 15.14), (43.327, 15.66), (43.582, 16.21)), ((43.827, 16.74), (44, 17.4), (44, 18)))
        self.add_bezier('e7', (44, 37), ((44, 38.34), (42.827, 39.2), (42, 40)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', closed=True)
