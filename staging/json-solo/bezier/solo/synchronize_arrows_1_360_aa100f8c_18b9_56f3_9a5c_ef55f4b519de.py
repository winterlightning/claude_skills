"""Synchronize arrows 1 360 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa100f8c-18b9-56f3-9a5c-ef55f4b519de'
SOURCE_PATH = 'icons-json/arrows/synchronize arrows 1 360_aa100f8c-18b9-56f3-9a5c-ef55f4b519de.json'
AUTHOR = 'json_to_solo'

class SynchronizeArrows1360Arrows(Solo48):
    icon_id = 'synchronize-arrows-1-360-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('synchronize', 'arrows')

    def build(self):
        self.add_line('e0', (17, 35), (11, 36))
        self.add_line('e1', (11, 36), (13, 42))
        self.add_line('e2', (35, 6), (37, 13))
        self.add_line('e3', (37, 13), (30, 13))
        self.add_bezier('e4', (41, 19), ((41.376, 20.334), (41.984, 21.963), (41.984, 23.362)), ((41.984, 23.566), (42, 23.771), (42, 23.975)), ((42, 23.979), (42, 23.982), (42, 23.985)), ((42, 24.178), (41.984, 24.379), (41.984, 24.573)), ((41.984, 26.512), (41.419, 28.565), (40.658, 30.333)), ((36.903, 39.071), (27.305, 42), (18.338, 40.372)), ((15.532, 39.554), (13.152, 37.996), (11, 36)))
        self.add_bezier('e5', (7, 29), ((6.575, 27.593), (6.016, 26.045), (6.016, 24.565)), ((6.016, 24.376), (6, 24.188), (6, 24)), ((6, 23.996), (6, 23.992), (6, 23.988)), ((6, 23.747), (6.008, 23.497), (6.008, 23.255)), ((6.008, 21.619), (6.425, 19.95), (6.957, 18.412)), ((9.657, 10.672), (17.774, 6.507), (25.669, 7.088)), ((30.12, 7.415), (33.752, 10.071), (37, 13)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e5')
