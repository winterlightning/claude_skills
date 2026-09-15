"""Person with Cocktail. Bust extends its arm toward a triangular cocktail bowl; retain round garnish, short stem and base. Rightward pose.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d337eec-e9ef-4a5d-893b-28700ef1496e'
SOURCE_PATH = 'pictographic-primitives/recreation/drinking_4d337eec-e9ef-4a5d-893b-28700ef1496e.svg'
AUTHOR = 'gpt-6'


class PersonWithCocktail(Solo48):
    icon_id = 'person-with-cocktail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('person', 'with', 'cocktail')

    def build(self) -> None:
        self.add_arc('head-top', (7, 17), (15, 17), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-bottom', (15, 17), (7, 17), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('person-1', (6, 42), (6, 34))
        self.add_line('person-2', (6, 34), (12, 30))
        self.add_line('person-3', (12, 30), (18, 32))
        self.add_line('person-4', (18, 32), (22, 40))
        self.add_line('person-5', (22, 40), (33, 40))
        self.add_contour('person', 'person-1', 'person-2', 'person-3', 'person-4', 'person-5', closed=False)
        self.add_line('glass-1', (24, 19), (42, 19))
        self.add_line('glass-2', (42, 19), (33, 31))
        self.add_line('glass-3', (33, 31), (24, 19))
        self.add_contour('glass', 'glass-1', 'glass-2', 'glass-3', closed=True)
        self.add_line('stem', (33, 31), (33, 40))
        self.relate("connect", 'glass', 'stem')
        self.add_line('foot', (33, 40), (40, 40))
        self.relate("connect", 'stem', 'foot')
        self.relate("connect", 'person', 'stem')
        self.relate("connect", 'person', 'foot')
        self.add_arc('garnish-top', (31, 8), (35, 8), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('garnish-bottom', (35, 8), (31, 8), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('garnish', 'garnish-top', 'garnish-bottom', closed=True)
