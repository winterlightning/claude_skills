"""Arrow badge top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '466b0701-7c09-52f1-bd1d-9f1f576f28f7'
SOURCE_PATH = 'icons-json/arrows/arrow badge top_466b0701-7c09-52f1-bd1d-9f1f576f28f7.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeTopArrows(Solo48):
    icon_id = 'arrow-badge-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (9, 16), (24, 4))
        self.add_line('e1', (40, 17), (40, 41))
        self.add_line('e2', (24, 4), (40, 17))
        self.add_line('e3-1', (40, 41), (40, 42))
        self.add_line('e3-2', (40, 42), (37, 44))
        self.add_line('e3-3', (37, 44), (15, 44))
        self.add_arc('e3-4', (15, 44), (10, 44), radius_x=67, sweep=False)
        self.add_line('e3-5', (10, 44), (8, 41))
        self.add_line('e3-6', (8, 41), (8, 19))
        self.add_line('e3-7', (8, 19), (9, 16))
        self.add_contour('c0', 'e0', 'e2', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', closed=True)
