"""Three evenly spaced solid dots on the vertical diameter of the circular keyshape. Lucide ellipsis-vertical informs one axis and constant pitch; dot size remains the fixed stroke width.

SOLO48 CIRCLE; live visible envelope (2, 2, 46, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='0a262ad5-77ea-4fea-bb24-97e6f7a6c26e'
SOURCE_PATH='pictographic-primitives/symbol/three dots_0a262ad5-77ea-4fea-bb24-97e6f7a6c26e.svg'
AUTHOR='gpt-6'

class DotsVerticalThree(Solo48):
    icon_id='dots-vertical-three'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol",)
    aliases=()
    keywords=('dots', 'more', 'menu', 'options', 'kebab', 'vertical', 'ellipsis', 'overflow')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def raw(self,n,points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(n+'-'+str(j),a,b)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        axis,origin,step=24,4,20
        for j in range(3):self.add_dot('dot-'+str(j),(axis,origin+j*step))
