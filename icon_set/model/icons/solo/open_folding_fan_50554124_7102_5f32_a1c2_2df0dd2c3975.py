"""An open fan with a curved leaf and round pivot. Fewer ribs keep the panels legible.

Authored directly on SOLO48 using the HRECT_XL centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50554124-7102-5f32-a1c2-2df0dd2c3975'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/hand fan_50554124-7102-5f32-a1c2-2df0dd2c3975.svg'
AUTHOR = 'astra-chatgpt'


class OpenFoldingFan(Solo48):
    icon_id = 'open-folding-fan'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('open', 'folding', 'fan')

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
        arc("leaf-left",(2,20),(24,5),22,15)
        arc("leaf-right",(24,5),(46,20),22,15)
        line("edge-right",(46,20),(24,37))
        line("edge-left",(24,37),(2,20))
        contour("leaf","leaf-left","leaf-right","edge-right","edge-left",closed=True)
        line("rib",(24,5),(24,37))
        connect("leaf","rib")
        circle("pivot",24,40,3)
        connect("leaf","pivot")
        connect("rib","pivot")
