"""U turn left (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a392fc8f-838e-40fb-a666-e78597be5c78'
SOURCE_PATH = 'pictographic-primitives/transportation/u turn left_a392fc8f-838e-40fb-a666-e78597be5c78.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class UTurnLeft(Solo48):
    icon_id = 'u-turn-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('u', 'turn', 'left', 'transportation')

    def build(self):
        self.add_line('e0', (13, 21), (13, 33))
        self.add_line('e1', (6, 25), (13, 33))
        self.add_line('e2', (13, 33), (23, 25))
        self.add_bezier('e3', (42, 42), ((42, 41.869), (41.984, 41.746), (41.984, 41.615)), ((41.984, 37.402), (41.984, 33.18), (41.984, 28.958)), ((41.984, 28.647), (42, 28.336), (42, 28.025)), ((42, 27.175), (41.984, 26.324), (41.984, 25.481)), ((41.984, 22.388), (41.992, 17.667), (41.002, 14.795)), ((39.537, 10.516), (35.847, 7.718), (31.593, 6.565)), ((30.496, 6.27), (29.392, 6.016), (28.255, 6.016)), ((27.981, 6.016), (27.699, 6), (27.425, 6)), ((27.421, 6), (27.416, 6), (27.412, 6)), ((27.109, 6), (26.815, 6.016), (26.512, 6.016)), ((25.718, 6.016), (24.884, 6.229), (24.115, 6.401)), ((17.52, 7.833), (13, 14.455), (13, 21)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
