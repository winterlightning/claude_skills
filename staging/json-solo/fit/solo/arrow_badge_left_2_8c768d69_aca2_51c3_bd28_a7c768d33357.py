"""Arrow badge left 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c768d69-aca2-51c3-bd28-a7c768d33357'
SOURCE_PATH = 'icons-json/arrows/arrow badge left 2_8c768d69-aca2-51c3-bd28-a7c768d33357.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeLeft2Arrows(Solo48):
    icon_id = 'arrow-badge-left-2-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'left', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 16), (17, 24))
        self.add_line('sym-e1', (17, 24), (24, 32))
        self.add_arc('sym-e3', (4, 24), (6, 28), radius_x=5, sweep=False)
        self.add_line('sym-e4', (6, 28), (17, 39))
        self.add_line('sym-e5', (17, 39), (19, 40))
        self.add_line('sym-e6', (19, 40), (42, 40))
        self.add_line('sym-e7', (42, 40), (44, 39))
        self.add_line('sym-e8', (44, 39), (44, 38))
        self.add_line('sym-e9', (44, 38), (44, 24))
        self.add_line('sym-e10', (44, 24), (44, 10))
        self.add_arc('sym-e11', (44, 10), (44, 9), radius_x=1)
        self.add_line('sym-e12', (44, 9), (42, 8))
        self.add_line('sym-e13', (42, 8), (19, 8))
        self.add_line('sym-e14', (19, 8), (17, 9))
        self.add_line('sym-e15', (17, 9), (6, 20))
        self.add_arc('sym-e16', (6, 20), (4, 24), radius_x=5, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
