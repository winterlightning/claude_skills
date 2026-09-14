"""M (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c3e4fcf-81eb-41b6-a780-33d760b0dd64'
SOURCE_PATH = 'icons-json/typeface/M_2c3e4fcf-81eb-41b6-a780-33d760b0dd64.json'
AUTHOR = 'json_to_solo'

class M2c3e4fcf(Solo48):
    icon_id = 'm-2c3e4fcf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('m', 'typeface')

    def build(self):
        self.add_line('sym-e0', (6, 42), (13, 9))
        self.add_bezier('sym-e1', (13, 9), ((13.18, 8.084), (13.74, 6), (15, 6)))
        self.add_bezier('sym-e2', (15, 6), ((15.065, 6), (14.943, 6), (15, 6)))
        self.add_bezier('sym-e3', (15, 6), ((15.057, 6.008), (14.943, 6), (15, 6)))
        self.add_bezier('sym-e4', (15, 6), ((16.857, 6), (16.697, 9.797), (17, 11)))
        self.add_line('sym-e5', (17, 11), (23, 34))
        self.add_bezier('sym-e6', (23, 34), ((23.074, 34.074), (22.926, 33.91), (23, 34)))
        self.add_bezier('sym-e7', (23, 34), ((23.164, 34.2), (23.755, 35), (24, 35)))
        self.add_bezier('sym-e8', (24, 35), ((24.245, 35), (24.836, 34.2), (25, 34)))
        self.add_bezier('sym-e9', (25, 34), ((25.074, 33.91), (24.926, 34.074), (25, 34)))
        self.add_line('sym-e10', (25, 34), (31, 11))
        self.add_bezier('sym-e11', (31, 11), ((31.303, 9.797), (31.143, 6), (33, 6)))
        self.add_bezier('sym-e12', (33, 6), ((33.057, 6), (32.943, 6.008), (33, 6)))
        self.add_bezier('sym-e13', (33, 6), ((33.057, 6), (32.935, 6), (33, 6)))
        self.add_bezier('sym-e14', (33, 6), ((34.26, 6), (34.82, 8.084), (35, 9)))
        self.add_line('sym-e15', (35, 9), (42, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
