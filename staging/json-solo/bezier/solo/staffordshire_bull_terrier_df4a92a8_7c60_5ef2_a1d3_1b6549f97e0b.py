"""Staffordshire bull terrier (pets), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df4a92a8-7c60-5ef2-a1d3-1b6549f97e0b'
SOURCE_PATH = 'icons-json/pets/staffordshire bull terrier_df4a92a8-7c60-5ef2-a1d3-1b6549f97e0b.json'
AUTHOR = 'json_to_solo'

class StaffordshireBullTerrierPets(Solo48):
    icon_id = 'staffordshire-bull-terrier-pets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('staffordshire', 'bull', 'terrier', 'pets')

    def build(self):
        self.add_line('e0', (27, 30), (21, 30))
        self.add_line('e1', (24, 33), (24, 37))
        self.add_line('e2', (37, 27), (34, 36))
        self.add_line('e3', (15, 36), (11, 27))
        self.add_line('e4', (10, 21), (11, 17))
        self.add_line('e5', (19, 11), (29, 11))
        self.add_line('e6', (29, 11), (31, 10))
        self.add_line('e7', (31, 10), (37, 17))
        self.add_line('e8', (4, 19), (5, 15))
        self.add_line('e9', (44, 19), (43, 15))
        self.add_bezier('e10', (21, 30), ((21.245, 31.331), (21.955, 32.227), (23.282, 32.935)), ((23.427, 33.011), (23.827, 33.28), (24, 33.263)), ((24.218, 33.238), (24.582, 32.943), (24.773, 32.834)), ((26.227, 32.034), (26.864, 31.516), (27, 30)))
        self.add_bezier('e11', (37, 17), ((37.318, 20.074), (37.891, 23.96), (37, 27)))
        self.add_bezier('e12', (34, 36), ((33.4, 38.029), (31.445, 40), (28.982, 40)), ((28.891, 39.992), (28.8, 39.992), (28.718, 39.983)), ((26.655, 39.983), (25.327, 38.288), (24, 37)))
        self.add_bezier('e13', (24, 37), ((23.045, 38.053), (21.918, 40), (20.255, 40)), ((20.253, 40), (20.252, 40), (20.251, 40)), ((20.179, 40), (20.099, 39.992), (20.027, 39.992)), ((17.527, 39.992), (15.836, 37.937), (15, 36)))
        self.add_bezier('e14', (11, 27), ((10.391, 25.577), (9.682, 22.482), (10, 21)))
        self.add_bezier('e15', (11, 17), ((12.818, 15.206), (13.773, 14.4), (15.018, 12.286)), ((15.491, 11.478), (15.991, 10.695), (16.545, 9.937)), ((16.6, 9.853), (16.664, 9.768), (16.727, 9.684)), ((17.236, 9.886), (17.573, 10.644), (17.945, 11.015)), ((18.136, 11.2), (18.8, 10.865), (19, 11)))
        self.add_bezier('e16', (11, 17), ((8.5, 18.288), (6.864, 19.025), (4, 19)))
        self.add_bezier('e17', (5, 15), ((5.191, 14.116), (5.245, 12.867), (5.573, 12.025)), ((6.509, 9.583), (8.855, 8.017), (11.655, 8.017)), ((11.736, 8.008), (11.818, 8.008), (11.9, 8)), ((13.809, 8), (15.473, 9.023), (17, 10)))
        self.add_bezier('e18', (38, 18), ((40.518, 18.943), (41.391, 19.034), (44, 19)))
        self.add_bezier('e19', (43, 15), ((42.8, 14.091), (42.736, 12.766), (42.373, 11.899)), ((41.455, 9.701), (38.809, 8.017), (36.282, 8.017)), ((36.127, 8.017), (35.982, 8), (35.827, 8)), ((35.824, 8), (35.82, 8), (35.817, 8)), ((35.593, 8), (35.369, 8.008), (35.145, 8.008)), ((33.791, 8.008), (32.027, 9.343), (31, 10)))
        self.add_contour('c0', 'e0', 'e10', closed=True)
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e11', 'e2', 'e12')
        self.add_contour('c3', 'e13', 'e3', 'e14', 'e4')
        self.add_contour('c4', 'e15', 'e5', 'e6', 'e7')
        self.add_contour('c5', 'e16', 'e8', 'e17')
        self.add_contour('c6', 'e18', 'e9', 'e19')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c5', 'c4')
