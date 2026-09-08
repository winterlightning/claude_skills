"""A broad collar necklace closing around a pearl. Nested arches retain the collar identity.

Authored directly on SOLO48 using the VRECT_XL centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1abfa79e-18a0-4f01-b0ce-90b012a88a6a'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/necklace with pearl_1abfa79e-18a0-4f01-b0ce-90b012a88a6a.svg'
AUTHOR = 'astra-chatgpt'


class CollarNecklaceWithPearl(Solo48):
    icon_id = 'collar-necklace-with-pearl'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('collar', 'necklace', 'with', 'pearl')

    def build(self) -> None:
        def line(n, a, b):
            self.add_line(n, a, b)
        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)
        def contour(n, *parts, closed=False):
            self.add_contour(n, *parts, closed=closed)
        def connect(a, b):
            self.relate("connect", a, b)
        def circle(n, x, y, r, ry=None):
            arc(n+"-top", (x-r,y), (x+r,y), r, ry)
            arc(n+"-bottom", (x+r,y), (x-r,y), r, ry)
            contour(n, n+"-top", n+"-bottom", closed=True)
        arc("outer-top",(5,21),(43,21),19)
        arc("outer-r",(43,21),(30,40),13,19)
        arc("outer-l",(18,40),(5,21),13,19)
        contour("collar","outer-l","outer-top","outer-r")
        arc("inner",(5,21),(43,21),19,9)
        connect("inner","collar")
        circle("pearl",24,40,6)
        connect("pearl","collar")
