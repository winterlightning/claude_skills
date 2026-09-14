"""Batch-04/hat cowboy (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '102a699a-efb8-5111-a65a-a03761946e2d'
SOURCE_PATH = 'icons-json/accessories/batch-04/hat cowboy_102a699a-efb8-5111-a65a-a03761946e2d.json'
AUTHOR = 'json_to_solo'

class Batch04HatCowboy(Solo48):
    icon_id = 'batch-04-hat-cowboy'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'cowboy', 'accessories')

    def build(self):
        self.add_bezier('sym-e0', (24, 11), ((23.94, 11), (24.061, 11.007), (24, 11)))
        self.add_bezier('sym-e1', (24, 11), ((22.491, 10.815), (21.436, 8), (20, 8)))
        self.add_bezier('sym-e2', (20, 8), ((19.864, 8), (19.136, 8.012), (19, 8)))
        self.add_bezier('sym-e3', (19, 8), ((18.864, 8.012), (19.136, 8), (19, 8)))
        self.add_bezier('sym-e4', (19, 8), ((16.682, 8), (15.4, 12.551), (15, 15)))
        self.add_line('sym-e5', (15, 15), (13, 26))
        self.add_bezier('sym-e6', (13, 26), ((16.116, 27.089), (20.105, 28), (24, 28)))
        self.add_bezier('sym-e7', (24, 28), ((27.895, 28), (31.884, 27.089), (35, 26)))
        self.add_line('sym-e8', (35, 26), (33, 15))
        self.add_bezier('sym-e9', (33, 15), ((32.6, 12.551), (31.318, 8), (29, 8)))
        self.add_bezier('sym-e10', (29, 8), ((28.864, 8), (29.136, 8.012), (29, 8)))
        self.add_bezier('sym-e11', (29, 8), ((28.864, 8.012), (28.136, 8), (28, 8)))
        self.add_bezier('sym-e12', (28, 8), ((26.564, 8), (25.509, 10.815), (24, 11)))
        self.add_bezier('sym-e13', (24, 11), ((23.939, 11.007), (24.06, 11), (24, 11)))
        self.add_line('sym-e14', (10, 25), (7, 22))
        self.add_bezier('sym-e15', (7, 22), ((6.645, 21.902), (6.373, 20.963), (6, 21)))
        self.add_bezier('sym-e16', (6, 21), ((5.073, 21.086), (4, 22.769), (4, 24)))
        self.add_bezier('sym-e17', (4, 24), ((4, 24.185), (4, 23.815), (4, 24)))
        self.add_bezier('sym-e18', (4, 24), ((4, 24.209), (4, 24.791), (4, 25)))
        self.add_bezier('sym-e19', (4, 25), ((4, 27.068), (6.045, 29.597), (7, 31)))
        self.add_bezier('sym-e20', (7, 31), ((10.073, 35.505), (14.555, 38.978), (19, 40)))
        self.add_bezier('sym-e21', (19, 40), ((19.582, 40), (19.4, 40), (20, 40)))
        self.add_line('sym-e22', (20, 40), (24, 40))
        self.add_line('sym-e23', (24, 40), (28, 40))
        self.add_bezier('sym-e24', (28, 40), ((28.6, 40), (28.418, 40), (29, 40)))
        self.add_bezier('sym-e25', (29, 40), ((33.445, 38.978), (37.927, 35.505), (41, 31)))
        self.add_bezier('sym-e26', (41, 31), ((41.955, 29.597), (44, 27.068), (44, 25)))
        self.add_bezier('sym-e27', (44, 25), ((44, 24.791), (44, 24.209), (44, 24)))
        self.add_bezier('sym-e28', (44, 24), ((44, 23.815), (44, 24.185), (44, 24)))
        self.add_bezier('sym-e29', (44, 24), ((44, 22.769), (42.927, 21.086), (42, 21)))
        self.add_bezier('sym-e30', (42, 21), ((41.627, 20.963), (41.355, 21.902), (41, 22)))
        self.add_line('sym-e31', (41, 22), (38, 25))
        self.add_bezier('sym-e32', (38, 25), ((37.3, 25.702), (35.818, 25.717), (35, 26)))
        self.add_bezier('sym-e33', (13, 26), ((12.182, 25.717), (10.7, 25.702), (10, 25)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=True)
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32')
        self.add_contour('sym-c2', 'sym-e33')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
