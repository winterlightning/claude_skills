"""Arrow badge top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '466b0701-7c09-52f1-bd1d-9f1f576f28f7'
SOURCE_PATH = 'icons-json/arrows/arrow badge top_466b0701-7c09-52f1-bd1d-9f1f576f28f7.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeTopArrows(Solo48):
    icon_id = 'arrow-badge-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (9, 16), (24, 4))
        self.add_line('e1', (40, 17), (40, 41))
        self.add_bezier('e2', (24, 4), ((24.15, 4.055), (24.3, 4.109), (24.45, 4.155)), ((24.76, 4.309), (24.98, 4.609), (25.27, 4.8)), ((27.12, 6.018), (28.76, 7.5), (30.47, 8.864)), ((33.69, 11.445), (36.9, 14.327), (40, 17)))
        self.add_bezier('e3', (40, 41), ((40, 41.064), (40, 41.4), (40, 41.464)), ((40, 43.9), (37.46, 43.645), (35.67, 43.755)), ((34.38, 43.836), (33.09, 43.9), (31.8, 43.945)), ((31.01, 43.973), (30.22, 43.982), (29.43, 43.982)), ((24.56, 43.982), (19.69, 44), (14.82, 44)), ((14.798, 44), (14.776, 44), (14.754, 44)), ((13.376, 44), (11.988, 43.991), (10.61, 43.991)), ((8.98, 43.991), (8.01, 42.936), (8.01, 41.5)), ((8.01, 41.428), (8, 41.366), (8, 41.303)), ((8, 41.302), (8, 41.301), (8, 41.3)), ((8, 35.445), (8.02, 29.591), (8.02, 23.736)), ((8.02, 22.609), (8.04, 21.482), (8.06, 20.355)), ((8.08, 19.036), (8, 17.018), (9, 16)))
        self.add_contour('c0', 'e0', 'e2', 'e1', 'e3', closed=True)
