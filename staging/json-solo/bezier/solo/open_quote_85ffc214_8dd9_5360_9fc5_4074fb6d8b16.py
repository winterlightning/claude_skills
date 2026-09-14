"""Open quote (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85ffc214-8dd9-5360-9fc5-4074fb6d8b16'
SOURCE_PATH = 'icons-json/interface-essential/open quote_85ffc214-8dd9-5360-9fc5-4074fb6d8b16.json'
AUTHOR = 'json_to_solo'

class OpenQuoteInterfaceEssential(Solo48):
    icon_id = 'open-quote-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('open', 'quote', 'interface-essential')

    def build(self):
        self.add_line('e0', (7, 24), (5, 26))
        self.add_line('e1', (30, 24), (28, 26))
        self.add_bezier('e2', (18, 8), ((13.245, 9.96), (9.009, 13.7), (6.664, 18.69)), ((6.109, 19.87), (5.091, 22.19), (5.018, 23.49)), ((4.982, 24.32), (5.036, 25.16), (5, 26)))
        self.add_bezier('e3', (5, 26), ((4.573, 27.42), (4.009, 29), (4.009, 30.53)), ((4.009, 30.678), (4, 30.825), (4, 30.973)), ((4, 30.975), (4, 30.978), (4, 30.98)), ((4, 31.13), (4.009, 31.28), (4.009, 31.43)), ((4.009, 35.74), (7.836, 39.99), (11.755, 39.99)), ((11.889, 39.99), (12.023, 40), (12.157, 40)), ((12.159, 40), (12.162, 40), (12.164, 40)), ((12.291, 40), (12.427, 39.99), (12.555, 39.99)), ((13.809, 39.99), (15.118, 39.53), (16.209, 38.86)), ((22.282, 35.15), (21.764, 24.78), (14.991, 22.36)), ((13.745, 21.92), (12.418, 21.8), (11.127, 21.98)), ((9.473, 22.22), (8.355, 22.95), (7, 24)))
        self.add_bezier('e4', (41, 8), ((35.964, 9.88), (32.327, 13.77), (29.736, 18.87)), ((29.1, 20.12), (28.364, 21.59), (28.118, 23.02)), ((27.964, 24.01), (28.164, 25.01), (28, 26)))
        self.add_bezier('e5', (28, 26), ((27.8, 27.72), (27.118, 29.42), (27.291, 31.16)), ((27.727, 35.55), (30.9, 39.98), (35.209, 39.98)), ((35.355, 39.99), (35.5, 39.99), (35.636, 40)), ((35.855, 40), (36.064, 39.98), (36.273, 39.98)), ((40.209, 39.98), (43.982, 35.67), (43.982, 31.37)), ((43.982, 31.17), (44, 30.96), (44, 30.76)), ((44, 30.758), (44, 30.756), (44, 30.753)), ((44, 30.616), (43.991, 30.478), (43.991, 30.34)), ((43.991, 25.36), (39.527, 21.56), (35.236, 21.83)), ((33.382, 21.94), (31.518, 22.89), (30, 24)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3', 'e0', closed=True)
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e1', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
