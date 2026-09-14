"""Acorn (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba175ed8-1c20-536e-bdbc-2223ac1856fa'
SOURCE_PATH = 'icons-json/food/acorn_ba175ed8-1c20-536e-bdbc-2223ac1856fa.json'
AUTHOR = 'json_to_solo'

class Acorn(Solo48):
    icon_id = 'acorn'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('acorn', 'food')

    def build(self):
        self.add_line('e0', (11, 22), (37, 22))
        self.add_bezier('e1', (27, 4), ((26.8, 4.109), (26.57, 4.1), (26.38, 4.218)), ((24.38, 5.5), (24.21, 6.955), (24, 9)))
        self.add_bezier('e2', (37, 22), ((37.23, 24.873), (37.99, 27.973), (37.57, 30.855)), ((36.86, 35.664), (32.94, 39.209), (28.5, 41.491)), ((27.36, 42.073), (26.21, 42.636), (25.11, 43.282)), ((24.874, 43.425), (24.085, 44), (23.994, 44)), ((23.992, 44), (23.991, 44), (23.99, 44)), ((23.79, 43.864), (23.6, 43.718), (23.4, 43.582)), ((22.44, 42.927), (21.37, 42.409), (20.32, 41.9)), ((14.9, 39.236), (10.81, 35.582), (10.4, 29.7)), ((10.28, 27.864), (10.5, 26.018), (10.77, 24.209)), ((10.84, 23.664), (11.11, 22.355), (11, 22.182)), ((10.5, 22), (10, 21.809), (9.5, 21.627)), ((8.65, 21.282), (8.01, 19.982), (8.01, 19.191)), ((8.01, 19.119), (8, 19.048), (8, 18.976)), ((8, 18.975), (8, 18.974), (8, 18.973)), ((8.01, 18.827), (8.01, 18.682), (8.02, 18.545)), ((8.02, 17.6), (8.55, 16.6), (8.94, 15.755)), ((11.57, 10.073), (18.07, 9.055), (24, 9)))
        self.add_bezier('e3', (37, 22), ((37.46, 21.827), (37.92, 21.836), (38.38, 21.673)), ((39.35, 21.273), (40, 19.782), (40, 18.891)), ((40, 18.89), (40, 18.889), (40, 18.888)), ((40, 18.816), (40, 18.744), (40, 18.673)), ((40, 18.609), (40, 18.536), (39.99, 18.464)), ((39.99, 17.436), (39.41, 16.418), (38.95, 15.518)), ((36.08, 9.909), (29.96, 9.1), (24, 9)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
