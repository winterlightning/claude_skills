"""Round child face with off-centre hair fringe and paired slanted eye dashes. Lucide baby informs the closed head and sparse features; hair asymmetry preserves the reference.

SOLO48 CIRCLE; live visible envelope (2, 2, 46, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='2126ca4d-f169-4065-8484-6a0bfd33fcd9'
SOURCE_PATH='pictographic-primitives/symbol/spicy head_2126ca4d-f169-4065-8484-6a0bfd33fcd9.svg'
AUTHOR='gpt-6'

class ChildFace(Solo48):
    icon_id='child-face'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('child', 'face', 'boy', 'kid', 'person', 'avatar', 'head', 'young')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.add_arc('head-top',(4,24),(44,24),radius_x=20)
        self.add_arc('head-bottom',(44,24),(4,24),radius_x=20)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_arc('fringe-left',(4,24),(28,14),radius_x=24,sweep=False)
        self.add_arc('fringe-right',(28,14),(44,24),radius_x=18,sweep=False)
        self.add_contour('fringe','fringe-left','fringe-right')
        self.relate('connect','head','fringe')
        for name,a,b in [('left',(17,33),(19,34)),('right',(29,34),(31,33))]:self.add_line(name+'-eye',a,b)
