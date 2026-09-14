"""Video (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '063ab342-3eb9-4c77-b5e5-59de1a294e59'
SOURCE_PATH = 'icons-json/state/video_063ab342-3eb9-4c77-b5e5-59de1a294e59.json'
AUTHOR = 'json_to_solo'

class Video063ab342(Solo48):
    icon_id = 'video-063ab342'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('video', 'state')

    def build(self):
        self.add_line('e0', (33, 19), (44, 13))
        self.add_line('e1', (44, 13), (44, 35))
        self.add_line('e2', (44, 35), (33, 29))
        self.add_line('e3', (29, 40), (9, 40))
        self.add_line('e4', (4, 33), (4, 15))
        self.add_line('e5', (10, 8), (28, 8))
        self.add_line('e6', (33, 14), (33, 29))
        self.add_bezier('e7', (33, 29), ((33, 33), (33.291, 35.902), (30.791, 38.658)), ((30.245, 39.249), (29.718, 40), (29, 40)))
        self.add_bezier('e8', (9, 40), ((8.782, 40), (9.009, 39.975), (8.791, 39.975)), ((6.491, 39.975), (4.009, 36.96), (4.009, 33.772)), ((4.009, 33.588), (4, 33.391), (4, 33.194)), ((4, 33.009), (4, 33.197), (4, 33)))
        self.add_bezier('e9', (4, 15), ((4, 14.791), (4.009, 14.954), (4.009, 14.745)), ((4.009, 10.905), (6.227, 8.025), (9.036, 8.025)), ((9.345, 8.025), (9.655, 8), (9.973, 8)), ((10.1, 8), (9.873, 8), (10, 8)))
        self.add_bezier('e10', (28, 8), ((28.173, 8), (27.982, 8.025), (28.155, 8.025)), ((30.364, 8.025), (32.3, 10.154), (32.882, 12.985)), ((32.945, 13.329), (33, 13.643), (33, 14)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
