'Square turning arrows: matched quarter-circle corners and arrowheads, rebuilt on a square envelope to remove vertical stretch.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5daad2a0-1899-447f-a4db-7072ef776e5c'
SOURCE_PATH = 'pictographic-primitives/combination/arrow square_5daad2a0-1899-447f-a4db-7072ef776e5c.svg'
AUTHOR = 'gpt-6'

class ArrowSquare(Solo48):
    icon_id = 'arrow-square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'combination'
    categories = ('combination', 'primitives')
    aliases = ()
    keywords = ('arrow', 'square', 'combination')

    def build(self) -> None:
        # Square is the natural envelope of the two equal turning arrows.
        self.add_line('upper-side',(6,30),(6,16))
        self.add_arc('upper-turn',(6,16),(10,12),radius_x=4)
        self.add_line('upper-run',(10,12),(36,12))
        self.add_contour('upper','upper-side','upper-turn','upper-run')
        self.add_polyline('upper-head',(30,6),(36,12),(30,18))
        self.relate('connect','upper','upper-head')
        self.add_line('lower-side',(42,18),(42,32))
        self.add_arc('lower-turn',(42,32),(38,36),radius_x=4)
        self.add_line('lower-run',(38,36),(12,36))
        self.add_contour('lower','lower-side','lower-turn','lower-run')
        self.add_polyline('lower-head',(18,30),(12,36),(18,42))
        self.relate('connect','lower','lower-head')
