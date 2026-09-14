"""Presentation speaker (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d0aa5c2-2cb9-4e78-a384-0a6db82a73dd'
SOURCE_PATH = 'icons-json/office/presentation speaker_3d0aa5c2-2cb9-4e78-a384-0a6db82a73dd.json'
AUTHOR = 'json_to_solo'

class PresentationSpeakerOffice(Solo48):
    icon_id = 'presentation-speaker-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'speaker', 'office')

    def build(self):
        self.add_arc('sym-e0', (19, 19), (29, 19), radius_x=5, radius_y=4)
        self.add_arc('sym-e1', (29, 19), (19, 19), radius_x=5, radius_y=4)
        self.add_line('sym-e2', (18, 40), (17, 33))
        self.add_line('sym-e3', (17, 33), (31, 33))
        self.add_line('sym-e4', (31, 33), (30, 40))
        self.add_line('sym-e5', (24, 8), (42, 8))
        self.add_bezier('sym-e6', (42, 8), ((42.191, 8.076), (42.809, 8), (43, 8)))
        self.add_bezier('sym-e7', (43, 8), ((43.736, 8.371), (43.7, 9.352), (44, 10)))
        self.add_line('sym-e8', (44, 10), (44, 28))
        self.add_bezier('sym-e9', (44, 28), ((43.918, 28.168), (44, 28.832), (44, 29)))
        self.add_bezier('sym-e10', (44, 29), ((43.618, 29.657), (42.664, 29.697), (42, 30)))
        self.add_line('sym-e11', (42, 30), (37, 30))
        self.add_bezier('sym-e12', (24, 26), ((24.009, 26), (23.991, 26), (24, 26)))
        self.add_bezier('sym-e13', (24, 26), ((26.409, 26), (28.436, 26.038), (30, 28)))
        self.add_bezier('sym-e14', (30, 28), ((31.165, 29.458), (31, 31.283), (31, 33)))
        self.add_bezier('sym-e15', (31, 33), ((31, 33.038), (31, 32.962), (31, 33)))
        self.add_line('sym-e16', (31, 33), (34, 33))
        self.add_line('sym-e17', (24, 8), (6, 8))
        self.add_bezier('sym-e18', (6, 8), ((5.809, 8.076), (5.191, 8), (5, 8)))
        self.add_bezier('sym-e19', (5, 8), ((4.264, 8.371), (4.3, 9.352), (4, 10)))
        self.add_line('sym-e20', (4, 10), (4, 28))
        self.add_bezier('sym-e21', (4, 28), ((4.082, 28.168), (4, 28.832), (4, 29)))
        self.add_bezier('sym-e22', (4, 29), ((4.382, 29.657), (5.336, 29.697), (6, 30)))
        self.add_line('sym-e23', (6, 30), (11, 30))
        self.add_bezier('sym-e24', (24, 26), ((23.991, 26), (24.009, 26), (24, 26)))
        self.add_bezier('sym-e25', (24, 26), ((21.591, 26), (19.564, 26.038), (18, 28)))
        self.add_bezier('sym-e26', (18, 28), ((16.835, 29.458), (17, 31.283), (17, 33)))
        self.add_bezier('sym-e27', (17, 33), ((17, 33.038), (17, 32.962), (17, 33)))
        self.add_line('sym-e28', (17, 33), (14, 33))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c3', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c4', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.add_contour('sym-c5', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c5')
