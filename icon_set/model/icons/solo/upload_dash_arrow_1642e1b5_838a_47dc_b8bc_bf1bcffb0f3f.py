"""Upload dash arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1642e1b5-838a-47dc-b8bc-bf1bcffb0f3f'
SOURCE_PATH = 'icons-json/arrows/upload dash arrow_1642e1b5-838a-47dc-b8bc-bf1bcffb0f3f.json'
AUTHOR = 'json_to_solo'

class UploadDashArrow(Solo48):
    icon_id = 'upload-dash-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('upload', 'dash', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (17, 33), (17, 17))
        self.add_line('e1', (17, 17), (8, 17))
        self.add_line('e2', (8, 17), (24, 4))
        self.add_line('e3', (24, 4), (40, 17))
        self.add_line('e4', (40, 17), (31, 17))
        self.add_line('e5', (31, 17), (31, 33))
        self.add_line('e6', (24, 44), (24, 29))
        self.add_line('e7', (17, 40), (17, 38))
        self.add_line('e8', (31, 38), (31, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e8')
