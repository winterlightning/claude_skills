"""Rectangle dots (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a85ee0a-25fe-413a-b15f-b957051e288b'
SOURCE_PATH = 'pictographic-primitives/state/rectangle dots_1a85ee0a-25fe-413a-b15f-b957051e288b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class RectangleDots(Solo48):
    icon_id = 'rectangle-dots'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rectangle', 'dots', 'state')

    def build(self):
        self.add_arc('sym-e0', (24, 14), (24, 15), radius_x=16, sweep=False)
        self.add_arc('sym-e1', (24, 32), (24, 33), radius_x=34, sweep=False)
        self.add_line('sym-e2', (40, 10), (40, 6))
        self.add_arc('sym-e4', (40, 6), (38, 4), radius_x=3, sweep=False)
        self.add_line('sym-e6', (38, 4), (30, 4))
        self.add_line('sym-e7', (40, 38), (40, 42))
        self.add_arc('sym-e9', (40, 42), (38, 44), radius_x=2)
        self.add_line('sym-e11', (38, 44), (30, 44))
        self.add_line('sym-e12', (39, 18), (39, 29))
        self.add_line('sym-e13', (8, 10), (8, 6))
        self.add_arc('sym-e15', (8, 6), (10, 4), radius_x=2)
        self.add_line('sym-e17', (10, 4), (18, 4))
        self.add_line('sym-e18', (8, 38), (8, 42))
        self.add_arc('sym-e20', (8, 42), (10, 44), radius_x=2, sweep=False)
        self.add_line('sym-e22', (10, 44), (18, 44))
        self.add_line('sym-e23', (9, 18), (9, 29))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e4', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e9', 'sym-e11')
        self.add_contour('sym-c4', 'sym-e12')
        self.add_contour('sym-c5', 'sym-e13', 'sym-e15', 'sym-e17')
        self.add_contour('sym-c6', 'sym-e18', 'sym-e20', 'sym-e22')
        self.add_contour('sym-c7', 'sym-e23')
