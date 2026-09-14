"""Theater (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d45686f-eb83-4870-bb8b-43def157a239'
SOURCE_PATH = 'icons-json/symbol/theater_3d45686f-eb83-4870-bb8b-43def157a239.json'
AUTHOR = 'json_to_solo'

class TheaterSymbol(Solo48):
    icon_id = 'theater-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('theater', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 13), (24, 8))
        self.add_line('sym-e1', (24, 8), (44, 8))
        self.add_line('sym-e2', (44, 8), (44, 40))
        self.add_line('sym-e3', (44, 40), (35, 40))
        self.add_bezier('sym-e4', (35, 40), ((34.809, 39.823), (34.182, 39.185), (34, 39)))
        self.add_bezier('sym-e5', (34, 39), ((33.727, 38.697), (34.009, 37.421), (34, 37)))
        self.add_bezier('sym-e6', (34, 37), ((33.973, 34.853), (35.764, 31.036), (38, 30)))
        self.add_line('sym-e7', (38, 30), (41, 28))
        self.add_bezier('sym-e8', (41, 28), ((33.855, 26.131), (29.318, 22.147), (26, 16)))
        self.add_line('sym-e9', (26, 16), (24, 13))
        self.add_line('sym-e10', (24, 13), (22, 16))
        self.add_bezier('sym-e11', (22, 16), ((18.682, 22.147), (14.145, 26.131), (7, 28)))
        self.add_line('sym-e12', (7, 28), (10, 30))
        self.add_bezier('sym-e13', (10, 30), ((12.236, 31.036), (14.027, 34.853), (14, 37)))
        self.add_bezier('sym-e14', (14, 37), ((13.991, 37.421), (14.273, 38.697), (14, 39)))
        self.add_bezier('sym-e15', (14, 39), ((13.818, 39.185), (13.191, 39.823), (13, 40)))
        self.add_line('sym-e16', (13, 40), (4, 40))
        self.add_line('sym-e17', (4, 40), (4, 8))
        self.add_line('sym-e18', (4, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
