"""Download bottom (internet), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '420aaab1-7942-44fa-a853-3e16edd896fd'
SOURCE_PATH = 'icons-json/internet/download bottom_420aaab1-7942-44fa-a853-3e16edd896fd.json'
AUTHOR = 'json_to_solo'

class DownloadBottomInternet(Solo48):
    icon_id = 'download-bottom-internet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('download', 'bottom', 'internet')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 34))
        self.add_line('sym-e1', (24, 34), (35, 23))
        self.add_line('sym-e2', (24, 42), (38, 42))
        self.add_arc('sym-e4', (38, 42), (42, 37), radius_x=6, sweep=False)
        self.add_line('sym-e5', (42, 37), (42, 34))
        self.add_line('sym-e6', (13, 23), (24, 34))
        self.add_line('sym-e7', (24, 42), (10, 42))
        self.add_arc('sym-e9', (10, 42), (6, 37), radius_x=6)
        self.add_line('sym-e10', (6, 37), (6, 34))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
