"""Batch-03/bag purse (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2197e20-d553-5c3e-bcd7-886f9d1e76e8'
SOURCE_PATH = 'icons-json/accessories/batch-03/bag purse_a2197e20-d553-5c3e-bcd7-886f9d1e76e8.json'
AUTHOR = 'json_to_solo'

class Batch03BagPurse(Solo48):
    icon_id = 'batch-03-bag-purse'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'bag', 'purse', 'accessories')

    def build(self):
        self.add_bezier('sym-e0', (28, 31), ((26.884, 29.169), (26.694, 29), (25, 29)))
        self.add_bezier('sym-e1', (25, 29), ((24.756, 29), (24.301, 28.997), (24, 29)))
        self.add_bezier('sym-e2', (24, 29), ((23.997, 29), (24.003, 29), (24, 29)))
        self.add_bezier('sym-e3', (24, 29), ((23.997, 29), (24.003, 29), (24, 29)))
        self.add_bezier('sym-e4', (24, 29), ((23.699, 28.997), (23.244, 29), (23, 29)))
        self.add_bezier('sym-e5', (23, 29), ((21.306, 29), (21.116, 29.169), (20, 31)))
        self.add_bezier('sym-e6', (20, 31), ((20.408, 34.029), (21.278, 34), (24, 34)))
        self.add_bezier('sym-e7', (24, 34), ((26.722, 34), (27.592, 34.029), (28, 31)))
        self.add_line('sym-e8', (28, 31), (32, 31))
        self.add_bezier('sym-e9', (32, 31), ((36.778, 31), (36.973, 29.551), (40, 26)))
        self.add_line('sym-e10', (40, 26), (40, 22))
        self.add_bezier('sym-e11', (40, 22), ((39.566, 19.415), (38.101, 16), (35, 16)))
        self.add_line('sym-e12', (35, 16), (33, 16))
        self.add_line('sym-e13', (33, 16), (24, 16))
        self.add_line('sym-e14', (24, 16), (15, 16))
        self.add_line('sym-e15', (15, 16), (13, 16))
        self.add_bezier('sym-e16', (13, 16), ((9.899, 16), (8.434, 19.415), (8, 22)))
        self.add_line('sym-e17', (8, 22), (8, 26))
        self.add_bezier('sym-e18', (8, 26), ((11.027, 29.551), (11.222, 31), (16, 31)))
        self.add_line('sym-e19', (16, 31), (20, 31))
        self.add_bezier('sym-e20', (33, 16), ((32.943, 14.961), (33.237, 14.015), (33, 13)))
        self.add_bezier('sym-e21', (33, 13), ((32.264, 9.875), (29.101, 6.777), (26, 6)))
        self.add_bezier('sym-e22', (26, 6), ((25.501, 6), (25.515, 6), (25, 6)))
        self.add_bezier('sym-e23', (25, 6), ((24.804, 6), (24.188, 6), (24, 6)))
        self.add_bezier('sym-e24', (24, 6), ((23.902, 6), (24.098, 6), (24, 6)))
        self.add_bezier('sym-e25', (24, 6), ((23.902, 6), (24.098, 6), (24, 6)))
        self.add_bezier('sym-e26', (24, 6), ((23.812, 6), (23.196, 6), (23, 6)))
        self.add_bezier('sym-e27', (23, 6), ((22.485, 6), (22.499, 6), (22, 6)))
        self.add_bezier('sym-e28', (22, 6), ((18.899, 6.777), (15.736, 9.875), (15, 13)))
        self.add_bezier('sym-e29', (15, 13), ((14.763, 14.015), (15.057, 14.961), (15, 16)))
        self.add_line('sym-e30', (40, 26), (42, 34))
        self.add_bezier('sym-e31', (42, 34), ((42, 34.851), (42, 35.149), (42, 36)))
        self.add_bezier('sym-e32', (42, 36), ((42, 36.376), (42, 36.648), (42, 37)))
        self.add_bezier('sym-e33', (42, 37), ((41.149, 39.504), (37.659, 42), (35, 42)))
        self.add_line('sym-e34', (35, 42), (24, 42))
        self.add_line('sym-e35', (24, 42), (13, 42))
        self.add_bezier('sym-e36', (13, 42), ((10.341, 42), (6.851, 39.504), (6, 37)))
        self.add_bezier('sym-e37', (6, 37), ((6, 36.648), (6, 36.376), (6, 36)))
        self.add_bezier('sym-e38', (6, 36), ((6, 35.149), (6, 34.851), (6, 34)))
        self.add_line('sym-e39', (6, 34), (8, 26))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c1', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c2', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
