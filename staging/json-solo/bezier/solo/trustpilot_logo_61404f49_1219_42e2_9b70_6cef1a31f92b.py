"""Trustpilot logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61404f49-1219-42e2-9b70-6cef1a31f92b'
SOURCE_PATH = 'icons-json/logos/trustpilot logo_61404f49-1219-42e2-9b70-6cef1a31f92b.json'
AUTHOR = 'json_to_solo'

class TrustpilotLogoLogos(Solo48):
    icon_id = 'trustpilot-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('trustpilot', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (18, 17), (22, 8))
        self.add_line('e1', (26, 8), (30, 18))
        self.add_line('e2', (30, 18), (40, 18))
        self.add_line('e3', (41, 22), (33, 29))
        self.add_line('e4', (33, 29), (36, 40))
        self.add_line('e5', (34, 42), (24, 35))
        self.add_line('e6', (24, 35), (14, 42))
        self.add_line('e7', (12, 40), (15, 29))
        self.add_line('e8', (15, 29), (7, 22))
        self.add_line('e9', (8, 18), (18, 17))
        self.add_bezier('e10', (22, 8), ((22.185, 7.549), (23.492, 6), (24.032, 6)), ((24.041, 6), (24.049, 6), (24.057, 6)), ((24.515, 6), (25.836, 7.583), (26, 8)))
        self.add_bezier('e11', (40, 18), ((40.671, 18.245), (41.992, 18.903), (41.992, 19.795)), ((41.992, 19.859), (42, 19.923), (42, 19.988)), ((42, 19.989), (42, 19.99), (42, 19.991)), ((42, 20.515), (41.376, 21.665), (41, 22)))
        self.add_bezier('e12', (36, 40), ((35.959, 40.9), (36.093, 41.239), (35.299, 41.82)), ((35.209, 41.894), (35.054, 42), (34.923, 42)), ((34.857, 42), (34.8, 42), (34.735, 42)), ((34.555, 42), (34.366, 42), (34.186, 42)), ((34.064, 42), (34.123, 42), (34, 42)))
        self.add_bezier('e13', (14, 42), ((13.877, 42), (13.936, 42), (13.814, 42)), ((13.568, 42), (13.331, 42), (13.085, 42)), ((13.02, 42), (12.963, 42), (12.905, 41.992)), ((12.783, 41.935), (12.668, 41.869), (12.545, 41.804)), ((11.817, 41.182), (12.057, 40.859), (12, 40)))
        self.add_bezier('e14', (7, 22), ((6.771, 21.705), (6, 20.711), (6, 20.326)), ((6, 20.318), (6, 20.309), (6, 20.3)), ((6, 19.743), (6.669, 18.881), (7.08, 18.551)), ((7.26, 18.412), (7.812, 18.115), (8, 18)))
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e2', 'e11', 'e3', 'e4', 'e12', 'e5', 'e6', 'e13', 'e7', 'e8', 'e14', 'e9', closed=True)
