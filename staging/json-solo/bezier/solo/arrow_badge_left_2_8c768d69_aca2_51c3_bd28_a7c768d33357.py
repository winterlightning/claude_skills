"""Arrow badge left 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e2', (4, 24), ((4, 24.01), (4, 23.99), (4, 24)))
        self.add_bezier('sym-e3', (4, 24), ((4, 25.75), (4.845, 26.84), (6, 28)))
        self.add_line('sym-e4', (6, 28), (17, 39))
        self.add_bezier('sym-e5', (17, 39), ((17.464, 39.47), (18.336, 40), (19, 40)))
        self.add_line('sym-e6', (19, 40), (42, 40))
        self.add_bezier('sym-e7', (42, 40), ((42.691, 39.7), (43.591, 39.77), (44, 39)))
        self.add_bezier('sym-e8', (44, 39), ((44, 38.78), (43.9, 38.23), (44, 38)))
        self.add_line('sym-e9', (44, 38), (44, 24))
        self.add_line('sym-e10', (44, 24), (44, 10))
        self.add_bezier('sym-e11', (44, 10), ((43.9, 9.77), (44, 9.22), (44, 9)))
        self.add_bezier('sym-e12', (44, 9), ((43.591, 8.23), (42.691, 8.3), (42, 8)))
        self.add_line('sym-e13', (42, 8), (19, 8))
        self.add_bezier('sym-e14', (19, 8), ((18.336, 8), (17.464, 8.53), (17, 9)))
        self.add_line('sym-e15', (17, 9), (6, 20))
        self.add_bezier('sym-e16', (6, 20), ((4.845, 21.16), (4, 22.25), (4, 24)))
        self.add_bezier('sym-e17', (4, 24), ((4, 24.01), (4, 23.99), (4, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
