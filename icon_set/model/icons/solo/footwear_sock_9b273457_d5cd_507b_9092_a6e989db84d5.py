"""Footwear sock (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b273457-d5cd-507b-9092-a6e989db84d5'
SOURCE_PATH = 'icons-json/clothes/footwear sock_9b273457-d5cd-507b-9092-a6e989db84d5.json'
AUTHOR = 'json_to_solo'

class FootwearSock(Solo48):
    icon_id = 'footwear-sock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('footwear', 'sock', 'clothes')

    def build(self):
        self.add_line('e0', (26, 4), (26, 16))
        self.add_line('e1', (27, 21), (32, 32))
        self.add_line('e2', (33, 44), (31, 44))
        self.add_line('e3', (16, 31), (11, 29))
        self.add_line('e4', (11, 13), (11, 4))
        self.add_line('e5', (11, 4), (26, 4))
        self.add_bezier('e6', (26, 16), ((26, 18.055), (26.175, 19.218), (27, 21)))
        self.add_bezier('e7', (32, 32), ((32.472, 33.018), (33.735, 34.009), (34.619, 34.582)), ((36.328, 35.7), (40, 36.709), (40, 39.491)), ((40, 39.493), (40, 39.495), (40, 39.498)), ((40, 39.641), (39.991, 39.775), (39.983, 39.909)), ((39.983, 41.873), (38.4, 43.391), (36.733, 43.818)), ((36, 44), (35.149, 43.982), (34.4, 43.982)), ((34.131, 43.982), (33.853, 44), (33.583, 44)), ((33.474, 44), (33.101, 44), (33, 44)))
        self.add_bezier('e8', (31, 44), ((29.863, 44), (28.362, 43.718), (27.293, 43.345)), ((24.076, 42.255), (22.484, 40.127), (20.573, 37.236)), ((19.318, 35.345), (18.08, 31.9), (16, 31)))
        self.add_bezier('e9', (11, 29), ((8.853, 28.073), (8, 25.882), (8, 23.482)), ((8, 23.479), (8, 23.476), (8, 23.474)), ((8, 23.304), (8.008, 23.134), (8.008, 22.964)), ((8.008, 22.264), (8.034, 21.491), (8.202, 20.818)), ((8.421, 19.955), (8.943, 19.155), (9.389, 18.427)), ((10.349, 16.836), (11, 14.973), (11, 13)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e5', closed=True)
