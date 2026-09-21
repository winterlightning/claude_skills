"""S (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3aec2c5-6aaa-5b86-a70b-961ba1dd9315'
SOURCE_PATH = 'icons-json/typeface/S_c3aec2c5-6aaa-5b86-a70b-961ba1dd9315.json'
AUTHOR = 'json_to_solo'

class S(Solo48):
    icon_id = 's'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('s', 'typeface')

    def build(self):
        self.add_line('e0', (28, 24), (18, 21))
        self.add_line('e1', (34, 7), (39, 9))
        self.add_bezier('e2', (8, 39), ((12.012, 42.236), (17.649, 44), (23.754, 44)), ((23.76, 44), (23.767, 44), (23.773, 44)), ((24.173, 44), (24.585, 43.982), (24.985, 43.982)), ((32.357, 43.982), (39.975, 40.409), (39.975, 34.445)), ((39.988, 34.374), (40, 34.293), (40, 34.222)), ((40, 34.22), (40, 34.219), (40, 34.218)), ((39.988, 34.073), (39.988, 33.927), (39.975, 33.782)), ((39.975, 28.645), (33.785, 25.6), (28, 24)))
        self.add_bezier('e3', (18, 21), ((17.335, 20.818), (16.517, 20.718), (15.902, 20.455)), ((12.849, 19.127), (10.018, 17.3), (9.452, 14.564)), ((8.492, 9.936), (12.726, 5.836), (18.548, 4.5)), ((19.68, 4.236), (20.825, 4.009), (22.031, 4.009)), ((22.225, 4.009), (22.418, 4), (22.612, 4)), ((22.615, 4), (22.618, 4), (22.622, 4)), ((22.818, 4), (23.015, 4.009), (23.212, 4.009)), ((25.329, 4.009), (27.84, 4.536), (29.772, 5.182)), ((31.237, 5.673), (32.326, 6.545), (34, 7)))
        self.add_contour('c0', 'e2', 'e0', 'e3', 'e1')
