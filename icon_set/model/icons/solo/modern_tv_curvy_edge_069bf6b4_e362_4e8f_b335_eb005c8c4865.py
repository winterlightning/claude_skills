"""Modern tv curvy edge (tv), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '069bf6b4-e362-4e8f-b335-eb005c8c4865'
SOURCE_PATH = 'icons-json/tv/modern tv curvy edge_069bf6b4-e362-4e8f-b335-eb005c8c4865.json'
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
        self.add_line('sym-e0', (24, 32), (24, 38))
        self.add_line('sym-e1', (24, 38), (17, 40))
        self.add_arc('sym-e2', (9, 32), (4, 29), radius_x=4)
        self.add_line('sym-e3', (4, 29), (4, 28))
        self.add_line('sym-e4', (4, 28), (4, 27))
        self.add_line('sym-e5', (4, 27), (4, 12))
        self.add_arc('sym-e7', (4, 12), (8, 8), radius_x=4)
        self.add_line('sym-e8', (8, 8), (9, 8))
        self.add_line('sym-e10', (9, 8), (24, 8))
        self.add_line('sym-e11', (24, 8), (39, 8))
        self.add_line('sym-e13', (39, 8), (40, 8))
        self.add_arc('sym-e14', (40, 8), (44, 12), radius_x=4)
        self.add_line('sym-e16', (44, 12), (44, 27))
        self.add_arc('sym-e17', (44, 27), (44, 28), radius_x=31, sweep=False)
        self.add_line('sym-e18', (44, 28), (44, 29))
        self.add_arc('sym-e19', (44, 29), (39, 32), radius_x=4)
        self.add_line('sym-e20', (39, 32), (24, 32))
        self.add_line('sym-e21', (24, 32), (9, 32))
        self.add_line('sym-e22', (24, 38), (31, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
        self.add_contour('sym-c2', 'sym-e22')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
