'Two blossom vase: round paired flower heads and continuous semicircular pot base fit VRECT_L exactly.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17b4e4f0-64b5-500d-a432-783026ce580b'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/decoration cherry blossom vase_17b4e4f0-64b5-500d-a432-783026ce580b.svg'
AUTHOR = 'gpt-6'

class TwoBlossomVase(Solo48):
    icon_id = 'two-blossom-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'blossom', 'flowers', 'stems', 'cherry', 'bouquet', 'decor')

    def build(self) -> None:
        self.add_arc('left-flower-top', (8,9), (18,9), radius_x=5, radius_y=5)
        self.add_arc('left-flower-bottom', (18,9), (8,9), radius_x=5, radius_y=5)
        self.add_contour('left-flower', 'left-flower-top', 'left-flower-bottom', closed=True)

        self.add_arc('right-flower-top', (30,9), (40,9), radius_x=5, radius_y=5)
        self.add_arc('right-flower-bottom', (40,9), (30,9), radius_x=5, radius_y=5)
        self.add_contour('right-flower', 'right-flower-top', 'right-flower-bottom', closed=True)

        self.add_polyline('left-stem',(13,14),(24,29))
        self.add_polyline('right-stem',(35,14),(24,29))
        self.relate('connect','left-stem','left-flower')
        self.relate('connect','right-stem','right-flower')
        self.relate('connect','left-stem','right-stem')
        self.add_polyline('rim',(16,29),(24,29),(32,29))
        self.add_line('pot-right',(32,29),(32,36))
        self.add_arc('base',(32,36),(16,36),radius_x=8)
        self.add_line('pot-left',(16,36),(16,29))
        self.add_contour('pot','pot-right','base','pot-left')
        self.relate('connect','pot','rim')
        self.relate('connect','left-stem','rim')
        self.relate('connect','right-stem','rim')
