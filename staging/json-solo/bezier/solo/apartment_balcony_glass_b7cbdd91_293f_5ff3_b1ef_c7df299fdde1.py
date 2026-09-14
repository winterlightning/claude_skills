"""Apartment balcony glass (building), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7cbdd91-293f-5ff3-b1ef-c7df299fdde1'
SOURCE_PATH = 'icons-json/building/apartment balcony glass_b7cbdd91-293f-5ff3-b1ef-c7df299fdde1.json'
AUTHOR = 'json_to_solo'

class ApartmentBalconyGlassBuilding(Solo48):
    icon_id = 'apartment-balcony-glass-building'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('apartment', 'balcony', 'glass', 'building')

    def build(self):
        self.add_line('e0', (42, 27), (18, 27))
        self.add_line('e1', (24, 8), (24, 40))
        self.add_line('e2', (39, 27), (39, 40))
        self.add_line('e3', (39, 40), (9, 40))
        self.add_line('e4', (9, 40), (9, 27))
        self.add_line('e5', (36, 27), (36, 8))
        self.add_line('e6', (36, 8), (24, 19))
        self.add_line('e7', (36, 8), (12, 8))
        self.add_line('e8', (12, 8), (12, 27))
        self.add_line('e9', (18, 15), (12, 20))
        self.add_bezier('e10', (44, 29), ((43.909, 28.798), (43.936, 28.623), (43.809, 28.421)), ((43.518, 27.983), (42.6, 27), (42, 27)))
        self.add_bezier('e11', (18, 27), ((16.2, 27), (14, 27.352), (12.182, 27.368)), ((11.273, 27.377), (10.364, 27.36), (9.455, 27.368)), ((7.855, 27.385), (5.827, 26.964), (4.591, 28.152)), ((4.445, 28.295), (4.236, 28.413), (4.136, 28.589)), ((4, 28.985), (4.255, 28.562), (4, 29)))
        self.add_bezier('e12', (12, 20), ((12, 19.722), (12, 19.278), (12, 19)))
        self.add_contour('c0', 'e10', 'e0', 'e11')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e6')
        self.add_contour('c4', 'e7', 'e8')
        self.add_contour('c5', 'e9', 'e12')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c5', 'c4')
        self.relate('connect', 'c5', 'c4')
