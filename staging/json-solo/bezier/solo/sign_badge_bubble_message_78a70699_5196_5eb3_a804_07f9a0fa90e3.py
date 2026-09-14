"""Sign badge bubble message (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78a70699-5196-5eb3-a804-07f9a0fa90e3'
SOURCE_PATH = 'icons-json/maps/sign badge bubble message_78a70699-5196-5eb3-a804-07f9a0fa90e3.json'
AUTHOR = 'json_to_solo'

class SignBadgeBubbleMessageMaps(Solo48):
    icon_id = 'sign-badge-bubble-message-maps'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'bubble', 'message', 'maps')

    def build(self):
        self.add_line('e0', (15, 35), (10, 35))
        self.add_line('e1', (6, 29), (6, 10))
        self.add_line('e2', (11, 6), (37, 6))
        self.add_line('e3', (42, 9), (42, 30))
        self.add_line('e4', (33, 35), (25, 42))
        self.add_bezier('e5', (10, 35), ((7.775, 35), (6.016, 32.665), (6.016, 30.455)), ((6.016, 30.104), (6, 29.76), (6, 29.408)), ((6, 29.245), (6, 29.164), (6, 29)))
        self.add_bezier('e6', (6, 10), ((6, 9.869), (6.008, 9.829), (6.008, 9.698)), ((6.008, 8.225), (7.628, 6.016), (9.232, 6.016)), ((9.289, 6.008), (9.346, 6.008), (9.412, 6)), ((9.911, 6), (10.501, 6), (11, 6)))
        self.add_bezier('e7', (37, 6), ((37.18, 6), (37.459, 6.016), (37.639, 6.016)), ((39.316, 6.016), (42, 7.077), (42, 9)))
        self.add_bezier('e8', (42, 30), ((42, 30.188), (41.992, 30.104), (41.992, 30.292)), ((41.992, 31.102), (41.681, 31.904), (41.206, 32.55)), ((39.537, 34.874), (37.115, 34.301), (34.645, 34.375)), ((34.252, 34.391), (33.679, 34.317), (33.311, 34.456)), ((33.205, 34.497), (33.106, 34.975), (33, 35)))
        self.add_bezier('e9', (25, 42), ((24.82, 42), (24.458, 42), (24.286, 42)), ((23.951, 42), (23.607, 42), (23.272, 42)), ((22.118, 42), (21.153, 40.585), (20.465, 39.873)), ((18.723, 38.081), (17.013, 36.497), (15, 35)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
