"""Paddle board (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97cda55a-4e3a-4bc4-b593-5316283a391c'
SOURCE_PATH = 'icons-json/outdoors/paddle board_97cda55a-4e3a-4bc4-b593-5316283a391c.json'
AUTHOR = 'json_to_solo'

class PaddleBoardOutdoors(Solo48):
    icon_id = 'paddle-board-outdoors'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('paddle', 'board', 'outdoors')

    def build(self):
        self.add_line('e0', (32, 4), (35, 4))
        self.add_line('e1', (38, 4), (35, 4))
        self.add_line('e2', (35, 29), (35, 4))
        self.add_line('e3', (16, 4), (15, 6))
        self.add_line('e4', (14, 44), (19, 44))
        self.add_bezier('e5', (35, 29), ((32.5, 32.336), (30.38, 35.282), (30.16, 39.418)), ((30.04, 41.718), (30.72, 43.991), (33.78, 43.991)), ((33.85, 43.991), (33.91, 44), (33.98, 44)), ((34.31, 44), (34.64, 43.982), (34.97, 43.982)), ((37.23, 43.982), (39.99, 43.473), (39.99, 40.855)), ((39.99, 40.792), (40, 40.738), (40, 40.676)), ((40, 40.675), (40, 40.674), (40, 40.673)), ((40, 40.418), (39.99, 40.173), (39.99, 39.918)), ((39.99, 35.645), (37.68, 32.345), (35, 29)))
        self.add_bezier('e6', (15, 6), ((10.38, 11.555), (8.02, 18.409), (8.02, 25.373)), ((8.02, 25.561), (8, 25.74), (8, 25.927)), ((8, 25.93), (8, 25.933), (8, 25.936)), ((8, 26.427), (8.02, 26.918), (8.02, 27.409)), ((8.02, 31.355), (9.38, 35.409), (10.69, 39.127)), ((11.24, 40.664), (11.65, 43), (13.38, 43.836)), ((13.58, 43.927), (13.8, 43.918), (14, 44)))
        self.add_bezier('e7', (19, 44), ((19.82, 44), (20.58, 43.436), (21.05, 42.882)), ((22.26, 41.445), (23.6, 37.364), (24.14, 35.582)), ((26.61, 27.5), (26.05, 18.682), (22.39, 10.936)), ((21.46, 8.991), (20.27, 7.155), (18.8, 5.509)), ((18.2, 4.836), (17.54, 4.018), (16.52, 4.018)), ((16.45, 4.009), (16.38, 4.009), (16.31, 4)), ((16.21, 4), (16.1, 4), (16, 4)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5', closed=True)
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e6', 'e4', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
