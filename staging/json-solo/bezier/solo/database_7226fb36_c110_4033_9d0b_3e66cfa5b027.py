"""Database (servers), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7226fb36-c110-4033-9d0b-3e66cfa5b027'
SOURCE_PATH = 'icons-json/servers/database_7226fb36-c110-4033-9d0b-3e66cfa5b027.json'
AUTHOR = 'json_to_solo'

class Database7226fb36(Solo48):
    icon_id = 'database-7226fb36'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'servers'
    aliases = ()
    keywords = ('database', 'servers')

    def build(self):
        self.add_bezier('sym-e0', (24, 23), ((24.011, 23), (23.989, 23), (24, 23)))
        self.add_bezier('sym-e1', (24, 23), ((26.891, 23), (29.42, 22.685), (32, 22)))
        self.add_bezier('sym-e2', (32, 22), ((34.72, 21.273), (37.491, 20.336), (40, 19)))
        self.add_line('sym-e3', (40, 19), (40, 29))
        self.add_bezier('sym-e4', (40, 29), ((37.549, 30.264), (35.619, 32.209), (33, 33)))
        self.add_bezier('sym-e5', (33, 33), ((30.406, 33.776), (26.91, 34), (24, 34)))
        self.add_bezier('sym-e6', (24, 34), ((23.942, 34), (24.058, 34), (24, 34)))
        self.add_bezier('sym-e7', (24, 34), ((23.942, 34), (24.058, 34), (24, 34)))
        self.add_bezier('sym-e8', (24, 34), ((21.09, 34), (17.594, 33.776), (15, 33)))
        self.add_bezier('sym-e9', (15, 33), ((12.381, 32.209), (10.451, 30.264), (8, 29)))
        self.add_line('sym-e10', (8, 29), (8, 37))
        self.add_bezier('sym-e11', (8, 37), ((8, 37.209), (8, 36.791), (8, 37)))
        self.add_bezier('sym-e12', (8, 37), ((8.059, 37.2), (8, 37.8), (8, 38)))
        self.add_bezier('sym-e13', (8, 38), ((8.564, 39.655), (9.577, 40.264), (11, 41)))
        self.add_bezier('sym-e14', (11, 41), ((14.638, 42.891), (18.983, 44), (23, 44)))
        self.add_bezier('sym-e15', (23, 44), ((23.218, 44), (23.785, 43.997), (24, 44)))
        self.add_bezier('sym-e16', (24, 44), ((24.215, 43.997), (24.782, 44), (25, 44)))
        self.add_bezier('sym-e17', (25, 44), ((29.017, 44), (33.362, 42.891), (37, 41)))
        self.add_bezier('sym-e18', (37, 41), ((38.423, 40.264), (39.436, 39.655), (40, 38)))
        self.add_bezier('sym-e19', (40, 38), ((40, 37.8), (39.941, 37.2), (40, 37)))
        self.add_bezier('sym-e20', (40, 37), ((40, 36.791), (40, 37.209), (40, 37)))
        self.add_line('sym-e21', (40, 37), (40, 29))
        self.add_line('sym-e22', (40, 19), (40, 9))
        self.add_bezier('sym-e23', (40, 9), ((39.444, 8.327), (38.674, 8.536), (38, 8)))
        self.add_bezier('sym-e24', (38, 8), ((34.632, 5.318), (29.109, 4), (25, 4)))
        self.add_bezier('sym-e25', (25, 4), ((24.856, 4), (24.144, 4), (24, 4)))
        self.add_bezier('sym-e26', (24, 4), ((23.928, 4), (24.072, 4), (24, 4)))
        self.add_bezier('sym-e27', (24, 4), ((23.928, 4), (24.072, 4), (24, 4)))
        self.add_bezier('sym-e28', (24, 4), ((23.856, 4), (23.144, 4), (23, 4)))
        self.add_bezier('sym-e29', (23, 4), ((18.891, 4), (13.368, 5.318), (10, 8)))
        self.add_bezier('sym-e30', (10, 8), ((9.326, 8.536), (8.556, 8.327), (8, 9)))
        self.add_line('sym-e31', (8, 9), (8, 19))
        self.add_bezier('sym-e32', (8, 19), ((10.509, 20.336), (13.28, 21.273), (16, 22)))
        self.add_bezier('sym-e33', (16, 22), ((18.58, 22.685), (21.109, 23), (24, 23)))
        self.add_bezier('sym-e34', (24, 23), ((24.011, 23), (23.989, 23), (24, 23)))
        self.add_line('sym-e35', (8, 29), (8, 19))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.add_contour('sym-c1', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34')
        self.add_contour('sym-c2', 'sym-e35')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
