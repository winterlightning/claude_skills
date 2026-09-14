"""Dash wave down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '811e8d54-369b-424d-a542-04d91cebc791'
SOURCE_PATH = 'icons-json/arrows/dash wave down large head_811e8d54-369b-424d-a542-04d91cebc791.json'
AUTHOR = 'json_to_solo'

class DashWaveDownLargeHeadArrows(Solo48):
    icon_id = 'dash-wave-down-large-head-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('dash', 'wave', 'down', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (12, 11), (12, 35))
        self.add_line('e1', (27, 35), (27, 11))
        self.add_line('e2', (38, 11), (38, 26))
        self.add_line('e3', (33, 22), (38, 26))
        self.add_line('e4', (42, 22), (38, 26))
        self.add_bezier('e5', (6, 6), ((6.303, 6), (6.614, 6.008), (6.916, 6.008)), ((9.142, 6.008), (11.04, 8.225), (11.531, 10.222)), ((11.58, 10.402), (12, 10.828), (12, 11)))
        self.add_bezier('e6', (12, 35), ((12, 35.385), (11.932, 35.585), (12.022, 35.962)), ((12.815, 39.112), (15.556, 41.992), (18.976, 41.992)), ((19.049, 41.992), (19.113, 42), (19.186, 42)), ((19.187, 42), (19.188, 42), (19.189, 42)), ((19.328, 42), (19.475, 41.992), (19.615, 41.992)), ((23.149, 41.992), (26.185, 39.071), (27.019, 35.765)), ((27.101, 35.438), (27, 35.327), (27, 35)))
        self.add_bezier('e7', (27, 11), ((27, 10.836), (27.412, 10.41), (27.461, 10.246)), ((28.009, 8.266), (30.267, 6.008), (32.452, 6.008)), ((32.525, 6.008), (32.599, 6), (32.673, 6)), ((32.746, 6), (32.82, 6), (32.894, 6.008)), ((35.127, 6.008), (38, 8.734), (38, 11)))
        self.add_bezier('e8', (42, 21), ((42, 21.27), (42, 21.73), (42, 22)))
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e8', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
