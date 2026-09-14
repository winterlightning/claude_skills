"""Download thick bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f02c296e-38c9-49af-a6ae-79517bb004c6'
SOURCE_PATH = 'icons-json/arrows/download thick bottom_f02c296e-38c9-49af-a6ae-79517bb004c6.json'
AUTHOR = 'json_to_solo'

class DownloadThickBottomArrows(Solo48):
    icon_id = 'download-thick-bottom-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('download', 'thick', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (6, 34), (6, 40))
        self.add_line('e1', (8, 42), (40, 42))
        self.add_line('e2', (42, 40), (42, 34))
        self.add_line('e3', (13, 23), (17, 23))
        self.add_line('e4', (18, 22), (18, 8))
        self.add_line('e5', (20, 6), (28, 6))
        self.add_line('e6', (30, 8), (30, 23))
        self.add_line('e7', (30, 23), (35, 23))
        self.add_line('e8', (35, 23), (24, 34))
        self.add_line('e9', (23, 34), (13, 23))
        self.add_bezier('e10', (6, 40), ((6.434, 41.015), (6.977, 41.55), (8, 42)))
        self.add_bezier('e11', (40, 42), ((40.057, 42), (39.66, 42), (39.709, 41.992)), ((40.863, 41.992), (41.485, 40.875), (42, 40)))
        self.add_bezier('e12', (17, 23), ((17.278, 22.73), (17.722, 22.278), (18, 22)))
        self.add_bezier('e13', (18, 8), ((18.524, 6.895), (18.92, 6.507), (20, 6)))
        self.add_bezier('e14', (28, 6), ((28.131, 6.065), (28.394, 6.033), (28.533, 6.09)), ((29.195, 6.36), (29.714, 7.419), (30, 8)))
        self.add_bezier('e15', (24, 34), ((23.73, 34), (23.27, 34), (23, 34)))
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11', 'e2')
        self.add_contour('c1', 'e3', 'e12', 'e4', 'e13', 'e5', 'e14', 'e6', 'e7', 'e8', 'e15', 'e9', closed=True)
