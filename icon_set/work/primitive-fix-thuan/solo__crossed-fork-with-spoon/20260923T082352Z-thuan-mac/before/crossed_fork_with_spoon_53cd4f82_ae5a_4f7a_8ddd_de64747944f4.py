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
        # Plan: Crossed fork and spoon. Lucide utensils-crossed X junction with compact oval spoon. Shared crossing; asymmetric heads retained. Envelope (6,6)-(42,42).
        self.add_bezier('fork-head',(6,14),((10,18),(13,22),(17,18)),((21,14),(18,10),(14,6)))
        self.add_line('fork-middle',(6,6),(17,18));self.relate('connect','fork-middle','fork-head')
        self.add_polyline('fork-handle',(17,18),(26,27),(42,42));self.relate('connect','fork-handle','fork-head');self.relate('connect','fork-handle','fork-middle')

        self.add_bezier('spoon',(32,20),((26,16),(32,6),(37,6)),((40,6),(42,8),(42,11)),((42,16),(36,23),(32,20)))
        self.add_contour('spoon-bowl','spoon',closed=True)
        self.add_polyline('spoon-handle',(6,42),(26,27),(32,20));self.relate('connect','spoon-handle','spoon-bowl');self.relate('connect','spoon-handle','fork-handle')
