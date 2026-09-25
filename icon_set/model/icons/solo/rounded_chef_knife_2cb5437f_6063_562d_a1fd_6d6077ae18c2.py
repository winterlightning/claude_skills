"""Diagonal Kitchen Chef Knife."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cb5437f-6063-562d-a1fd-6d6077ae18c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/knife_2cb5437f-6063-562d-a1fd-6d6077ae18c2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-chef-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('knife', 'chef knife', 'blade', 'handle', 'kitchen', 'cutting', 'utensil')

    def build(self):
        # Plan: Diagonal chef knife with broad blade and rounded handle. Lucide utensils-crossed construction; rivets omitted. Envelope (6,6)-(42,42). Rounded tip retained.
        self.add_line('handle-top',(18,26),(6,38))
        self.add_bezier('handle-end',(6,38),((6,41),(8,42),(12,42)),((15,42),(17,41),(18,40)))
        self.add_line('handle-bottom',(18,40),(26,34))
        self.add_line('heel',(26,34),(18,26))
        self.add_contour('handle','handle-top','handle-end','handle-bottom','heel',closed=True)

        self.add_line('spine',(18,26),(36,8))
        self.add_bezier('blade',(36,8),((38,6),(38,6),(40,6)),((42,6),(42,8),(42,10)),((42,18),(34,30),(26,34)))

        self.relate('connect','spine','handle');self.relate('connect','spine','blade');self.relate('connect','blade','handle')
