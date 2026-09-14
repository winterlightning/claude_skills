"""Modern tv curvy edge (tv), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa5afd06-b67a-40c6-a33a-401cad8e01a9'
SOURCE_PATH = 'icons-json/tv/modern tv curvy edge_fa5afd06-b67a-40c6-a33a-401cad8e01a9.json'
AUTHOR = 'json_to_solo'

class ModernTvCurvyEdge(Solo48):
    icon_id = 'modern-tv-curvy-edge'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('modern', 'tv', 'curvy', 'edge')

    def build(self):
        self.add_line('sym-e0', (24, 34), (24, 38))
        self.add_line('sym-e1', (24, 38), (17, 40))
        self.add_bezier('sym-e2', (9, 34), ((7.009, 34), (4, 32.64), (4, 30)))
        self.add_bezier('sym-e3', (4, 30), ((4, 29.72), (4, 29.28), (4, 29)))
        self.add_bezier('sym-e4', (4, 29), ((4, 28.52), (4, 28.48), (4, 28)))
        self.add_line('sym-e5', (4, 28), (4, 13))
        self.add_bezier('sym-e6', (4, 13), ((4, 12.71), (4, 12.29), (4, 12)))
        self.add_bezier('sym-e7', (4, 12), ((4, 9.26), (6.836, 8), (9, 8)))
        self.add_bezier('sym-e8', (9, 8), ((9.245, 8), (8.755, 8), (9, 8)))
        self.add_line('sym-e9', (9, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (39, 8))
        self.add_bezier('sym-e11', (39, 8), ((39.245, 8), (38.755, 8), (39, 8)))
        self.add_bezier('sym-e12', (39, 8), ((41.164, 8), (44, 9.26), (44, 12)))
        self.add_bezier('sym-e13', (44, 12), ((44, 12.29), (44, 12.71), (44, 13)))
        self.add_line('sym-e14', (44, 13), (44, 28))
        self.add_bezier('sym-e15', (44, 28), ((44, 28.48), (44, 28.52), (44, 29)))
        self.add_bezier('sym-e16', (44, 29), ((44, 29.28), (44, 29.72), (44, 30)))
        self.add_bezier('sym-e17', (44, 30), ((44, 32.64), (40.991, 34), (39, 34)))
        self.add_line('sym-e18', (39, 34), (24, 34))
        self.add_line('sym-e19', (24, 34), (9, 34))
        self.add_line('sym-e20', (24, 38), (31, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
        self.add_contour('sym-c2', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
