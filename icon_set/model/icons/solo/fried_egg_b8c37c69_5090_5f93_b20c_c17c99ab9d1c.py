'Fried egg: smooth asymmetric white with aligned cubic tangents and a circular yolk. Lucide egg-fried informs the broad flowing lobes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8c37c69-5090-5f93-b20c-c17c99ab9d1c'
SOURCE_PATH = 'pictographic-primitives/food/fried egg_b8c37c69-5090-5f93-b20c-c17c99ab9d1c.svg'
AUTHOR = 'gpt-6'

class FriedEgg(Solo48):
    icon_id = 'fried-egg'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('fried', 'egg', 'food')

    def build(self) -> None:
        # Lucide egg-fried: broad asymmetric lobes, not faceted short segments.
        # Cardinal knots land exactly on the SQUARE envelope; tangents agree at every join.
        self.add_bezier('white',(24,6),((31,6),(32,13),(36,17)),((40,21),(42,23),(42,28)),((42,35),(34,36),(29,39)),((26,40.8),(25,42),(22,42)),((16,42),(15,36),(11,33)),((7,30),(6,28),(6,24)),((6,19),(11,17),(14,13)),((17,9),(18,6),(24,6)))
        self.add_contour('outline','white',closed=True)

        self.add_arc('yolk-top', (19,24), (29,24), radius_x=5, radius_y=5)
        self.add_arc('yolk-bottom', (29,24), (19,24), radius_x=5, radius_y=5)
        self.add_contour('yolk', 'yolk-top', 'yolk-bottom', closed=True)
