"""Camping tent (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6abce5ce-492a-5630-a30e-c47fb4045166'
SOURCE_PATH = 'icons-json/outdoors/camping tent_6abce5ce-492a-5630-a30e-c47fb4045166.json'
AUTHOR = 'json_to_solo'

class CampingTent6abce5ce(Solo48):
    icon_id = 'camping-tent-6abce5ce'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('camping', 'tent', 'outdoors')

    def build(self):
        self.add_line('sym-e0', (14, 40), (14, 35))
        self.add_bezier('sym-e1', (14, 35), ((14, 33.363), (14.582, 32.489), (15, 31)))
        self.add_bezier('sym-e2', (15, 31), ((16.191, 26.766), (17.782, 21.957), (21, 20)))
        self.add_bezier('sym-e3', (21, 20), ((21.983, 19.398), (23.09, 19), (24, 19)))
        self.add_bezier('sym-e4', (24, 19), ((24.91, 19), (26.017, 19.398), (27, 20)))
        self.add_bezier('sym-e5', (27, 20), ((30.218, 21.957), (31.809, 26.766), (33, 31)))
        self.add_bezier('sym-e6', (33, 31), ((33.418, 32.489), (34, 33.363), (34, 35)))
        self.add_line('sym-e7', (34, 35), (34, 40))
        self.add_line('sym-e8', (34, 40), (44, 40))
        self.add_bezier('sym-e9', (44, 40), ((43.273, 35.791), (42.336, 31.938), (41, 28)))
        self.add_bezier('sym-e10', (41, 28), ((38.001, 19.142), (31.923, 8), (24, 8)))
        self.add_bezier('sym-e11', (24, 8), ((16.077, 8), (9.999, 19.142), (7, 28)))
        self.add_bezier('sym-e12', (7, 28), ((5.664, 31.938), (4.727, 35.791), (4, 40)))
        self.add_line('sym-e13', (4, 40), (14, 40))
        self.add_line('sym-e14', (14, 40), (24, 40))
        self.add_line('sym-e15', (24, 40), (34, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
