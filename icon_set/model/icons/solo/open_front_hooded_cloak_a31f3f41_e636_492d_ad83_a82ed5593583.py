"""Open-front cloak with a rounded hood, teardrop opening and parted panels.
VRECT_L (8,4)..(40,44) gives a narrow hood above broader flared panels.
Mirror panels around x=24; use shared neckline and hem attachment nodes.
Reference supplies hood opening and split front; omit the tiny neck fastener.
Lucide shirt informs a single garment silhouette with explicit neck geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a31f3f41-e636-492d-ad83-a82ed5593583'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/cloak_a31f3f41-e636-492d-ad83-a82ed5593583.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'open-front-hooded-cloak'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Hooded Cloak Garment']
    keywords = ['cloak','hood','garment','cape','clothing','panels','outerwear']
    def build(self):
        axis = 24
        mirror = lambda point: (2 * axis - point[0], point[1])
        neckline = (axis, 24)
        left_hem = (16, 44)
        left_body = [left_hem, (8, 44), (12, 28), (14, 24)]
        left_hood = [left_body[-1], (12, 23), (10, 21), (10, 18)]
        left_opening = [neckline, (22, 22), (20, 19), (20, 16)]
        left_panel = [left_hem, (22, 37), (axis, 30), neckline]

        def curve(name, points):
            self.add_bezier(name, points[0], tuple(points[1:]))

        self.add_polyline('body-left', *left_body)
        curve('hood-left', left_hood)
        self.add_arc('hood-top', left_hood[-1], mirror(left_hood[-1]), radius_x=14, radius_y=14)
        curve('hood-right', [mirror(p) for p in reversed(left_hood)])
        self.add_polyline('body-right', *[mirror(p) for p in reversed(left_body)], left_hem)
        curve('opening-left', left_opening)
        self.add_arc('opening-top', left_opening[-1], mirror(left_opening[-1]), radius_x=4)
        curve('opening-right', [mirror(p) for p in reversed(left_opening)])
        self.add_contour('opening', 'opening-left', 'opening-top', 'opening-right', closed=True)
        curve('panel-left', left_panel)
        curve('panel-right', [mirror(p) for p in reversed(left_panel)])
        contacts = [
            ('body-left', 'hood-left'), ('hood-left', 'hood-top'),
            ('hood-top', 'hood-right'), ('hood-right', 'body-right'),
            ('body-right', 'body-left'), ('panel-left', 'opening'),
            ('panel-right', 'opening'), ('panel-left', 'panel-right'),
            ('body-left', 'panel-left'), ('body-right', 'panel-left'),
            ('body-right', 'panel-right'),
        ]
        for first, second in contacts:
            self.relate('connect', first, second)
