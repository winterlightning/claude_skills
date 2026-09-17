"""Chicken Biryani Rice Bowl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a45a2c2-48bb-46eb-8254-41a46db5b27d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chicken biryani muslim yellow rice with chicken_1a45a2c2-48bb-46eb-8254-41a46db5b27d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chicken-biryani-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('biryani', 'chicken', 'rice', 'bowl', 'meal', 'drumstick', 'food')

    def build(self):
        # Plan: Rice bowl with diagonal chicken piece resting on rim. Lucide drumstick and salad. Rice grains and second garnish omitted. Envelope (6,6)-(42,42).
        self.add_polyline('rim',(6,30),(26,30),(42,30))
        self.add_bezier('bowl',(42,30),((42,37),(34,42),(24,42)),((14,42),(6,37),(6,30)))
        self.relate('connect','bowl','rim')
        self.add_bezier('meat',(14,6),((20,6),(23,12),(22,18)),((22,20),(20,22),(18,22)),((12,22),(6,18),(6,14)),((6,9),(9,6),(14,6)))
        self.add_contour('chicken','meat',closed=True)
        self.add_line('bone',(18,22),(26,30));self.relate('connect','bone','chicken');self.relate('connect','bone','rim')
        self.add_bezier('rice',(32,16),((38,16),(42,23),(42,30)));self.relate('connect','rice','rim');self.relate('connect','rice','bowl')
