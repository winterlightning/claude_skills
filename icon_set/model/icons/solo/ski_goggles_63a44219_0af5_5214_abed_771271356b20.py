"""A broad ski lens with a raised nose notch. Mirrored shoulders and lower lobes preserve the one-piece silhouette.

Authored directly on SOLO48 using the HRECT_S centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63a44219-0af5-5214-abed-771271356b20'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/glasses ski_63a44219-0af5-5214-abed-771271356b20.svg'
AUTHOR = 'astra-chatgpt'


class SkiGoggles(Solo48):
    icon_id = 'ski-goggles'
    keyshape = Keyshape.HRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('ski', 'goggles')

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
        line("top",(8,14),(40,14))
        arc("shoulder-r",(40,14),(46,20),6)
        line("side-r",(46,20),(46,23))
        arc("lobe-r",(46,23),(35,34),11)
        arc("inner-r",(35,34),(27,26),8)
        arc("nose",(27,26),(21,26),3,sweep=False)
        arc("inner-l",(21,26),(13,34),8)
        arc("lobe-l",(13,34),(2,23),11)
        line("side-l",(2,23),(2,20))
        arc("shoulder-l",(2,20),(8,14),6)
        contour("lens","top","shoulder-r","side-r","lobe-r","inner-r","nose","inner-l","lobe-l","side-l","shoulder-l",closed=True)
