"""Arrow badge right 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bdeb55d-f637-54d7-ae3a-b56165d08c04'
SOURCE_PATH = 'icons-json/arrows/arrow badge right 2_9bdeb55d-f637-54d7-ae3a-b56165d08c04.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeRight2Arrows(Solo48):
    icon_id = 'arrow-badge-right-2-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'right', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 32), (31, 24))
        self.add_line('sym-e1', (31, 24), (24, 16))
        self.add_bezier('sym-e2', (44, 24), ((44, 23.99), (44, 24.01), (44, 24)))
        self.add_bezier('sym-e3', (44, 24), ((44, 22.25), (43.155, 21.16), (42, 20)))
        self.add_line('sym-e4', (42, 20), (31, 9))
        self.add_bezier('sym-e5', (31, 9), ((30.536, 8.53), (29.664, 8), (29, 8)))
        self.add_line('sym-e6', (29, 8), (6, 8))
        self.add_bezier('sym-e7', (6, 8), ((5.309, 8.3), (4.409, 8.23), (4, 9)))
        self.add_bezier('sym-e8', (4, 9), ((4, 9.22), (4.1, 9.77), (4, 10)))
        self.add_line('sym-e9', (4, 10), (4, 24))
        self.add_line('sym-e10', (4, 24), (4, 38))
        self.add_bezier('sym-e11', (4, 38), ((4.1, 38.23), (4, 38.78), (4, 39)))
        self.add_bezier('sym-e12', (4, 39), ((4.409, 39.77), (5.309, 39.7), (6, 40)))
        self.add_line('sym-e13', (6, 40), (29, 40))
        self.add_bezier('sym-e14', (29, 40), ((29.664, 40), (30.536, 39.47), (31, 39)))
        self.add_line('sym-e15', (31, 39), (42, 28))
        self.add_bezier('sym-e16', (42, 28), ((43.155, 26.84), (44, 25.75), (44, 24)))
        self.add_bezier('sym-e17', (44, 24), ((44, 23.99), (44, 24.01), (44, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
