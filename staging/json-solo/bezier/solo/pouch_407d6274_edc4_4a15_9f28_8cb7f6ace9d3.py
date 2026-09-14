"""Pouch (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '407d6274-edc4-4a15-9f28-8cb7f6ace9d3'
SOURCE_PATH = 'icons-json/video-games/pouch_407d6274-edc4-4a15-9f28-8cb7f6ace9d3.json'
AUTHOR = 'json_to_solo'

class Pouch407d6274(Solo48):
    icon_id = 'pouch-407d6274'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pouch', 'video-games')

    def build(self):
        self.add_line('sym-e0', (24, 13), (25, 13))
        self.add_line('sym-e1', (25, 13), (29, 13))
        self.add_bezier('sym-e2', (29, 13), ((30.255, 13.709), (31.922, 15), (33, 16)))
        self.add_bezier('sym-e3', (33, 16), ((37.042, 19.745), (40, 26.191), (40, 32)))
        self.add_bezier('sym-e4', (40, 32), ((40, 32.191), (40, 32.809), (40, 33)))
        self.add_bezier('sym-e5', (40, 33), ((40, 33.255), (40, 33.736), (40, 34)))
        self.add_bezier('sym-e6', (40, 34), ((40, 37.255), (38.577, 40.164), (36, 42)))
        self.add_bezier('sym-e7', (36, 42), ((34.375, 43.155), (31.92, 44), (30, 44)))
        self.add_bezier('sym-e8', (30, 44), ((29.739, 44), (29.269, 44), (29, 44)))
        self.add_bezier('sym-e9', (29, 44), ((28.596, 44), (28.404, 44), (28, 44)))
        self.add_bezier('sym-e10', (28, 44), ((26.576, 44), (25.422, 44), (24, 44)))
        self.add_bezier('sym-e11', (24, 44), ((22.578, 44), (21.424, 44), (20, 44)))
        self.add_bezier('sym-e12', (20, 44), ((19.596, 44), (19.404, 44), (19, 44)))
        self.add_bezier('sym-e13', (19, 44), ((18.731, 44), (18.261, 44), (18, 44)))
        self.add_bezier('sym-e14', (18, 44), ((16.08, 44), (13.625, 43.155), (12, 42)))
        self.add_bezier('sym-e15', (12, 42), ((9.423, 40.164), (8, 37.255), (8, 34)))
        self.add_bezier('sym-e16', (8, 34), ((8, 33.736), (8, 33.255), (8, 33)))
        self.add_bezier('sym-e17', (8, 33), ((8, 32.809), (8, 32.191), (8, 32)))
        self.add_bezier('sym-e18', (8, 32), ((8, 26.191), (10.958, 19.745), (15, 16)))
        self.add_bezier('sym-e19', (15, 16), ((16.078, 15), (17.745, 13.709), (19, 13)))
        self.add_line('sym-e20', (19, 13), (23, 13))
        self.add_line('sym-e21', (23, 13), (24, 13))
        self.add_line('sym-e22', (27, 15), (25, 13))
        self.add_bezier('sym-e23', (29, 13), ((29.876, 11.473), (31.705, 8.718), (32, 7)))
        self.add_bezier('sym-e24', (32, 7), ((32.253, 5.555), (31.398, 4), (30, 4)))
        self.add_bezier('sym-e25', (30, 4), ((29.815, 4), (29.177, 4), (29, 4)))
        self.add_bezier('sym-e26', (29, 4), ((28.335, 4), (27.657, 4), (27, 4)))
        self.add_line('sym-e27', (27, 4), (24, 4))
        self.add_line('sym-e28', (24, 4), (21, 4))
        self.add_bezier('sym-e29', (21, 4), ((20.343, 4), (19.665, 4), (19, 4)))
        self.add_bezier('sym-e30', (19, 4), ((18.823, 4), (18.185, 4), (18, 4)))
        self.add_bezier('sym-e31', (18, 4), ((16.602, 4), (15.747, 5.555), (16, 7)))
        self.add_bezier('sym-e32', (16, 7), ((16.295, 8.718), (18.124, 11.473), (19, 13)))
        self.add_line('sym-e33', (21, 15), (23, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
        self.add_contour('sym-c1', 'sym-e22')
        self.add_contour('sym-c2', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32')
        self.add_contour('sym-c3', 'sym-e33')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
