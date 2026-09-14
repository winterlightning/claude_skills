"""Lab protection glasses (science), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6456c8f-9c22-54f5-8ffc-ddc18ca120ed'
SOURCE_PATH = 'icons-json/science/lab protection glasses_c6456c8f-9c22-54f5-8ffc-ddc18ca120ed.json'
AUTHOR = 'json_to_solo'

class LabProtectionGlassesScience(Solo48):
    icon_id = 'lab-protection-glasses-science'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'protection', 'glasses', 'science')

    def build(self):
        self.add_line('sym-e0', (24, 20), (26, 20))
        self.add_line('sym-e1', (26, 20), (35, 20))
        self.add_bezier('sym-e2', (35, 20), ((37.118, 20), (38.945, 21.372), (41, 22)))
        self.add_bezier('sym-e3', (41, 22), ((41.336, 22.111), (42.809, 21.778), (43, 22)))
        self.add_bezier('sym-e4', (43, 22), ((43.282, 22.345), (44, 24.434), (44, 25)))
        self.add_line('sym-e5', (44, 25), (44, 31))
        self.add_bezier('sym-e6', (44, 31), ((44, 31.098), (44, 31.902), (44, 32)))
        self.add_bezier('sym-e7', (44, 32), ((44, 34.117), (43.445, 36.114), (42, 37)))
        self.add_bezier('sym-e8', (42, 37), ((41.609, 37.246), (40.409, 37.865), (40, 38)))
        self.add_line('sym-e9', (40, 38), (33, 40))
        self.add_bezier('sym-e10', (33, 40), ((32.582, 40), (32.418, 40), (32, 40)))
        self.add_bezier('sym-e11', (32, 40), ((30.645, 40), (29.545, 37.489), (29, 36)))
        self.add_line('sym-e12', (29, 36), (27, 31))
        self.add_bezier('sym-e13', (27, 31), ((26.313, 29.133), (25.009, 29.524), (24, 30)))
        self.add_bezier('sym-e14', (24, 30), ((22.991, 29.524), (21.687, 29.133), (21, 31)))
        self.add_line('sym-e15', (21, 31), (19, 36))
        self.add_bezier('sym-e16', (19, 36), ((18.455, 37.489), (17.355, 40), (16, 40)))
        self.add_bezier('sym-e17', (16, 40), ((15.582, 40), (15.418, 40), (15, 40)))
        self.add_line('sym-e18', (15, 40), (8, 38))
        self.add_bezier('sym-e19', (8, 38), ((7.591, 37.865), (6.391, 37.246), (6, 37)))
        self.add_bezier('sym-e20', (6, 37), ((4.555, 36.114), (4, 34.117), (4, 32)))
        self.add_bezier('sym-e21', (4, 32), ((4, 31.902), (4, 31.098), (4, 31)))
        self.add_line('sym-e22', (4, 31), (4, 25))
        self.add_bezier('sym-e23', (4, 25), ((4, 24.434), (4.718, 22.345), (5, 22)))
        self.add_bezier('sym-e24', (5, 22), ((5.191, 21.778), (6.664, 22.111), (7, 22)))
        self.add_bezier('sym-e25', (7, 22), ((9.055, 21.372), (10.882, 20), (13, 20)))
        self.add_line('sym-e26', (13, 20), (22, 20))
        self.add_line('sym-e27', (22, 20), (24, 20))
        self.add_bezier('sym-e28', (31, 10), ((31.709, 9.052), (32.891, 8), (34, 8)))
        self.add_bezier('sym-e29', (34, 8), ((34.109, 8.012), (33.891, 8), (34, 8)))
        self.add_bezier('sym-e30', (34, 8), ((35.918, 8), (38.045, 11.178), (39, 13)))
        self.add_line('sym-e31', (39, 13), (43, 22))
        self.add_bezier('sym-e32', (17, 10), ((16.291, 9.052), (15.109, 8), (14, 8)))
        self.add_bezier('sym-e33', (14, 8), ((13.891, 8.012), (14.109, 8), (14, 8)))
        self.add_bezier('sym-e34', (14, 8), ((12.082, 8), (9.955, 11.178), (9, 13)))
        self.add_line('sym-e35', (9, 13), (5, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', closed=True)
        self.add_contour('sym-c1', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31')
        self.add_contour('sym-c2', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35')
