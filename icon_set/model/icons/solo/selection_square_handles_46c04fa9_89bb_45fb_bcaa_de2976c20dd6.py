"""Vector selection square with four corner handles. Lucide frame informs shared axes; four repeated square handles connect to the perimeter.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='46c04fa9-89bb-45fb-bcaa-de2976c20dd6'
SOURCE_PATH='pictographic-primitives/symbol/square block_46c04fa9-89bb-45fb-bcaa-de2976c20dd6.svg'
AUTHOR='gpt-6'

class SelectionSquareHandles(Solo48):
    icon_id='selection-square-handles'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('selection', 'square', 'vector', 'shape', 'transform', 'design', 'bounding-box', 'handles')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        lo,hi,w=6,34,8
        for j,(x,y) in enumerate([(lo,lo),(hi,lo),(hi,hi),(lo,hi)]):
            self.path('handle-'+str(j),[(x,y),(x+w,y),(x+w,y+w),(x,y+w)],True)
        for name,a,b,h1,h2 in [('top',(14,10),(34,10),0,1),('right',(38,14),(38,34),1,2),('bottom',(34,38),(14,38),2,3),('left',(10,34),(10,14),3,0)]:
            self.add_line(name,a,b)
            for h in (h1,h2):self.relate('connect',name,'handle-'+str(h))
