"""Blood cell (other), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4297dd9b-55dc-43a4-a561-14dd5b598993'
SOURCE_PATH = 'icons-json/other/blood cell_4297dd9b-55dc-43a4-a561-14dd5b598993.json'
AUTHOR = 'json_to_solo'

class BloodCellOther(Solo48):
    icon_id = 'blood-cell-other'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('blood', 'cell', 'other')

    def build(self):
        self.add_bezier('sym-e0', (24, 42), ((24.081, 41.994), (23.914, 42), (24, 42)))
        self.add_bezier('sym-e1', (24, 42), ((25.407, 42), (27.075, 41.006), (28, 40)))
        self.add_bezier('sym-e2', (28, 40), ((28.344, 39.624), (28.738, 39.442), (29, 39)))
        self.add_bezier('sym-e3', (29, 39), ((29.025, 38.959), (28.951, 39.016), (29, 39)))
        self.add_bezier('sym-e4', (29, 39), ((29.033, 38.992), (28.967, 38.984), (29, 39)))
        self.add_bezier('sym-e5', (29, 39), ((29.368, 39.229), (30.583, 38.877), (31, 39)))
        self.add_bezier('sym-e6', (31, 39), ((32.096, 39.319), (32.961, 39.491), (34, 39)))
        self.add_bezier('sym-e7', (34, 39), ((35.669, 38.198), (36.46, 36.743), (37, 35)))
        self.add_bezier('sym-e8', (37, 35), ((37.074, 34.755), (37.975, 33.033), (38, 33)))
        self.add_bezier('sym-e9', (38, 33), ((38.033, 32.951), (37.935, 33.008), (38, 33)))
        self.add_bezier('sym-e10', (38, 33), ((38.548, 32.869), (39.534, 32.319), (40, 32)))
        self.add_bezier('sym-e11', (40, 32), ((41.645, 30.887), (42, 28.923), (42, 27)))
        self.add_bezier('sym-e12', (42, 27), ((42, 26.902), (42, 27.098), (42, 27)))
        self.add_bezier('sym-e13', (42, 27), ((42, 26.91), (42, 26.09), (42, 26)))
        self.add_bezier('sym-e14', (42, 26), ((42, 24.56), (41.745, 23.219), (41, 22)))
        self.add_bezier('sym-e15', (41, 22), ((40.861, 21.763), (40.033, 21.131), (40, 21)))
        self.add_bezier('sym-e16', (40, 21), ((39.926, 20.73), (39.984, 20.286), (40, 20)))
        self.add_bezier('sym-e17', (40, 20), ((40.065, 19.215), (40.139, 17.777), (40, 17)))
        self.add_bezier('sym-e18', (40, 17), ((39.558, 14.57), (37.381, 12.72), (35, 12)))
        self.add_bezier('sym-e19', (35, 12), ((34.509, 11.853), (34.507, 12.008), (34, 12)))
        self.add_bezier('sym-e20', (34, 12), ((33.82, 12), (33.164, 12.049), (33, 12)))
        self.add_bezier('sym-e21', (33, 12), ((32.984, 11.992), (33.074, 11.196), (33, 11)))
        self.add_bezier('sym-e22', (33, 11), ((32.665, 10.206), (31.573, 9.638), (31, 9)))
        self.add_bezier('sym-e23', (31, 9), ((29.38, 7.167), (27.438, 6), (25, 6)))
        self.add_bezier('sym-e24', (25, 6), ((24.779, 6), (24.221, 6), (24, 6)))
        self.add_bezier('sym-e25', (24, 6), ((23.779, 6), (23.221, 6), (23, 6)))
        self.add_bezier('sym-e26', (23, 6), ((20.562, 6), (18.62, 7.167), (17, 9)))
        self.add_bezier('sym-e27', (17, 9), ((16.427, 9.638), (15.335, 10.206), (15, 11)))
        self.add_bezier('sym-e28', (15, 11), ((14.926, 11.196), (15.016, 11.992), (15, 12)))
        self.add_bezier('sym-e29', (15, 12), ((14.836, 12.049), (14.18, 12), (14, 12)))
        self.add_bezier('sym-e30', (14, 12), ((13.493, 12.008), (13.491, 11.853), (13, 12)))
        self.add_bezier('sym-e31', (13, 12), ((10.619, 12.72), (8.442, 14.57), (8, 17)))
        self.add_bezier('sym-e32', (8, 17), ((7.861, 17.777), (7.935, 19.215), (8, 20)))
        self.add_bezier('sym-e33', (8, 20), ((8.016, 20.286), (8.074, 20.73), (8, 21)))
        self.add_bezier('sym-e34', (8, 21), ((7.967, 21.131), (7.139, 21.763), (7, 22)))
        self.add_bezier('sym-e35', (7, 22), ((6.255, 23.219), (6, 24.56), (6, 26)))
        self.add_bezier('sym-e36', (6, 26), ((6, 26.09), (6, 26.91), (6, 27)))
        self.add_bezier('sym-e37', (6, 27), ((6, 27.098), (6, 26.902), (6, 27)))
        self.add_bezier('sym-e38', (6, 27), ((6, 28.923), (6.355, 30.887), (8, 32)))
        self.add_bezier('sym-e39', (8, 32), ((8.466, 32.319), (9.452, 32.869), (10, 33)))
        self.add_bezier('sym-e40', (10, 33), ((10.065, 33.008), (9.967, 32.951), (10, 33)))
        self.add_bezier('sym-e41', (10, 33), ((10.025, 33.033), (10.926, 34.755), (11, 35)))
        self.add_bezier('sym-e42', (11, 35), ((11.54, 36.743), (12.331, 38.198), (14, 39)))
        self.add_bezier('sym-e43', (14, 39), ((15.039, 39.491), (15.904, 39.319), (17, 39)))
        self.add_bezier('sym-e44', (17, 39), ((17.417, 38.877), (18.632, 39.229), (19, 39)))
        self.add_bezier('sym-e45', (19, 39), ((19.033, 38.984), (18.967, 38.992), (19, 39)))
        self.add_bezier('sym-e46', (19, 39), ((19.049, 39.016), (18.975, 38.959), (19, 39)))
        self.add_bezier('sym-e47', (19, 39), ((19.262, 39.442), (19.656, 39.624), (20, 40)))
        self.add_bezier('sym-e48', (20, 40), ((20.925, 41.006), (22.593, 42), (24, 42)))
        self.add_bezier('sym-e49', (24, 42), ((24.086, 42), (23.919, 41.994), (24, 42)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39', 'sym-e40', 'sym-e41', 'sym-e42', 'sym-e43', 'sym-e44', 'sym-e45', 'sym-e46', 'sym-e47', 'sym-e48', 'sym-e49', closed=True)
