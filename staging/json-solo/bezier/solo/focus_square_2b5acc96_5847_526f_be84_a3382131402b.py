"""Focus square (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b5acc96-5847-526f-be84-a3382131402b'
SOURCE_PATH = 'icons-json/photography/focus square_2b5acc96-5847-526f-be84-a3382131402b.json'
AUTHOR = 'json_to_solo'

class FocusSquarePhotography(Solo48):
    icon_id = 'focus-square-photography'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('focus', 'square', 'photography')

    def build(self):
        self.add_line('sym-e0', (34, 34), (24, 34))
        self.add_line('sym-e1', (24, 34), (14, 34))
        self.add_line('sym-e2', (14, 34), (14, 24))
        self.add_line('sym-e3', (14, 24), (14, 14))
        self.add_line('sym-e4', (14, 14), (24, 14))
        self.add_line('sym-e5', (24, 14), (34, 14))
        self.add_line('sym-e6', (34, 14), (34, 24))
        self.add_line('sym-e7', (34, 24), (34, 34))
        self.add_line('sym-e8', (14, 24), (6, 24))
        self.add_line('sym-e9', (6, 24), (6, 8))
        self.add_bezier('sym-e10', (6, 8), ((6, 8), (6, 8), (6, 8)))
        self.add_bezier('sym-e11', (6, 8), ((6, 7.321), (7.329, 6), (8, 6)))
        self.add_line('sym-e12', (8, 6), (24, 6))
        self.add_line('sym-e13', (24, 6), (24, 14))
        self.add_line('sym-e14', (34, 24), (42, 24))
        self.add_line('sym-e15', (42, 24), (42, 8))
        self.add_bezier('sym-e16', (42, 8), ((42, 8), (42, 8), (42, 8)))
        self.add_bezier('sym-e17', (42, 8), ((42, 7.321), (40.671, 6), (40, 6)))
        self.add_line('sym-e18', (40, 6), (24, 6))
        self.add_line('sym-e19', (24, 34), (24, 42))
        self.add_line('sym-e20', (24, 42), (8, 42))
        self.add_bezier('sym-e21', (8, 42), ((7.329, 42), (6, 40.679), (6, 40)))
        self.add_bezier('sym-e22', (6, 40), ((6, 40), (6, 40), (6, 40)))
        self.add_line('sym-e23', (6, 40), (6, 24))
        self.add_bezier('sym-e24', (42, 40), ((42, 40), (42, 40), (42, 40)))
        self.add_bezier('sym-e25', (42, 40), ((42, 40.679), (40.671, 42), (40, 42)))
        self.add_line('sym-e26', (40, 42), (24, 42))
        self.add_line('sym-e27', (42, 24), (42, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', closed=True)
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c3', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.add_contour('sym-c4', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c5', 'sym-e27')
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
