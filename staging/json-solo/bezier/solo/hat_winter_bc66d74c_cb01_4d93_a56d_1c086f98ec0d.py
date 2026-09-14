"""Batch-05/hat winter (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc66d74c-cb01-4d93-a56d-1c086f98ec0d'
SOURCE_PATH = 'icons-json/accessories/batch-05/hat winter_bc66d74c-cb01-4d93-a56d-1c086f98ec0d.json'
AUTHOR = 'json_to_solo'

class Batch05HatWinter(Solo48):
    icon_id = 'batch-05-hat-winter'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'winter', 'accessories')

    def build(self):
        self.add_line('sym-e0', (8, 28), (40, 28))
        self.add_bezier('sym-e1', (40, 28), ((41.155, 28), (43.327, 27.78), (44, 29)))
        self.add_bezier('sym-e2', (44, 29), ((44, 29.2), (43.918, 29.81), (44, 30)))
        self.add_line('sym-e3', (44, 30), (44, 37))
        self.add_bezier('sym-e4', (44, 37), ((44, 37.05), (44, 36.95), (44, 37)))
        self.add_bezier('sym-e5', (44, 37), ((44, 37.98), (41.891, 40), (41, 40)))
        self.add_bezier('sym-e6', (41, 40), ((40.955, 40), (41.045, 39.99), (41, 40)))
        self.add_line('sym-e7', (41, 40), (24, 40))
        self.add_line('sym-e8', (24, 40), (7, 40))
        self.add_bezier('sym-e9', (7, 40), ((6.955, 39.99), (7.045, 40), (7, 40)))
        self.add_bezier('sym-e10', (7, 40), ((6.109, 40), (4, 37.98), (4, 37)))
        self.add_bezier('sym-e11', (4, 37), ((4, 36.95), (4, 37.05), (4, 37)))
        self.add_line('sym-e12', (4, 37), (4, 30))
        self.add_bezier('sym-e13', (4, 30), ((4.082, 29.81), (4, 29.2), (4, 29)))
        self.add_bezier('sym-e14', (4, 29), ((4.673, 27.78), (6.845, 28), (8, 28)))
        self.add_bezier('sym-e15', (8, 28), ((8.236, 24.98), (7.073, 22.01), (8, 19)))
        self.add_bezier('sym-e16', (8, 19), ((10.009, 12.51), (16.745, 8), (23, 8)))
        self.add_bezier('sym-e17', (23, 8), ((23.145, 8), (22.855, 8), (23, 8)))
        self.add_bezier('sym-e18', (23, 8), ((23.196, 8), (23.802, 8), (24, 8)))
        self.add_bezier('sym-e19', (24, 8), ((24.198, 8), (24.804, 8), (25, 8)))
        self.add_bezier('sym-e20', (25, 8), ((25.145, 8), (24.855, 8), (25, 8)))
        self.add_bezier('sym-e21', (25, 8), ((31.255, 8), (37.991, 12.51), (40, 19)))
        self.add_bezier('sym-e22', (40, 19), ((40.927, 22.01), (39.764, 24.98), (40, 28)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22')
