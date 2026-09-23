"""Crossed Fork and Spoon."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53cd4f82-ae5a-4f7a-8ddd-de64747944f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/symbol spoon cross fork_53cd4f82-ae5a-4f7a-8ddd-de64747944f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-fork-with-spoon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('fork', 'spoon', 'cutlery', 'crossed', 'dining', 'utensil', 'meal')

    def build(self):
        # Plan: three parallel fork tines and straight diagonal shafts sharing
        # (24,24). SQUARE centerline extremes (6,6)-(42,42).
        # Lucide utensils-crossed: coherent U-shaped fork and a shared crossing.
        # The different utensil heads deliberately remain asymmetric.
        self.add_line('fork-left-tine',(6,18),(10,22))
        self.add_bezier('fork-left-curve',(10,22),((13,25),(17,23),(20,20)))
        self.add_bezier('fork-right-curve',(20,20),((23,17),(25,13),(22,10)))
        self.add_line('fork-right-tine',(22,10),(18,6))
        self.add_contour('fork-head','fork-left-tine','fork-left-curve',
                         'fork-right-curve','fork-right-tine')
        self.add_line('fork-middle-tine',(12,12),(20,20))
        self.add_polyline('fork-handle',(20,20),(24,24),(42,42))
        self.relate('connect','fork-head','fork-middle-tine')
        self.relate('connect','fork-head','fork-handle')
        self.relate('connect','fork-middle-tine','fork-handle')

        # A diagonal oval bowl; both sides share tangent directions at the neck.
        self.add_bezier('spoon-upper',(30,18),((26,14),(32,6),(37,6)),
                        ((40,6),(42,8),(42,11)))
        self.add_bezier('spoon-lower',(42,11),((42,16),(34,22),(30,18)))
        self.add_contour('spoon-bowl','spoon-upper','spoon-lower',closed=True)
        self.add_polyline('spoon-handle',(6,42),(24,24),(30,18))
        self.relate('connect','spoon-handle','spoon-bowl')
        self.relate('connect','spoon-handle','fork-handle')
