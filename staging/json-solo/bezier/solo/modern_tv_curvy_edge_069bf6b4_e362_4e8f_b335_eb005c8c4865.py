"""Modern tv curvy edge (tv), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '069bf6b4-e362-4e8f-b335-eb005c8c4865'
SOURCE_PATH = 'icons-json/tv/modern tv curvy edge_069bf6b4-e362-4e8f-b335-eb005c8c4865.json'
AUTHOR = 'json_to_solo'

class ModernTvCurvyEdge069bf6b4(Solo48):
    icon_id = 'modern-tv-curvy-edge-069bf6b4'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('modern', 'tv', 'curvy', 'edge')

    def build(self):
        self.add_line('sym-e0', (24, 32), (24, 38))
        self.add_line('sym-e1', (24, 38), (17, 40))
        self.add_bezier('sym-e2', (9, 32), ((6.864, 32), (4, 31.232), (4, 29)))
        self.add_bezier('sym-e3', (4, 29), ((4, 28.638), (4, 28.362), (4, 28)))
        self.add_bezier('sym-e4', (4, 28), ((4, 27.587), (4, 27.413), (4, 27)))
        self.add_line('sym-e5', (4, 27), (4, 12))
        self.add_bezier('sym-e6', (4, 12), ((4, 11.773), (4, 12.227), (4, 12)))
        self.add_bezier('sym-e7', (4, 12), ((4, 10.063), (5.964, 8), (8, 8)))
        self.add_bezier('sym-e8', (8, 8), ((8.264, 8), (8.745, 8), (9, 8)))
        self.add_bezier('sym-e9', (9, 8), ((9.245, 8), (8.755, 8), (9, 8)))
        self.add_line('sym-e10', (9, 8), (24, 8))
        self.add_line('sym-e11', (24, 8), (39, 8))
        self.add_bezier('sym-e12', (39, 8), ((39.245, 8), (38.755, 8), (39, 8)))
        self.add_bezier('sym-e13', (39, 8), ((39.255, 8), (39.736, 8), (40, 8)))
        self.add_bezier('sym-e14', (40, 8), ((42.036, 8), (44, 10.063), (44, 12)))
        self.add_bezier('sym-e15', (44, 12), ((44, 12.227), (44, 11.773), (44, 12)))
        self.add_line('sym-e16', (44, 12), (44, 27))
        self.add_bezier('sym-e17', (44, 27), ((44, 27.413), (44, 27.587), (44, 28)))
        self.add_bezier('sym-e18', (44, 28), ((44, 28.362), (44, 28.638), (44, 29)))
        self.add_bezier('sym-e19', (44, 29), ((44, 31.232), (41.136, 32), (39, 32)))
        self.add_line('sym-e20', (39, 32), (24, 32))
        self.add_line('sym-e21', (24, 32), (9, 32))
        self.add_line('sym-e22', (24, 38), (31, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
        self.add_contour('sym-c2', 'sym-e22')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
