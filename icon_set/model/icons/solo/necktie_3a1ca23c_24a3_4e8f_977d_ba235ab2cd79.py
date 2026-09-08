"""A vertical necktie with a trapezoid knot and pointed blade. Symmetry preserves the formal hanging shape.

Authored directly on SOLO48 using the VRECT_S centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a1ca23c-24a3-4e8f-977d-ba235ab2cd79'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/tie_3a1ca23c-24a3-4e8f-977d-ba235ab2cd79.svg'
AUTHOR = 'astra-chatgpt'


class Necktie(Solo48):
    icon_id = 'necktie'
    keyshape = Keyshape.VRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('necktie',)

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
        self.add_polyline("knot",(14,2),(34,2),(29,12),(19,12),closed=True)
        self.add_polyline("blade",(19,12),(14,36),(24,46),(34,36),(29,12))
        connect("knot","blade")
