"""Solid and Dashed Overlapping Squares. Empty standalone subject, per explicit user correction.
Lucide copy: offset rounded frames with visible rear edges only. Rear dash spacing is owned by the 6-unit frame inset; front bounds 18 to 42. Fewer longer dashes preserve clear separation.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '99f8634e-1112-413f-8e94-b31a95ad9d9e'
SOURCE_PATH = 'pictographic-primitives/design/copy_99f8634e-1112-413f-8e94-b31a95ad9d9e.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'solid-and-dashed-overlapping-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    aliases = ()
    keywords = ('solid', 'and', 'dashed', 'overlapping', 'squares')
    def build(self):
        x0,y0,x1,y1,r=18,18,42,42,4
        self.add_line("front-top",(x0+r,y0),(x1-r,y0))
        self.add_arc("front-ne",(x1-r,y0),(x1,y0+r),radius_x=r)
        self.add_line("front-right",(x1,y0+r),(x1,y1-r))
        self.add_arc("front-se",(x1,y1-r),(x1-r,y1),radius_x=r)
        self.add_line("front-bottom",(x1-r,y1),(x0+r,y1))
        self.add_arc("front-sw",(x0+r,y1),(x0,y1-r),radius_x=r)
        self.add_line("front-left",(x0,y1-r),(x0,y0+r))
        self.add_arc("front-nw",(x0,y0+r),(x0+r,y0),radius_x=r)
        self.add_contour("front",*("front-"+s for s in ("top","ne","right","se","bottom","sw","left","nw")),closed=True)
        self.add_arc("rear-nw",(6,9),(9,6),radius_x=3)
        self.add_line("rear-top-left",(9,6),(14,6))
        self.add_contour("rear-first-dash","rear-nw","rear-top-left")
        self.add_line("rear-top-right",(26,6),(31,6))
        self.add_arc("rear-ne",(31,6),(34,9),radius_x=3)
        self.add_contour("rear-second-dash","rear-top-right","rear-ne")
        self.add_line("rear-left",(6,18),(6,22))
        self.add_arc("rear-sw",(6,31),(9,34),radius_x=3,sweep=False)
