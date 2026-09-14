"""Disability q (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04780cbf-d786-5114-97e7-065fa73b45c2'
SOURCE_PATH = 'icons-json/typeface/disability q_04780cbf-d786-5114-97e7-065fa73b45c2.json'
AUTHOR = 'json_to_solo'

class DisabilityQTypeface(Solo48):
    icon_id = 'disability-q-typeface'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('disability', 'q', 'typeface')

    def build(self):
        self.add_line('e0', (31, 30), (37, 36))
        self.add_line('e1', (29, 7), (25, 6))
        self.add_line('e2', (37, 36), (42, 41))
        self.add_bezier('e3', (37, 36), ((39.471, 33.292), (40.895, 30.464), (41.607, 26.888)), ((41.763, 26.119), (41.992, 25.309), (41.992, 24.515)), ((41.992, 24.393), (42, 24.27), (42, 24.139)), ((42, 24.016), (41.992, 23.885), (41.992, 23.763)), ((41.992, 22.838), (41.738, 21.873), (41.55, 20.973)), ((40.388, 15.466), (37.492, 10.95), (32.435, 8.25)), ((31.372, 7.685), (30.195, 7.237), (29, 7)))
        self.add_bezier('e4', (25, 6), ((24.149, 6), (23.116, 6.016), (22.265, 6.016)), ((20.678, 6.016), (18.927, 6.605), (17.471, 7.186)), ((10.786, 9.87), (6.008, 16.44), (6.008, 23.746)), ((6.008, 23.819), (6, 23.883), (6, 23.956)), ((6, 23.957), (6, 23.958), (6, 23.959)), ((6, 31.846), (10.999, 38.891), (18.608, 41.206)), ((19.975, 41.624), (21.488, 41.992), (22.92, 41.992)), ((23.194, 41.992), (23.46, 42), (23.726, 42)), ((23.73, 42), (23.734, 42), (23.738, 42)), ((24.074, 42), (24.409, 41.984), (24.745, 41.984)), ((29.547, 41.984), (33.662, 39.248), (37, 36)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2')
