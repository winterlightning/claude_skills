"""Curve rise large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd13c23c-99cd-4dd8-932b-e39c965b1587'
SOURCE_PATH = 'icons-json/arrows/curve rise large head_dd13c23c-99cd-4dd8-932b-e39c965b1587.json'
AUTHOR = 'json_to_solo'

class CurveRiseLargeHead(Solo48):
    icon_id = 'curve-rise-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'rise', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (18, 17), (18, 30))
        self.add_line('e1', (37, 29), (37, 8))
        self.add_line('e2', (44, 18), (37, 8))
        self.add_line('e3', (29, 18), (37, 8))
        self.add_bezier('e4', (4, 10), ((5.455, 8.351), (7.064, 8.025), (8.991, 8.025)), ((9.3, 8.025), (9.609, 8), (9.918, 8)), ((10.345, 8), (10.782, 8.025), (11.209, 8.025)), ((14.227, 8.025), (16.736, 10.818), (17.355, 14.794)), ((17.436, 15.335), (18, 16.495), (18, 17)))
        self.add_bezier('e5', (18, 30), ((18, 30.505), (17.909, 31.569), (18.045, 32.086)), ((19.3, 36.8), (23.082, 39.988), (26.745, 39.988)), ((26.808, 39.988), (26.871, 40), (26.933, 40)), ((26.934, 40), (26.935, 40), (26.936, 40)), ((27.218, 40), (27.509, 39.988), (27.791, 39.988)), ((31.555, 39.988), (34.882, 36.603), (36.2, 31.914)), ((36.445, 31.015), (37, 29.972), (37, 29)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
