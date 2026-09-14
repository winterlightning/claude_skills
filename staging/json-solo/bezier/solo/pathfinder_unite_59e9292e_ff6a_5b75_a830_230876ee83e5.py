"""Pathfinder unite (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59e9292e-ff6a-5b75-a830-230876ee83e5'
SOURCE_PATH = 'icons-json/design/pathfinder unite_59e9292e-ff6a-5b75-a830-230876ee83e5.json'
AUTHOR = 'json_to_solo'

class PathfinderUniteDesign(Solo48):
    icon_id = 'pathfinder-unite-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'unite', 'design')

    def build(self):
        self.add_line('e0', (28, 15), (28, 8))
        self.add_line('e1', (26, 6), (9, 6))
        self.add_line('e2', (6, 8), (6, 27))
        self.add_line('e3', (7, 29), (17, 29))
        self.add_line('e4', (18, 31), (18, 40))
        self.add_line('e5', (20, 42), (40, 42))
        self.add_line('e6', (42, 40), (42, 21))
        self.add_line('e7', (40, 18), (29, 18))
        self.add_bezier('e8', (28, 8), ((28, 7.018), (26.736, 6.254), (26, 6)))
        self.add_bezier('e9', (9, 6), ((8.746, 6), (8.774, 6.008), (8.52, 6.008)), ((7.571, 6.008), (7.023, 6.065), (6.335, 6.72)), ((6.237, 6.818), (6, 7.015), (6, 7.17)), ((6, 7.325), (6, 7.845), (6, 8)))
        self.add_bezier('e10', (6, 27), ((6, 27.123), (6.008, 27.51), (6.008, 27.633)), ((6.008, 28.295), (6.558, 28.607), (7, 29)))
        self.add_bezier('e11', (17, 29), ((18.055, 29.499), (17.534, 29.912), (18, 31)))
        self.add_bezier('e12', (18, 40), ((18.425, 41.088), (18.912, 41.583), (20, 42)))
        self.add_bezier('e13', (40, 42), ((40.131, 42), (39.807, 42), (39.938, 41.992)), ((40.887, 41.992), (41.992, 41.1), (41.992, 40.11)), ((41.992, 40.053), (42, 39.987), (42, 39.922)), ((42, 39.799), (42, 40.123), (42, 40)))
        self.add_bezier('e14', (42, 21), ((42, 20.869), (42, 20.474), (41.992, 20.343)), ((41.992, 19.418), (41.165, 18.445), (40.274, 18.24)), ((40.004, 18.183), (40.254, 18), (40, 18)))
        self.add_bezier('e15', (29, 18), ((28.468, 16.977), (28, 16.186), (28, 15)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4', 'e12', 'e5', 'e13', 'e6', 'e14', 'e7', 'e15', closed=True)
