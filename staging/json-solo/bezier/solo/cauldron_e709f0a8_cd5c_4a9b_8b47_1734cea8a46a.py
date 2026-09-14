"""Cauldron (holidays), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e709f0a8-cd5c-4a9b-8b47-1734cea8a46a'
SOURCE_PATH = 'icons-json/holidays/cauldron_e709f0a8-cd5c-4a9b-8b47-1734cea8a46a.json'
AUTHOR = 'json_to_solo'

class CauldronHolidays(Solo48):
    icon_id = 'cauldron-holidays'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('cauldron', 'holidays')

    def build(self):
        self.add_line('sym-e0', (7, 8), (24, 8))
        self.add_line('sym-e1', (24, 8), (41, 8))
        self.add_bezier('sym-e2', (41, 8), ((41.045, 8.008), (40.955, 8), (41, 8)))
        self.add_bezier('sym-e3', (41, 8), ((42.4, 8), (44, 9.846), (44, 11)))
        self.add_bezier('sym-e4', (44, 11), ((44, 11.067), (44, 10.933), (44, 11)))
        self.add_bezier('sym-e5', (44, 11), ((43.991, 11.059), (44, 10.933), (44, 11)))
        self.add_bezier('sym-e6', (44, 11), ((44, 12.078), (42.973, 13.486), (42, 14)))
        self.add_bezier('sym-e7', (42, 14), ((41.736, 14.143), (41.282, 13.899), (41, 14)))
        self.add_bezier('sym-e8', (41, 14), ((40.664, 14.109), (40.336, 14.882), (40, 15)))
        self.add_bezier('sym-e9', (40, 15), ((39.991, 15.118), (41.673, 16.411), (42, 17)))
        self.add_bezier('sym-e10', (42, 17), ((42.936, 18.667), (43.691, 20.147), (44, 22)))
        self.add_bezier('sym-e11', (44, 22), ((44, 28.897), (40.891, 36.297), (34, 39)))
        self.add_bezier('sym-e12', (34, 39), ((32.527, 39.581), (30.618, 40), (29, 40)))
        self.add_bezier('sym-e13', (29, 40), ((28.927, 40), (29.073, 39.992), (29, 40)))
        self.add_line('sym-e14', (29, 40), (24, 40))
        self.add_line('sym-e15', (24, 40), (19, 40))
        self.add_bezier('sym-e16', (19, 40), ((18.927, 39.992), (19.073, 40), (19, 40)))
        self.add_bezier('sym-e17', (19, 40), ((17.382, 40), (15.473, 39.581), (14, 39)))
        self.add_bezier('sym-e18', (14, 39), ((7.109, 36.297), (4, 28.897), (4, 22)))
        self.add_bezier('sym-e19', (4, 22), ((4.309, 20.147), (5.064, 18.667), (6, 17)))
        self.add_bezier('sym-e20', (6, 17), ((6.327, 16.411), (8.009, 15.118), (8, 15)))
        self.add_bezier('sym-e21', (8, 15), ((7.664, 14.882), (7.336, 14.109), (7, 14)))
        self.add_bezier('sym-e22', (7, 14), ((6.718, 13.899), (6.264, 14.143), (6, 14)))
        self.add_bezier('sym-e23', (6, 14), ((5.027, 13.486), (4, 12.078), (4, 11)))
        self.add_bezier('sym-e24', (4, 11), ((4, 10.933), (4.009, 11.059), (4, 11)))
        self.add_bezier('sym-e25', (4, 11), ((4, 10.933), (4, 11.067), (4, 11)))
        self.add_bezier('sym-e26', (4, 11), ((4, 9.846), (5.6, 8), (7, 8)))
        self.add_bezier('sym-e27', (7, 8), ((7.045, 8), (6.955, 8.008), (7, 8)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', closed=True)
