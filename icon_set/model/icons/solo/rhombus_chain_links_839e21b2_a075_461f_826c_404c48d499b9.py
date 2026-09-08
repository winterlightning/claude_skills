"""Three diagonal rhombus links. Lucide link informs simple linked contours; diagonal arrangement is intentional.

Authored directly on SOLO48 using the SQUARE centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '839e21b2-a075-461f-826c-404c48d499b9'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/chain rhombus_839e21b2-a075-461f-826c-404c48d499b9.svg'
AUTHOR = 'astra-chatgpt'


class RhombusChainLinks(Solo48):
    icon_id = 'rhombus-chain-links'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('rhombus', 'chain', 'links')

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
        for n,x,y in (("lower",10,38),("middle",24,24),("upper",38,10)):
            self.add_polyline(n, (x,y-8), (x+4,y-4), (x+8,y), (x+4,y+4), (x,y+8), (x-8,y), (x-4,y-4), closed=True)
        line("join-lower", (14,34), (20,28))
        line("join-upper", (28,20), (34,14))
        for a,b in (("lower","join-lower"),("middle","join-lower"),("middle","join-upper"),("upper","join-upper")):
            connect(a,b)
