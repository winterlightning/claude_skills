"""Crossed Fork and Knife."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aba5bfb7-5990-4b45-9606-e4cfe58ad1ea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/symbol fork cross knife_aba5bfb7-5990-4b45-9606-e4cfe58ad1ea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-fork-and-chef-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('fork', 'knife', 'cutlery', 'utensil', 'crossed', 'dining', 'kitchen')

    def build(self):
        # Plan: Crossed fork and chef knife. Lucide utensils-crossed common junction and separate head silhouettes. Three tines retained; handles simplified. Envelope (6,6)-(42,42).
        self.add_bezier('fork-head',(6,14),((10,18),(13,22),(17,18)),((21,14),(18,10),(14,6)))
        self.add_line('fork-middle',(6,6),(17,18));self.relate('connect','fork-middle','fork-head')
        self.add_polyline('fork-handle',(17,18),(26,27),(42,42));self.relate('connect','fork-handle','fork-head');self.relate('connect','fork-handle','fork-middle')

        self.add_polyline('knife-handle',(6,42),(26,27),(32,21))
        self.add_bezier('blade',(32,21),((40,18),(42,12),(42,6)))
        self.add_line('spine',(42,6),(26,15));self.add_line('heel',(26,15),(32,21))
        self.add_contour('knife-blade','blade','spine','heel',closed=True)
        self.relate('connect','knife-handle','knife-blade');self.relate('connect','knife-handle','fork-handle')
