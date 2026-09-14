"""Water currents (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f60789d0-083c-4477-bbef-c268ab428e49'
SOURCE_PATH = 'icons-json/weather/water currents_f60789d0-083c-4477-bbef-c268ab428e49.json'
AUTHOR = 'json_to_solo'

class WaterCurrentsWeather(Solo48):
    icon_id = 'water-currents-weather'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('water', 'currents', 'weather')

    def build(self):
        self.add_line('sym-e0', (8, 8), (4, 12))
        self.add_line('sym-e1', (4, 12), (8, 16))
        self.add_bezier('sym-e2', (19, 21), ((19.003, 20.866), (19, 21.132), (19, 21)))
        self.add_bezier('sym-e3', (19, 21), ((19, 17.532), (18.669, 14.647), (15, 13)))
        self.add_bezier('sym-e4', (15, 13), ((14.327, 12.697), (12.773, 12), (12, 12)))
        self.add_line('sym-e5', (12, 12), (4, 12))
        self.add_bezier('sym-e6', (4, 25), ((4, 25.042), (4, 24.958), (4, 25)))
        self.add_bezier('sym-e7', (4, 25), ((4, 28.149), (7.982, 30.027), (11, 29)))
        self.add_bezier('sym-e8', (11, 29), ((12.391, 28.528), (13.109, 28.036), (14, 27)))
        self.add_bezier('sym-e9', (14, 26), ((14.518, 26.707), (15.336, 27.402), (16, 28)))
        self.add_bezier('sym-e10', (16, 28), ((16.961, 28.854), (17.68, 29), (19, 29)))
        self.add_bezier('sym-e11', (19, 29), ((19.84, 29), (21.272, 28.432), (22, 28)))
        self.add_bezier('sym-e12', (22, 28), ((22.573, 27.663), (22.6, 27.505), (23, 27)))
        self.add_bezier('sym-e13', (23, 27), ((23.282, 26.655), (23.718, 26.345), (24, 26)))
        self.add_bezier('sym-e14', (24, 26), ((24.009, 26.011), (23.991, 25.989), (24, 26)))
        self.add_bezier('sym-e15', (24, 26), ((24.009, 25.989), (23.991, 26.011), (24, 26)))
        self.add_bezier('sym-e16', (24, 26), ((24.282, 26.345), (24.718, 26.655), (25, 27)))
        self.add_bezier('sym-e17', (25, 27), ((25.4, 27.505), (25.427, 27.663), (26, 28)))
        self.add_bezier('sym-e18', (26, 28), ((26.728, 28.432), (28.16, 29), (29, 29)))
        self.add_bezier('sym-e19', (29, 29), ((30.32, 29), (31.039, 28.854), (32, 28)))
        self.add_bezier('sym-e20', (32, 28), ((32.664, 27.402), (33.482, 26.707), (34, 26)))
        self.add_bezier('sym-e21', (4, 36), ((4.009, 36.059), (4, 35.941), (4, 36)))
        self.add_bezier('sym-e22', (4, 36), ((4, 38.139), (6.773, 40), (9, 40)))
        self.add_bezier('sym-e23', (9, 40), ((9.109, 40), (8.891, 40), (9, 40)))
        self.add_bezier('sym-e24', (9, 40), ((9.109, 40), (8.891, 40), (9, 40)))
        self.add_bezier('sym-e25', (9, 40), ((10.336, 40), (12.155, 38.893), (13, 38)))
        self.add_bezier('sym-e26', (13, 38), ((13.345, 37.638), (13.891, 37), (14, 37)))
        self.add_bezier('sym-e27', (14, 37), ((14.264, 37.371), (14.736, 37.629), (15, 38)))
        self.add_bezier('sym-e28', (15, 38), ((15.327, 38.446), (15.527, 38.68), (16, 39)))
        self.add_bezier('sym-e29', (16, 39), ((17.936, 39.943), (20.236, 40), (22, 39)))
        self.add_bezier('sym-e30', (22, 39), ((22.709, 38.427), (23.445, 37.699), (24, 37)))
        self.add_bezier('sym-e31', (24, 37), ((24.555, 37.699), (25.291, 38.427), (26, 39)))
        self.add_bezier('sym-e32', (26, 39), ((27.764, 40), (30.064, 39.943), (32, 39)))
        self.add_bezier('sym-e33', (32, 39), ((32.473, 38.68), (32.673, 38.446), (33, 38)))
        self.add_bezier('sym-e34', (33, 38), ((33.264, 37.629), (33.736, 37.371), (34, 37)))
        self.add_bezier('sym-e35', (34, 37), ((34.109, 37), (34.655, 37.638), (35, 38)))
        self.add_bezier('sym-e36', (35, 38), ((35.845, 38.893), (37.664, 40), (39, 40)))
        self.add_bezier('sym-e37', (39, 40), ((39.109, 40), (38.891, 40), (39, 40)))
        self.add_bezier('sym-e38', (39, 40), ((39.109, 40), (38.891, 40), (39, 40)))
        self.add_bezier('sym-e39', (39, 40), ((41.227, 40), (44, 38.139), (44, 36)))
        self.add_bezier('sym-e40', (44, 36), ((44, 35.941), (43.991, 36.059), (44, 36)))
        self.add_line('sym-e41', (40, 8), (44, 12))
        self.add_line('sym-e42', (44, 12), (40, 16))
        self.add_bezier('sym-e43', (29, 21), ((28.997, 20.866), (29, 21.132), (29, 21)))
        self.add_bezier('sym-e44', (29, 21), ((29, 17.532), (29.331, 14.647), (33, 13)))
        self.add_bezier('sym-e45', (33, 13), ((33.673, 12.697), (35.227, 12), (36, 12)))
        self.add_line('sym-e46', (36, 12), (44, 12))
        self.add_bezier('sym-e47', (44, 25), ((44, 25.042), (44, 24.958), (44, 25)))
        self.add_bezier('sym-e48', (44, 25), ((44, 28.149), (40.018, 30.027), (37, 29)))
        self.add_bezier('sym-e49', (37, 29), ((35.609, 28.528), (34.891, 28.036), (34, 27)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c3', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.add_contour('sym-c4', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39', 'sym-e40')
        self.add_contour('sym-c5', 'sym-e41', 'sym-e42')
        self.add_contour('sym-c6', 'sym-e43', 'sym-e44', 'sym-e45', 'sym-e46')
        self.add_contour('sym-c7', 'sym-e47', 'sym-e48', 'sym-e49')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c1')
