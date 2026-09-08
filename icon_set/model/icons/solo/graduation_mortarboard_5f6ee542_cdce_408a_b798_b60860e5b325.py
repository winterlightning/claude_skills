"""An academic diamond cap above a shallow crown. Lucide graduation-cap informs the layered construction; no tassel added.

Authored directly on SOLO48 using the HRECT_L centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f6ee542-cdce-408a-b798-b60860e5b325'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/cap_5f6ee542-cdce-408a-b798-b60860e5b325.svg'
AUTHOR = 'astra-chatgpt'


class GraduationMortarboard(Solo48):
    icon_id = 'graduation-mortarboard'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('graduation', 'mortarboard')

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
        self.add_polyline("board", (2,18), (24,8), (46,18), (38,22), (24,28), (10,22), closed=True)
        line("crown-left", (10,22), (10,33))
        arc("crown-bottom", (10,33), (38,33), 14, 7, False)
        line("crown-right", (38,33), (38,22))
        contour("crown", "crown-left", "crown-bottom", "crown-right")
        connect("board", "crown")
