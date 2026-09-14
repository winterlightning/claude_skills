"""Download (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58449573-38e8-4aa0-bebb-14002004402f'
SOURCE_PATH = 'icons-json/arrows/download_58449573-38e8-4aa0-bebb-14002004402f.json'
AUTHOR = 'json_to_solo'

class Download(Solo48):
    icon_id = 'download'
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
        self.add_arc('e6-1', (4, 37), (7, 40), radius_x=3, sweep=False)
        self.add_arc('e6-2', (7, 40), (9, 40), radius_x=21)
        self.add_arc('e7', (42, 40), (44, 38), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
