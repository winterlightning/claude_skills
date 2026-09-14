"""Specialty skin (health), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5f6a274-d60d-4b27-95f2-f11ba7c9c63e'
SOURCE_PATH = 'icons-json/health/specialty skin_c5f6a274-d60d-4b27-95f2-f11ba7c9c63e.json'
AUTHOR = 'json_to_solo'

class SpecialtySkinHealth(Solo48):
    icon_id = 'specialty-skin-health'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('specialty', 'skin', 'health')

    def build(self):
        self.add_line('sym-e0', (4, 8), (44, 8))
        self.add_bezier('sym-e1', (24, 17), ((28.566, 17), (29.534, 25.342), (34, 25)))
        self.add_bezier('sym-e2', (34, 25), ((36.645, 24.792), (38.1, 20.56), (40, 18)))
        self.add_bezier('sym-e3', (40, 18), ((41.291, 16.272), (42.418, 16.048), (44, 16)))
        self.add_line('sym-e4', (29, 32), (29, 40))
        self.add_line('sym-e5', (37, 40), (37, 32))
        self.add_bezier('sym-e6', (24, 17), ((19.434, 17), (18.466, 25.342), (14, 25)))
        self.add_bezier('sym-e7', (14, 25), ((11.355, 24.792), (9.9, 20.56), (8, 18)))
        self.add_bezier('sym-e8', (8, 18), ((6.709, 16.272), (5.582, 16.048), (4, 16)))
        self.add_line('sym-e9', (19, 32), (19, 40))
        self.add_line('sym-e10', (11, 40), (11, 32))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c5', 'sym-e9')
        self.add_contour('sym-c6', 'sym-e10')
        self.relate('connect', 'sym-c1', 'sym-c4')
