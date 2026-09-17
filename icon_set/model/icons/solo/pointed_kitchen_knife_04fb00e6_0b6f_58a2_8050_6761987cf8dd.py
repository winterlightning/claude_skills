"""Diagonal Kitchen Knife."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04fb00e6-0b6f-58a2-8050-6761987cf8dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/knife_04fb00e6-0b6f-58a2-8050-6761987cf8dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-kitchen-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('knife', 'blade', 'handle', 'kitchen', 'cutting', 'utensil', 'point')

    def build(self):
        # Plan: Diagonal chef knife with broad blade and rounded handle. Lucide utensils-crossed construction; rivets omitted. Envelope (6,6)-(42,42). Sharp tip retained.
        self.add_line('handle-top',(18,26),(6,38))
        self.add_bezier('handle-end',(6,38),((6,41),(8,42),(12,42)),((15,42),(17,41),(18,40)))
        self.add_line('handle-bottom',(18,40),(26,34))
        self.add_line('heel',(26,34),(18,26))
        self.add_contour('handle','handle-top','handle-end','handle-bottom','heel',closed=True)

        self.add_line('spine',(18,26),(42,6))
        self.add_bezier('blade',(42,6),((42,16),(34,28),(26,34)))

        self.relate('connect','spine','handle');self.relate('connect','spine','blade');self.relate('connect','blade','handle')
