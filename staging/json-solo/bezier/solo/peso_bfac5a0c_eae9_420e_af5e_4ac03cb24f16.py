"""Peso (money), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfac5a0c-eae9-420e-af5e-4ac03cb24f16'
SOURCE_PATH = 'icons-json/money/peso_bfac5a0c-eae9-420e-af5e-4ac03cb24f16.json'
AUTHOR = 'json_to_solo'

class PesoBfac5a0c(Solo48):
    icon_id = 'peso-bfac5a0c'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('peso', 'money')

    def build(self):
        self.add_line('e0', (6, 24), (32, 24))
        self.add_line('e1', (23, 6), (14, 6))
        self.add_line('e2', (14, 6), (14, 42))
        self.add_bezier('e3', (32, 24), ((35.42, 24), (38.997, 22.666), (40.895, 19.713)), ((41.534, 18.731), (41.992, 17.479), (41.992, 16.301)), ((41.992, 16.18), (42, 16.059), (42, 15.938)), ((42, 15.937), (42, 15.935), (42, 15.933)), ((42, 15.81), (41.992, 15.687), (41.992, 15.565)), ((41.992, 14.19), (41.354, 12.766), (40.666, 11.613)), ((38.768, 8.438), (35.414, 6.605), (31.814, 6.106)), ((30.783, 6), (29.686, 6.016), (28.647, 6.016)), ((27.747, 6.016), (26.847, 6), (25.939, 6)), ((25.023, 6), (23.916, 6), (23, 6)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e2')
