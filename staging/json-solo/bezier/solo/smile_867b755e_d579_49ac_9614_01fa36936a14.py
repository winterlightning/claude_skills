"""Smile (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '867b755e-d579-49ac-9614-01fa36936a14'
SOURCE_PATH = 'icons-json/smileys/smile_867b755e-d579-49ac-9614-01fa36936a14.json'
AUTHOR = 'json_to_solo'

class Smile(Solo48):
    icon_id = 'smile'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('smile', 'smileys')

    def build(self):
        self.add_line('e0', (14, 20), (15, 19))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e2', (15, 19), ((17.336, 16.545), (19.409, 16.791), (20, 20)))
        self.add_bezier('e3', (28, 19), ((28.136, 18.318), (27.873, 18.127), (28.309, 17.555)), ((29.791, 15.582), (32.764, 16.064), (33.755, 18.245)), ((33.936, 18.636), (33.936, 18.591), (34, 19)))
        self.add_bezier('e4', (14, 29), ((14.555, 30.009), (15.136, 30.482), (15.955, 31.3)), ((19.891, 35.227), (26.8, 35.627), (31.173, 32.173)), ((32.427, 31.173), (33.273, 30.409), (34, 29)))
        self.add_contour('c0', 'e0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
