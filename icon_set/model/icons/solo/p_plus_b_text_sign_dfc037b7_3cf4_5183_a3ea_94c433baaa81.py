"""P plus b text sign; independently authored for SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfc037b7-3cf4-5183-a3ea-94c433baaa81'
SOURCE_PATH = 'pictographic-primitives/transportation/park and bike_dfc037b7-3cf4-5183-a3ea-94c433baaa81.svg'
AUTHOR = 'gpt-6'

class PPlusBTextSign(Solo48):
    icon_id = 'p-plus-b-text-sign'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('park and bike', 'parking', 'bicycle', 'transit', 'text')

    def build(self) -> None:
        # HRECT_L centerline bounds (6,8)-(42,40). Letter bowls share rx=8, ry=8.
        self.add_line('p-stem', (6,40), (6,24))
        self.add_line('p-upright', (6,24), (6,8))
        self.add_arc('p-bowl', (6,8), (6,24), radius_x=8)
        self.add_contour('p-loop', 'p-upright', 'p-bowl', closed=True)
        self.relate('connect', 'p-stem', 'p-loop')
        self.add_line('plus-left', (21,24), (24,24))
        self.add_line('plus-right', (24,24), (27,24))
        self.add_contour('plus-bar', 'plus-left', 'plus-right')
        self.add_polyline('plus-stem', (24,19), (24,24), (24,29))
        self.relate('connect', 'plus-bar', 'plus-stem')
        self.add_line('b-upper-stem', (36,24), (36,8))
        self.add_arc('b-upper-bowl', (36,8), (36,24), radius_x=8)
        self.add_contour('b-upper', 'b-upper-stem', 'b-upper-bowl', closed=True)
        self.add_line('b-lower-stem', (36,40), (36,24))
        self.add_arc('b-lower-bowl', (36,24), (36,40), radius_x=8)
        self.add_contour('b-lower', 'b-lower-stem', 'b-lower-bowl', closed=True)
        self.relate('connect', 'b-upper', 'b-lower')
