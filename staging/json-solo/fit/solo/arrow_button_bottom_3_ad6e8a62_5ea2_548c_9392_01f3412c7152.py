"""Arrow button bottom 3 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad6e8a62-5ea2-548c-9392-01f3412c7152'
SOURCE_PATH = 'icons-json/arrows/arrow button bottom 3_ad6e8a62-5ea2-548c-9392-01f3412c7152.json'
AUTHOR = 'json_to_solo'

class ArrowButtonBottom3Arrows(Solo48):
    icon_id = 'arrow-button-bottom-3-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 40))
        self.add_arc('sym-e1', (24, 40), (27, 38), radius_x=4, sweep=False)
        self.add_line('sym-e2', (27, 38), (43, 22))
        self.add_line('sym-e3', (43, 22), (44, 21))
        self.add_arc('sym-e4', (44, 21), (44, 20), radius_x=26)
        self.add_arc('sym-e5', (44, 20), (44, 19), radius_x=26)
        self.add_line('sym-e6', (44, 19), (44, 8))
        self.add_line('sym-e7', (44, 8), (25, 27))
        self.add_arc('sym-e8', (25, 27), (24, 27), radius_x=1, sweep=False)
        self.add_arc('sym-e9', (24, 27), (23, 27), radius_x=1, sweep=False)
        self.add_line('sym-e10', (23, 27), (4, 8))
        self.add_line('sym-e11', (4, 8), (4, 19))
        self.add_line('sym-e12', (4, 19), (4, 20))
        self.add_line('sym-e13', (4, 20), (4, 21))
        self.add_line('sym-e14', (4, 21), (5, 22))
        self.add_line('sym-e15', (5, 22), (21, 38))
        self.add_arc('sym-e16', (21, 38), (24, 40), radius_x=4, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
