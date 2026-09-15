"""Focus square (photography), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2b5acc96-5847-526f-be84-a3382131402b'
SOURCE_PATH = 'icons-json/photography/focus square_2b5acc96-5847-526f-be84-a3382131402b.json'
AUTHOR = 'gpt-6'

class FocusSquare(Solo48):
    icon_id = 'focus-square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('focus', 'square', 'photography')

    def build(self):
        self.add_line('sym-e0', (34, 34), (14, 34))
        self.add_line('sym-e2', (14, 34), (14, 14))
        self.add_line('sym-e4', (14, 14), (34, 14))
        self.add_line('sym-e6', (34, 14), (34, 34))
        self.add_line('sym-e8', (14, 24), (6, 24))
        self.add_line('sym-e9', (6, 24), (6, 8))
        self.add_arc('sym-e11', (6, 8), (8, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e12', (8, 6), (24, 6))
        self.add_line('sym-e13', (24, 6), (24, 14))
        self.add_line('sym-e14', (34, 24), (42, 24))
        self.add_line('sym-e15', (42, 24), (42, 8))
        self.add_arc('sym-e17', (42, 8), (40, 6), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e18', (40, 6), (24, 6))
        self.add_line('sym-e19', (24, 34), (24, 42))
        self.add_line('sym-e20', (24, 42), (8, 42))
        self.add_arc('sym-e21', (8, 42), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e23', (6, 40), (6, 24))
        self.add_arc('sym-e25', (42, 40), (40, 42), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e26', (40, 42), (24, 42))
        self.add_line('sym-e27', (42, 24), (42, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e4', 'sym-e6', closed=True)
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13', closed=False)
        self.add_contour('sym-c2', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', closed=False)
        self.add_contour('sym-c3', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23', closed=False)
        self.add_contour('sym-c4', 'sym-e25', 'sym-e26', closed=False)
        self.add_contour('sym-c5', 'sym-e27', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c5')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c3', 'sym-c4', 'sym-c5')
