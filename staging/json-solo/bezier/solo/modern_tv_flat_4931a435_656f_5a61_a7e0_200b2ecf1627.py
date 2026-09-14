"""Modern tv flat (tv), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4931a435-656f-5a61-a7e0-200b2ecf1627'
SOURCE_PATH = 'icons-json/tv/modern tv flat_4931a435-656f-5a61-a7e0-200b2ecf1627.json'
AUTHOR = 'json_to_solo'

class ModernTvFlatTv(Solo48):
    icon_id = 'modern-tv-flat-tv'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('modern', 'tv', 'flat')

    def build(self):
        self.add_line('sym-e0', (24, 34), (24, 40))
        self.add_line('sym-e1', (24, 40), (14, 40))
        self.add_line('sym-e2', (24, 8), (12, 8))
        self.add_bezier('sym-e3', (12, 8), ((10.191, 8), (8.809, 8), (7, 8)))
        self.add_bezier('sym-e4', (7, 8), ((5.7, 8), (4, 9.53), (4, 11)))
        self.add_bezier('sym-e5', (4, 11), ((4, 11.22), (4, 11.78), (4, 12)))
        self.add_bezier('sym-e6', (4, 12), ((4, 12.15), (4, 11.85), (4, 12)))
        self.add_line('sym-e7', (4, 12), (4, 29))
        self.add_bezier('sym-e8', (4, 29), ((4, 29.52), (4, 30.48), (4, 31)))
        self.add_bezier('sym-e9', (4, 31), ((4, 33.95), (6.873, 34), (9, 34)))
        self.add_line('sym-e10', (9, 34), (24, 34))
        self.add_line('sym-e11', (24, 34), (39, 34))
        self.add_bezier('sym-e12', (39, 34), ((41.127, 34), (44, 33.95), (44, 31)))
        self.add_bezier('sym-e13', (44, 31), ((44, 30.48), (44, 29.52), (44, 29)))
        self.add_line('sym-e14', (44, 29), (44, 12))
        self.add_bezier('sym-e15', (44, 12), ((44, 11.85), (44, 12.15), (44, 12)))
        self.add_bezier('sym-e16', (44, 12), ((44, 11.78), (44, 11.22), (44, 11)))
        self.add_bezier('sym-e17', (44, 11), ((44, 9.53), (42.3, 8), (41, 8)))
        self.add_bezier('sym-e18', (41, 8), ((39.191, 8), (37.809, 8), (36, 8)))
        self.add_line('sym-e19', (36, 8), (24, 8))
        self.add_line('sym-e20', (34, 40), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
        self.add_contour('sym-c2', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
