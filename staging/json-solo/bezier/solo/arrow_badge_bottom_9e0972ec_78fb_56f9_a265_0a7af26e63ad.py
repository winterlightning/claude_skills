"""Arrow badge bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e0972ec-78fb-56f9-a265-0a7af26e63ad'
SOURCE_PATH = 'icons-json/arrows/arrow badge bottom_9e0972ec-78fb-56f9-a265-0a7af26e63ad.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeBottom9e0972ec(Solo48):
    icon_id = 'arrow-badge-bottom-9e0972ec'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (8, 31), (8, 7))
        self.add_line('e1', (39, 32), (24, 44))
        self.add_bezier('e2', (24, 44), ((23.85, 43.945), (23.7, 43.891), (23.55, 43.845)), ((23.24, 43.691), (23.02, 43.391), (22.73, 43.2)), ((20.88, 41.982), (19.24, 40.5), (17.53, 39.136)), ((14.31, 36.555), (11.1, 33.673), (8, 31)))
        self.add_bezier('e3', (8, 7), ((8, 6.936), (8, 6.6), (8, 6.536)), ((8, 4.1), (10.54, 4.355), (12.33, 4.245)), ((13.62, 4.164), (14.91, 4.1), (16.2, 4.055)), ((16.99, 4.027), (17.78, 4.018), (18.57, 4.018)), ((23.44, 4.018), (28.31, 4), (33.18, 4)), ((33.202, 4), (33.224, 4), (33.246, 4)), ((34.624, 4), (36.012, 4.009), (37.39, 4.009)), ((39.02, 4.009), (39.99, 5.064), (39.99, 6.5)), ((39.99, 6.572), (40, 6.634), (40, 6.697)), ((40, 6.698), (40, 6.699), (40, 6.7)), ((40, 12.464), (39.98, 18.227), (39.98, 23.991)), ((39.98, 25.209), (39.96, 26.427), (39.94, 27.645)), ((39.92, 28.964), (40, 30.982), (39, 32)))
        self.add_contour('c0', 'e2', 'e0', 'e3', 'e1', closed=True)
