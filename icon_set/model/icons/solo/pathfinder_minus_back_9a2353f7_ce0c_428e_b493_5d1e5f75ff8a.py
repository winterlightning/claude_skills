"""Pathfinder minus back (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a2353f7-ce0c-428e-b493-5d1e5f75ff8a'
SOURCE_PATH = 'icons-json/design/pathfinder minus back_9a2353f7-ce0c-428e-b493-5d1e5f75ff8a.json'
AUTHOR = 'gpt-6'

class PathfinderMinusBack(Solo48):
    icon_id = 'pathfinder-minus-back'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'minus', 'back', 'design')

    def build(self):
        self.add_line('e0', (18, 30), (18, 20))
        self.add_line('e1', (19, 18), (29, 18))
        self.add_line('e2', (18, 30), (29, 30))
        self.add_line('e3', (29, 29), (29, 18))
        self.add_line('e4', (18, 30), (16, 30))
        self.add_line('e5', (29, 18), (29, 16))
        self.add_line('e6', (16, 30), (16, 38))
        self.add_line('e7', (17, 40), (42, 40))
        self.add_line('e8', (44, 38), (44, 17))
        self.add_line('e9', (42, 16), (29, 16))
        self.add_line('e10', (16, 30), (6, 30))
        self.add_line('e11', (4, 29), (4, 10))
        self.add_line('e12', (6, 8), (29, 8))
        self.add_line('e14', (18, 20), (19, 18))
        self.add_arc('e15', (29, 30), (29, 29), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e16', (16, 38), (17, 40), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('e17', (42, 40), (44, 38), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e18', (44, 17), (42, 16))
        self.add_arc('e19', (6, 30), (4, 29), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e20', (4, 10), (6, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('e21', (29, 8), (29, 16))
        self.add_contour('c0', 'e0', 'e14', 'e1', closed=False)
        self.add_contour('c1', 'e2', 'e15', 'e3', closed=False)
        self.add_contour('c2', 'e4', closed=False)
        self.add_contour('c3', 'e5', closed=False)
        self.add_contour('c4', 'e6', 'e16', 'e7', 'e17', 'e8', 'e18', 'e9', closed=False)
        self.add_contour('c5', 'e10', 'e19', 'e11', 'e20', 'e12', 'e21', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
