"""Double arrow 1 right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd05d19d9-976f-5079-b944-bcc8f10a2b2b'
SOURCE_PATH = 'icons-json/arrows/double arrow 1 right_d05d19d9-976f-5079-b944-bcc8f10a2b2b.json'
AUTHOR = 'json_to_solo'

class DoubleArrow1Right(Solo48):
    icon_id = 'double-arrow-1-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'right', 'arrows')

    def build(self):
        self.add_line('sym-e0', (29, 8), (44, 24))
        self.add_line('sym-e1', (44, 24), (29, 40))
        self.add_line('sym-e2', (14, 8), (29, 24))
        self.add_line('sym-e3', (29, 24), (14, 40))
        self.add_line('sym-e4', (4, 24), (29, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.relate('connect', 'sym-c1', 'sym-c2')
