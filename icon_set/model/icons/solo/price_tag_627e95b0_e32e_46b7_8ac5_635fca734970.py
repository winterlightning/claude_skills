"""Diagonal price tag with upper-right punch hole. Lucide tag informs rounded corners and a sparse identifying hole; no label text added.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='627e95b0-e32e-46b7-8ac5-635fca734970'
SOURCE_PATH='pictographic-primitives/symbol/tag_627e95b0-e32e-46b7-8ac5-635fca734970.svg'
AUTHOR='gpt-6'

class PriceTag(Solo48):
    icon_id='price-tag'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('tag', 'price', 'label', 'sale', 'discount', 'shopping', 'offer', 'store')

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

        self.add_line('top',(26,6),(36,6))
        self.add_arc('tr',(36,6),(42,12),radius_x=6)
        self.add_line('right',(42,12),(42,24))
        self.add_line('diagonal-r',(42,24),(24,42))
        self.add_line('bottom',(24,42),(6,24))
        self.add_line('diagonal-l',(6,24),(26,6))
        self.add_contour('tag','top','tr','right','diagonal-r','bottom','diagonal-l',closed=True)
        self.add_dot('hole',(32,16))
