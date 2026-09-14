"""Archive (content), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d3380f1-04ae-52fb-a0b2-916fda7e3f13'
SOURCE_PATH = 'icons-json/content/archive_4d3380f1-04ae-52fb-a0b2-916fda7e3f13.json'
AUTHOR = 'json_to_solo'

class Archive4d3380f1(Solo48):
    icon_id = 'archive-4d3380f1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('archive', 'content')

    def build(self):
        self.add_line('sym-e0', (24, 24), (29, 24))
        self.add_line('sym-e1', (24, 40), (39, 40))
        self.add_bezier('sym-e2', (39, 40), ((39.355, 40), (39.7, 40), (40, 40)))
        self.add_bezier('sym-e3', (40, 40), ((41.536, 39.183), (41, 38.558), (41, 37)))
        self.add_line('sym-e4', (41, 37), (41, 16))
        self.add_bezier('sym-e5', (41, 16), ((41.065, 15.999), (40.934, 16), (41, 16)))
        self.add_bezier('sym-e6', (41, 16), ((41.176, 16), (41.823, 16), (42, 16)))
        self.add_bezier('sym-e7', (42, 16), ((42.588, 16), (43.498, 16.334), (44, 16)))
        self.add_bezier('sym-e8', (44, 16), ((44, 15.874), (43.827, 16.152), (44, 16)))
        self.add_line('sym-e9', (44, 16), (44, 11))
        self.add_bezier('sym-e10', (44, 11), ((44, 10.924), (44, 10.084), (44, 10)))
        self.add_bezier('sym-e11', (44, 10), ((44, 8.644), (42.145, 8.312), (41, 8)))
        self.add_line('sym-e12', (41, 8), (24, 8))
        self.add_line('sym-e13', (24, 8), (7, 8))
        self.add_bezier('sym-e14', (7, 8), ((5.855, 8.312), (4, 8.644), (4, 10)))
        self.add_bezier('sym-e15', (4, 10), ((4, 10.084), (4, 10.924), (4, 11)))
        self.add_line('sym-e16', (4, 11), (4, 16))
        self.add_bezier('sym-e17', (4, 16), ((4.173, 16.152), (4, 15.874), (4, 16)))
        self.add_bezier('sym-e18', (4, 16), ((4.502, 16.334), (5.412, 16), (6, 16)))
        self.add_bezier('sym-e19', (6, 16), ((6.177, 16), (6.824, 16), (7, 16)))
        self.add_bezier('sym-e20', (7, 16), ((7.066, 16), (6.935, 15.999), (7, 16)))
        self.add_line('sym-e21', (7, 16), (7, 37))
        self.add_bezier('sym-e22', (7, 37), ((7, 38.558), (6.464, 39.183), (8, 40)))
        self.add_bezier('sym-e23', (8, 40), ((8.3, 40), (8.645, 40), (9, 40)))
        self.add_line('sym-e24', (9, 40), (24, 40))
        self.add_bezier('sym-e25', (41, 16), ((40.797, 16.006), (41.202, 16), (41, 16)))
        self.add_bezier('sym-e26', (41, 16), ((40.597, 16), (39.406, 16), (39, 16)))
        self.add_line('sym-e27', (39, 16), (24, 16))
        self.add_line('sym-e28', (24, 16), (9, 16))
        self.add_bezier('sym-e29', (9, 16), ((8.594, 16), (7.403, 16), (7, 16)))
        self.add_bezier('sym-e30', (7, 16), ((6.798, 16), (7.203, 16.006), (7, 16)))
        self.add_line('sym-e31', (24, 24), (19, 24))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', closed=True)
        self.add_contour('sym-c2', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30')
        self.add_contour('sym-c3', 'sym-e31')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
