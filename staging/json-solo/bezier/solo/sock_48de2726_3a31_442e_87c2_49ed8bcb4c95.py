"""Sock (holidays), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48de2726-3a31-442e-87c2-49ed8bcb4c95'
SOURCE_PATH = 'icons-json/holidays/sock_48de2726-3a31-442e-87c2-49ed8bcb4c95.json'
AUTHOR = 'json_to_solo'

class SockHolidays(Solo48):
    icon_id = 'sock-holidays'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('sock', 'holidays')

    def build(self):
        self.add_line('e0', (12, 27), (12, 12))
        self.add_line('e1', (28, 12), (12, 12))
        self.add_line('e2', (28, 12), (28, 24))
        self.add_line('e3', (30, 28), (36, 29))
        self.add_line('e4', (31, 44), (20, 40))
        self.add_line('e5', (28, 4), (11, 4))
        self.add_bezier('e6', (12, 27), ((13.027, 27.445), (14.274, 27.564), (15.234, 28.182)), ((18.198, 30.073), (20.059, 33.536), (20.067, 37.264)), ((20.067, 38.3), (20.126, 38.964), (20, 40)))
        self.add_bezier('e7', (12, 27), ((12, 28.845), (12, 30.5), (12.16, 32.336)), ((12.396, 35.082), (14.08, 37.6), (16.269, 38.945)), ((17.373, 39.618), (18.796, 39.6), (20, 40)))
        self.add_bezier('e8', (28, 24), ((28, 24.955), (29.048, 27.709), (30, 28)))
        self.add_bezier('e9', (36, 29), ((38.156, 29.664), (39.983, 33.673), (39.983, 36.018)), ((39.983, 36.117), (40, 36.206), (40, 36.304)), ((40, 36.306), (40, 36.308), (40, 36.309)), ((40, 36.436), (39.983, 36.573), (39.983, 36.7)), ((39.983, 39.655), (37.676, 42.382), (35.326, 43.555)), ((35.023, 43.709), (34.526, 43.991), (34.173, 43.991)), ((34.147, 43.991), (34.122, 44), (34.097, 44)), ((32.977, 44), (32.12, 44), (31, 44)))
        self.add_bezier('e10', (28, 12), ((28.539, 12), (29.44, 11.891), (29.903, 11.609)), ((32.472, 10.036), (32.547, 6.6), (30.156, 4.809)), ((29.693, 4.464), (28.968, 4.018), (28.396, 4.018)), ((28.337, 4.009), (28.059, 4.009), (28, 4)))
        self.add_bezier('e11', (11, 4), ((9.56, 4), (8.017, 5.855), (8.017, 7.455)), ((8.017, 7.573), (8, 7.7), (8, 7.818)), ((8, 7.82), (8, 7.822), (8, 7.824)), ((8, 7.949), (8.008, 8.066), (8.008, 8.191)), ((8.008, 10.318), (10.173, 12), (12, 12)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2', 'e8', 'e3', 'e9', 'e4')
        self.add_contour('c5', 'e10', 'e5', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
