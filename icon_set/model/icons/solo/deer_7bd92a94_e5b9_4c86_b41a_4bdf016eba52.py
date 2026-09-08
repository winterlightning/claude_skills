"""A frontal deer head with mirrored branching antlers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bd92a94-e5b9-4c86-b41a-4bdf016eba52'
SOURCE_PATH = 'pictographic-primitives/animals/deer_7bd92a94-e5b9-4c86-b41a-4bdf016eba52.svg'
AUTHOR = 'gpt-6'


class DeerHead(Solo48):
    icon_id = 'deer-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('deer', 'head', 'antlers', 'stag', 'face', 'muzzle', 'wildlife', 'buck')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_line("crown",(16,22),(32,22))
        self.add_line("cheek-right",(32,22),(30,40))
        self.add_arc("chin",(30,40),(18,40),radius_x=6)
        self.add_line("cheek-left",(18,40),(16,22))
        self.add_contour("head","crown","cheek-right","chin","cheek-left",closed=True)
        for side,x,outer in (("left",16,2),("right",32,46)):
         self.add_polyline(side+"-antler",(x,22),(outer,10),(outer,2))
         self.relate("connect","head",side+"-antler")
         self.add_line(side+"-tine",(outer,10),(x,4))
         self.relate("connect",side+"-antler",side+"-tine")
