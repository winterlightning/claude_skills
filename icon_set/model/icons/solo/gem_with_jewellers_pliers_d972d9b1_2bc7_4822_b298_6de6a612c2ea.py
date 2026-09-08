"""A gem above open jewellers pliers. Lucide gem informs the pointed outline; tiny facets are omitted.

Authored directly on SOLO48 using the VRECT_L centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd972d9b1-2bc7-4822-b298-6de6a612c2ea'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/jewelry maker_d972d9b1-2bc7-4822-b298-6de6a612c2ea.svg'
AUTHOR = 'astra-chatgpt'


class GemWithJewellersPliers(Solo48):
    icon_id = 'gem-with-jewellers-pliers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('gem', 'with', 'jewellers', 'pliers')

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
        self.add_polyline("gem",(8,9),(14,2),(34,2),(40,9),(24,21),closed=True)
        line("facet",(8,9),(40,9))
        connect("gem","facet")
        self.add_polyline("pliers-left",(11,46),(15,29),(24,37))
        self.add_polyline("pliers-right",(37,46),(33,29),(24,37))
        connect("pliers-left","pliers-right")
        line("joint-post",(24,37),(24,40))
        connect("pliers-left","joint-post")
        connect("pliers-right","joint-post")
        circle("joint",24,43,3)
        connect("joint-post","joint")
