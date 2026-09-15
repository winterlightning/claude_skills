"""Theater (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d45686f-eb83-4870-bb8b-43def157a239'
SOURCE_PATH = 'pictographic-primitives/symbol/theater_3d45686f-eb83-4870-bb8b-43def157a239.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Theater(Solo48):
    icon_id = 'theater'
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
        self.add_line('sym-e4', (35, 40), (34, 39))
        self.add_line('sym-e5', (34, 39), (34, 37))
        self.add_arc('sym-e6', (34, 37), (38, 30), radius_x=9)
        self.add_line('sym-e7', (38, 30), (41, 28))
        self.add_arc('sym-e8', (41, 28), (26, 16), radius_x=23)
        self.add_line('sym-e9', (26, 16), (24, 13))
        self.add_line('sym-e10', (24, 13), (22, 16))
        self.add_arc('sym-e11', (22, 16), (7, 28), radius_x=22)
        self.add_line('sym-e12', (7, 28), (10, 30))
        self.add_arc('sym-e13', (10, 30), (14, 37), radius_x=9)
        self.add_line('sym-e14', (14, 37), (14, 39))
        self.add_line('sym-e15', (14, 39), (13, 40))
        self.add_line('sym-e16', (13, 40), (4, 40))
        self.add_line('sym-e17', (4, 40), (4, 8))
        self.add_line('sym-e18', (4, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
