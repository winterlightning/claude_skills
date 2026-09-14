"""Arrow badge right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd008f183-b70b-5382-88ac-0b5a252e8f8e'
SOURCE_PATH = 'icons-json/arrows/arrow badge right_d008f183-b70b-5382-88ac-0b5a252e8f8e.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeRightArrows(Solo48):
    icon_id = 'arrow-badge-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (31, 40), (7, 40))
        self.add_line('e1', (32, 9), (44, 24))
        self.add_bezier('e2', (44, 24), ((43.945, 24.15), (43.891, 24.3), (43.845, 24.45)), ((43.691, 24.76), (43.391, 24.98), (43.2, 25.27)), ((41.982, 27.12), (40.5, 28.76), (39.136, 30.47)), ((36.555, 33.69), (33.673, 36.9), (31, 40)))
        self.add_bezier('e3', (7, 40), ((6.936, 40), (6.6, 40), (6.536, 40)), ((4.1, 40), (4.355, 37.46), (4.245, 35.67)), ((4.164, 34.38), (4.1, 33.09), (4.055, 31.8)), ((4.027, 31.01), (4.018, 30.22), (4.018, 29.43)), ((4.018, 24.56), (4, 19.69), (4, 14.82)), ((4, 14.798), (4, 14.776), (4, 14.754)), ((4, 13.376), (4.009, 11.988), (4.009, 10.61)), ((4.009, 8.98), (5.064, 8.01), (6.5, 8.01)), ((6.572, 8.01), (6.634, 8), (6.697, 8)), ((6.698, 8), (6.699, 8), (6.7, 8)), ((12.555, 8), (18.409, 8.02), (24.264, 8.02)), ((25.391, 8.02), (26.518, 8.04), (27.645, 8.06)), ((28.964, 8.08), (30.982, 8), (32, 9)))
        self.add_contour('c0', 'e2', 'e0', 'e3', 'e1', closed=True)
