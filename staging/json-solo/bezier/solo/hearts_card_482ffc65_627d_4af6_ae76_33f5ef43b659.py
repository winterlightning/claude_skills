"""Hearts card (entertainment), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '482ffc65-627d-4af6-ae76-33f5ef43b659'
SOURCE_PATH = 'icons-json/entertainment/hearts card_482ffc65-627d-4af6-ae76-33f5ef43b659.json'
AUTHOR = 'json_to_solo'

class HeartsCardEntertainment(Solo48):
    icon_id = 'hearts-card-entertainment'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('hearts', 'card', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (24, 39), (24, 40))
        self.add_line('sym-e1', (24, 40), (41, 24))
        self.add_bezier('sym-e2', (41, 24), ((42.427, 22.678), (44, 19.886), (44, 18)))
        self.add_bezier('sym-e3', (44, 18), ((44, 17.874), (43.991, 18.118), (44, 18)))
        self.add_bezier('sym-e4', (44, 18), ((44, 17.882), (44, 17.118), (44, 17)))
        self.add_bezier('sym-e5', (44, 17), ((44, 12.175), (39.155, 8), (34, 8)))
        self.add_bezier('sym-e6', (34, 8), ((33.864, 8), (33.136, 8), (33, 8)))
        self.add_bezier('sym-e7', (33, 8), ((32.736, 8), (33.264, 8), (33, 8)))
        self.add_bezier('sym-e8', (33, 8), ((30.609, 8), (27.736, 9.56), (26, 11)))
        self.add_bezier('sym-e9', (26, 11), ((25.364, 11.531), (24.673, 11.528), (24, 12)))
        self.add_bezier('sym-e10', (24, 12), ((23.873, 11.975), (24.127, 12), (24, 12)))
        self.add_bezier('sym-e11', (24, 12), ((23.873, 12), (24.127, 11.975), (24, 12)))
        self.add_bezier('sym-e12', (24, 12), ((23.327, 11.528), (22.636, 11.531), (22, 11)))
        self.add_bezier('sym-e13', (22, 11), ((20.264, 9.56), (17.391, 8), (15, 8)))
        self.add_bezier('sym-e14', (15, 8), ((14.736, 8), (15.264, 8), (15, 8)))
        self.add_bezier('sym-e15', (15, 8), ((14.864, 8), (14.136, 8), (14, 8)))
        self.add_bezier('sym-e16', (14, 8), ((8.845, 8), (4, 12.175), (4, 17)))
        self.add_bezier('sym-e17', (4, 17), ((4, 17.118), (4, 17.882), (4, 18)))
        self.add_bezier('sym-e18', (4, 18), ((4.009, 18.118), (4, 17.874), (4, 18)))
        self.add_bezier('sym-e19', (4, 18), ((4, 19.886), (5.573, 22.678), (7, 24)))
        self.add_line('sym-e20', (7, 24), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
