"""4m (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6323b2a3-5811-461c-8215-b5e860c35564'
SOURCE_PATH = 'icons-json/text/4m (text)_6323b2a3-5811-461c-8215-b5e860c35564.json'
AUTHOR = 'json_to_solo'

class Icon4mTextText(Solo48):
    icon_id = 'icon-4m-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('4m', 'text')

    def build(self):
        self.add_line('e0', (16, 33), (4, 33))
        self.add_line('e1', (4, 33), (14, 8))
        self.add_line('e2', (14, 8), (14, 40))
        self.add_line('e3', (24, 40), (28, 9))
        self.add_line('e4', (29, 9), (33, 33))
        self.add_line('e5', (34, 33), (39, 9))
        self.add_line('e6', (40, 11), (44, 40))
        self.add_line('e7-1', (28, 9), (29, 8))
        self.add_line('e7-2', (29, 8), (29, 9))
        self.add_arc('e8', (33, 33), (34, 33), radius_x=1, sweep=False)
        self.add_line('e9-1', (39, 9), (39, 8))
        self.add_arc('e9-2', (39, 8), (40, 11), radius_x=3)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e7-1', 'e7-2', 'e4', 'e8', 'e5', 'e9-1', 'e9-2', 'e6')
