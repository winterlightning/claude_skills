"""Round glasses with bridge and short temple stubs. Lucide glasses informs matched lenses and a curved bridge.

Authored directly on SOLO48 using the HRECT_S centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41550461-e3b5-5afa-9c94-f00a4eb2aa3a'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/glasses retro_41550461-e3b5-5afa-9c94-f00a4eb2aa3a.svg'
AUTHOR = 'astra-chatgpt'


class RoundEyeglasses(Solo48):
    icon_id = 'round-eyeglasses'
    keyshape = Keyshape.HRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('round', 'eyeglasses')

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
        circle("left-lens",12,24,8,10)
        circle("right-lens",36,24,8,10)
        arc("bridge",(20,24),(28,24),4)
        line("temple-left",(2,24),(4,24))
        line("temple-right",(44,24),(46,24))
        connect("left-lens","bridge")
        connect("right-lens","bridge")
        connect("left-lens","temple-left")
        connect("right-lens","temple-right")
