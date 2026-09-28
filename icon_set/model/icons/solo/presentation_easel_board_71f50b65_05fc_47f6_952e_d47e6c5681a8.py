"""Presentation Easel Board. Empty standalone subject, per explicit user correction.
Lucide presentation: board outline and splayed support junctions. Symmetry about x=24; clamp width and height 8. Tiny top stub and central support overlap omitted, preserving clamp and two legs.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '71f50b65-05fc-47f6-952e-d47e6c5681a8'
SOURCE_PATH = 'pictographic-primitives/design/design drawing board_71f50b65-05fc-47f6-952e-d47e6c5681a8.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'presentation-easel-board'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    categories = ('design', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('presentation', 'easel', 'board')
    def build(self):
        points=((10,14),(20,14),(20,6),(28,6),(28,14),(38,14))
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f"top-clamp-{i}",a,b)
        self.add_arc("board-ne",(38,14),(42,18),radius_x=4)
        self.add_line("board-right",(42,18),(42,28))
        self.add_arc("board-se",(42,28),(38,32),radius_x=4)
        points=((38,32),(30,32),(18,32),(10,32))
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f"board-bottom-{i}",a,b)
        self.add_arc("board-sw",(10,32),(6,28),radius_x=4)
        self.add_line("board-left",(6,28),(6,18))
        self.add_arc("board-nw",(6,18),(10,14),radius_x=4)
        self.add_contour("board",*(f"top-clamp-{i}" for i in range(1,6)),"board-ne","board-right","board-se",*(f"board-bottom-{i}" for i in range(1,4)),"board-sw","board-left","board-nw",closed=True)
        self.add_line("clamp-bottom",(20,14),(28,14))
        self.relate("connect","board","clamp-bottom")
        for side,x,foot in (("left",18,12),("right",30,36)):
            self.add_line(side+"-leg",(x,32),(foot,42))
            self.relate("connect","board",side+"-leg")
