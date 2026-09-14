"""Batch-05/ribbon tie (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8df920a-b5e4-42ca-a8cb-d0665fd4de17'
SOURCE_PATH = 'icons-json/accessories/batch-05/ribbon tie_a8df920a-b5e4-42ca-a8cb-d0665fd4de17.json'
AUTHOR = 'json_to_solo'

class Batch05RibbonTieAccessories(Solo48):
    icon_id = 'batch-05-ribbon-tie-accessories'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'ribbon', 'tie', 'accessories')

    def build(self):
        self.add_line('sym-e0', (13, 24), (19, 24))
        self.add_line('sym-e1', (19, 24), (19, 30))
        self.add_line('sym-e2', (19, 30), (6, 40))
        self.add_bezier('sym-e3', (6, 40), ((5.827, 40), (5.173, 40), (5, 40)))
        self.add_bezier('sym-e4', (5, 40), ((4.6, 40), (4.2, 39.624), (4, 39)))
        self.add_bezier('sym-e5', (4, 39), ((4, 38.776), (4.045, 38.208), (4, 38)))
        self.add_line('sym-e6', (4, 38), (4, 24))
        self.add_line('sym-e7', (4, 24), (4, 10))
        self.add_bezier('sym-e8', (4, 10), ((4.045, 9.792), (4, 9.224), (4, 9)))
        self.add_bezier('sym-e9', (4, 9), ((4.2, 8.376), (4.6, 8), (5, 8)))
        self.add_bezier('sym-e10', (5, 8), ((5.173, 8), (5.827, 8), (6, 8)))
        self.add_line('sym-e11', (6, 8), (19, 18))
        self.add_bezier('sym-e12', (19, 18), ((19.527, 16.304), (20.064, 14.88), (21, 14)))
        self.add_line('sym-e13', (21, 14), (24, 14))
        self.add_line('sym-e14', (24, 14), (27, 14))
        self.add_bezier('sym-e15', (27, 14), ((27.936, 14.88), (28.473, 16.304), (29, 18)))
        self.add_line('sym-e16', (29, 18), (42, 8))
        self.add_bezier('sym-e17', (42, 8), ((42.173, 8), (42.827, 8), (43, 8)))
        self.add_bezier('sym-e18', (43, 8), ((43.4, 8), (43.8, 8.376), (44, 9)))
        self.add_bezier('sym-e19', (44, 9), ((44, 9.224), (43.955, 9.792), (44, 10)))
        self.add_line('sym-e20', (44, 10), (44, 24))
        self.add_line('sym-e21', (44, 24), (44, 38))
        self.add_bezier('sym-e22', (44, 38), ((43.955, 38.208), (44, 38.776), (44, 39)))
        self.add_bezier('sym-e23', (44, 39), ((43.8, 39.624), (43.4, 40), (43, 40)))
        self.add_bezier('sym-e24', (43, 40), ((42.827, 40), (42.173, 40), (42, 40)))
        self.add_line('sym-e25', (42, 40), (29, 30))
        self.add_bezier('sym-e26', (29, 30), ((28.473, 31.696), (27.936, 33.12), (27, 34)))
        self.add_line('sym-e27', (27, 34), (24, 34))
        self.add_line('sym-e28', (24, 34), (21, 34))
        self.add_bezier('sym-e29', (21, 34), ((20.064, 33.12), (19.527, 31.696), (19, 30)))
        self.add_line('sym-e30', (35, 24), (29, 24))
        self.add_line('sym-e31', (29, 24), (29, 30))
        self.add_line('sym-e32', (19, 18), (19, 24))
        self.add_line('sym-e33', (29, 18), (29, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c1', 'sym-e30', 'sym-e31')
        self.add_contour('sym-c2', 'sym-e32')
        self.add_contour('sym-c3', 'sym-e33')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
