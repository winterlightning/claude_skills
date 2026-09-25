"""Pathfinder unite (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '59e9292e-ff6a-5b75-a830-230876ee83e5'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder unite_59e9292e-ff6a-5b75-a830-230876ee83e5.svg'
AUTHOR = 'gpt-6'

class PathfinderUnite(Solo48):
    icon_id = 'pathfinder-unite'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('pathfinder', 'unite', 'design')

    def build(self):
        self.add_line('e0', (28, 15), (28, 8))
        self.add_line('e1', (26, 6), (9, 6))
        self.add_line('e3', (7, 29), (17, 29))
        self.add_line('e4', (18, 31), (18, 40))
        self.add_line('e5', (20, 42), (40, 42))
        self.add_line('e6', (42, 40), (42, 21))
        self.add_line('e7', (40, 18), (29, 18))
        self.add_arc('e8', (28, 8), (26, 6), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e9-1', (9, 6), (6, 7))
        self.add_line('e9-2', (6, 7), (6, 27))
        self.add_line('e10', (6, 27), (7, 29))
        self.add_line('e11', (17, 29), (18, 31))
        self.add_line('e12', (18, 40), (20, 42))
        self.add_arc('e13', (40, 42), (42, 40), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e14', (42, 21), (40, 18))
        self.add_arc('e15', (29, 18), (28, 15), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9-1', 'e9-2', 'e10', 'e3', 'e11', 'e4', 'e12', 'e5', 'e13', 'e6', 'e14', 'e7', 'e15', closed=True)
