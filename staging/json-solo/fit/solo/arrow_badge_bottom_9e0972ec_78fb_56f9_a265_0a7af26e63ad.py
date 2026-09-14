"""Arrow badge bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e0972ec-78fb-56f9-a265-0a7af26e63ad'
SOURCE_PATH = 'icons-json/arrows/arrow badge bottom_9e0972ec-78fb-56f9-a265-0a7af26e63ad.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeBottom9e0972ec(Solo48):
    icon_id = 'arrow-badge-bottom-9e0972ec'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (8, 31), (8, 7))
        self.add_line('e1', (39, 32), (24, 44))
        self.add_line('e2', (24, 44), (8, 31))
        self.add_line('e3-1', (8, 7), (8, 6))
        self.add_line('e3-2', (8, 6), (11, 4))
        self.add_line('e3-3', (11, 4), (33, 4))
        self.add_line('e3-4', (33, 4), (38, 4))
        self.add_line('e3-5', (38, 4), (40, 7))
        self.add_line('e3-6', (40, 7), (40, 29))
        self.add_line('e3-7', (40, 29), (39, 32))
        self.add_contour('c0', 'e2', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e1', closed=True)
