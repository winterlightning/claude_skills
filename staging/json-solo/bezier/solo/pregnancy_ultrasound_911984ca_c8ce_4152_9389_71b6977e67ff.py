"""Pregnancy ultrasound (health), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '911984ca-c8ce-4152-9389-71b6977e67ff'
SOURCE_PATH = 'icons-json/health/pregnancy ultrasound_911984ca-c8ce-4152-9389-71b6977e67ff.json'
AUTHOR = 'json_to_solo'

class PregnancyUltrasoundHealth(Solo48):
    icon_id = 'pregnancy-ultrasound-health'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('pregnancy', 'ultrasound', 'health')

    def build(self):
        self.add_line('e0', (44, 29), (31, 8))
        self.add_line('e1', (18, 8), (4, 29))
        self.add_bezier('e2', (31, 8), ((30.455, 8), (30.191, 8), (29.645, 8)), ((29.036, 8), (28.355, 8.512), (27.764, 8.736)), ((26.591, 9.136), (25.4, 9.392), (24.209, 9.408)), ((23.045, 9.424), (21.873, 9.2), (20.736, 8.752)), ((20.245, 8.56), (19.627, 8), (19.127, 8)), ((18.636, 8), (18.5, 8), (18, 8)))
        self.add_bezier('e3', (4, 29), ((4, 29.256), (4, 29.328), (4, 29.584)), ((4, 29.856), (4, 30.176), (4, 30.448)), ((4, 30.624), (4, 30.8), (4, 30.976)), ((4, 31.424), (4.709, 31.76), (4.9, 31.904)), ((6.027, 32.784), (7.182, 33.568), (8.355, 34.288)), ((13.127, 37.216), (18.173, 39.968), (23.282, 39.968)), ((23.55, 39.968), (23.819, 40), (24.087, 40)), ((24.091, 40), (24.096, 40), (24.1, 40)), ((24.518, 40), (24.927, 39.968), (25.336, 39.968)), ((30.264, 39.968), (35.173, 37.376), (39.745, 34.368)), ((40.827, 33.648), (41.9, 32.88), (42.945, 32.016)), ((43.164, 31.824), (44, 31.392), (44, 30.848)), ((44, 30.768), (43.991, 30.672), (43.991, 30.576)), ((43.991, 30.288), (44, 29.936), (44, 29.664)), ((44, 29.376), (44, 29.288), (44, 29)))
        self.add_contour('c0', 'e0', 'e2', 'e1', 'e3', closed=True)
