"""A broad ski lens with a raised nose notch. Mirrored shoulders and lower lobes preserve the one-piece silhouette.

Authored directly on SOLO48 using the HRECT_L centerline envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63a44219-0af5-5214-abed-771271356b20'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/glasses ski_63a44219-0af5-5214-abed-771271356b20.svg'
AUTHOR = 'gpt-6'


class SkiGoggles(Solo48):
    icon_id = 'ski-goggles'
    keyshape = Keyshape.HRECT_L
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
        line("top",(8,8),(40,8))
        arc("shoulder-r",(40,8),(44,14),4,6)
        line("side-r",(44,14),(44,29))
        arc("lobe-r",(44,29),(35,40),9,11)
        arc("inner-r",(35,40),(27,32),8)
        arc("nose",(27,32),(21,32),3,sweep=False)
        arc("inner-l",(21,32),(13,40),8)
        arc("lobe-l",(13,40),(4,29),9,11)
        line("side-l",(4,29),(4,14))
        arc("shoulder-l",(4,14),(8,8),4,6)
        contour("lens","top","shoulder-r","side-r","lobe-r","inner-r","nose","inner-l","lobe-l","side-l","shoulder-l",closed=True)
