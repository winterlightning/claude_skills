"""Curvy both direction large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc11795e-9c7b-4522-995a-d02107828f81'
SOURCE_PATH = 'icons-json/arrows/curvy both direction large head_fc11795e-9c7b-4522-995a-d02107828f81.json'
AUTHOR = 'json_to_solo'

class CurvyBothDirectionLargeHead(Solo48):
    icon_id = 'curvy-both-direction-large-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curvy', 'both', 'direction', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (36, 6), (42, 12))
        self.add_line('e1', (11, 32), (6, 37))
        self.add_line('e2', (11, 42), (6, 37))
        self.add_line('e3', (36, 17), (42, 12))
        self.add_line('e4', (42, 12), (20, 12))
        self.add_line('e5', (20, 24), (24, 24))
        self.add_line('e6', (25, 37), (6, 37))
        self.add_bezier('e7', (20, 12), ((19.305, 12), (18.224, 12.235), (17.635, 12.586)), ((13.887, 14.82), (13.585, 20.498), (17.209, 23.01)), ((17.97, 23.534), (19.051, 24), (20, 24)))
        self.add_bezier('e8', (24, 24), ((28.189, 24), (30.685, 28.606), (29.858, 32.354)), ((29.392, 34.448), (27.715, 36.265), (25.661, 36.886)), ((25.415, 36.96), (25.254, 37), (25, 37)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e7', 'e5', 'e8', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
