"""A domed bowler with a hatband and upturned brim. Symmetric crown and brim corners use shared radii.

Authored directly on SOLO48 using the HRECT_L centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9ffcaa3-d483-4e32-bc69-6209c65297b2'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/hat gentleman_f9ffcaa3-d483-4e32-bc69-6209c65297b2.svg'
AUTHOR = 'astra-chatgpt'


class BowlerHat(Solo48):
    icon_id = 'bowler-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('bowler', 'hat')

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
        arc("dome",(9,23),(39,23),15)
        line("wall-r",(39,23),(39,32))
        line("wall-r-bottom",(39,32),(39,40))
        line("base",(39,40),(9,40))
        line("wall-l-bottom",(9,40),(9,32))
        line("wall-l",(9,32),(9,23))
        contour("crown","dome","wall-r","wall-r-bottom","base","wall-l-bottom","wall-l",closed=True)
        line("band",(9,32),(39,32))
        connect("crown","band")
        arc("brim-l",(2,33),(9,40),7,sweep=False)
        arc("brim-r",(39,40),(46,33),7,sweep=False)
        connect("crown","brim-l")
        connect("crown","brim-r")
