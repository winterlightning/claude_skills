"""Download (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58449573-38e8-4aa0-bebb-14002004402f'
SOURCE_PATH = 'icons-json/arrows/download_58449573-38e8-4aa0-bebb-14002004402f.json'
AUTHOR = 'json_to_solo'

class DownloadArrows(Solo48):
    icon_id = 'download-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('download', 'arrows')

    def build(self):
        self.add_line('e0', (4, 33), (4, 37))
        self.add_line('e1', (9, 40), (42, 40))
        self.add_line('e2', (44, 38), (44, 33))
        self.add_line('e3', (24, 31), (24, 8))
        self.add_line('e4', (24, 31), (14, 22))
        self.add_line('e5', (24, 31), (33, 22))
        self.add_bezier('e6', (4, 37), ((4, 38.086), (5.345, 40), (6.582, 40)), ((7.545, 40), (8.045, 40), (9, 40)))
        self.add_bezier('e7', (42, 40), ((42.509, 39.621), (43.327, 39.225), (43.755, 38.754)), ((43.873, 38.627), (43.891, 38.135), (44, 38)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
