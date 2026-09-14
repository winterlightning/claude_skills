"""Arrow badge bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50465b37-9ca7-502c-8cce-8e0ebf3b8b13'
SOURCE_PATH = 'icons-json/arrows/arrow badge bottom_50465b37-9ca7-502c-8cce-8e0ebf3b8b13.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeBottom50465b37(Solo48):
    icon_id = 'arrow-badge-bottom-50465b37'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (8, 26), (8, 7))
        self.add_line('e1', (11, 4), (37, 4))
        self.add_line('e2', (40, 6), (40, 29))
        self.add_line('e3', (34, 36), (26, 43))
        self.add_line('e4', (22, 42), (10, 32))
        self.add_line('e5', (16, 18), (24, 25))
        self.add_line('e6', (24, 25), (32, 18))
        self.add_bezier('e7', (12, 34), ((11.33, 33.4), (10.66, 32.791), (10, 32.182)), ((9.33, 31.564), (8.02, 30.591), (8.02, 29.6)), ((8.02, 29.355), (8, 29.118), (8, 28.873)), ((8, 27.855), (8, 27.018), (8, 26)))
        self.add_bezier('e8', (8, 7), ((8, 6.8), (8.01, 6.327), (8.01, 6.127)), ((8.01, 4.991), (9.27, 4), (10.47, 4)), ((10.64, 4), (10.82, 4), (11, 4)))
        self.add_bezier('e9', (37, 4), ((37.1, 4), (37.19, 4.009), (37.29, 4.009)), ((38.31, 4.009), (39.2, 4.518), (39.77, 5.255)), ((39.9, 5.436), (39.88, 5.818), (40, 6)))
        self.add_bezier('e10', (40, 29), ((39.99, 29.136), (39.99, 28.818), (39.98, 28.955)), ((39.98, 30.536), (35.01, 35.082), (34, 36)))
        self.add_bezier('e11', (26, 43), ((25.68, 43.291), (25.19, 43.982), (24.68, 43.982)), ((24.62, 43.991), (24.57, 43.991), (24.52, 44)), ((24.519, 44), (24.518, 44), (24.517, 44)), ((24.458, 44), (24.409, 43.991), (24.36, 43.991)), ((23.39, 43.991), (22.61, 42.509), (22, 42)))
        self.add_contour('c0', 'e7', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4')
        self.add_contour('c1', 'e5', 'e6')
