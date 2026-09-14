"""Download arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58683514-619a-4591-ab3b-7d4cfa512a2d'
SOURCE_PATH = 'icons-json/arrows/download arrow_58683514-619a-4591-ab3b-7d4cfa512a2d.json'
AUTHOR = 'json_to_solo'

class DownloadArrow58683514(Solo48):
    icon_id = 'download-arrow-58683514'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('download', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (4, 40), (44, 40))
        self.add_line('e1', (10, 8), (38, 8))
        self.add_line('e2', (39, 10), (25, 29))
        self.add_line('e3', (23, 28), (9, 10))
        self.add_bezier('e4', (38, 8), ((38.2, 8.209), (38.073, 8.172), (38.264, 8.431)), ((38.518, 8.763), (38.773, 9.095), (39.027, 9.428)), ((38.864, 9.772), (39.164, 9.655), (39, 10)))
        self.add_bezier('e5', (25, 29), ((23.955, 28.791), (23.755, 29.022), (23, 28)))
        self.add_bezier('e6', (9, 10), ((8.791, 9.606), (9.036, 9.674), (8.827, 9.292)), ((9.127, 8.972), (9.418, 8.652), (9.718, 8.332)), ((9.918, 8.111), (9.8, 8.172), (10, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2', 'e5', 'e3', 'e6', closed=True)
