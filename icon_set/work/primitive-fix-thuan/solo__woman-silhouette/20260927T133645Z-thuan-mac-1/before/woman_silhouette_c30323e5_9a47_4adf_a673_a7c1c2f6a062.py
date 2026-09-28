"""Woman with parted hair, neck and sloping shoulders. Lucide user-round informs coherent paired contours; small outward hair flicks simplified to clear side ends.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='c30323e5-9a47-4adf-a673-a7c1c2f6a062'
SOURCE_PATH='pictographic-primitives/symbol/women_c30323e5-9a47-4adf-a673-a7c1c2f6a062.svg'
AUTHOR='gpt-6'

class WomanSilhouette(Solo48):
    icon_id='woman-silhouette'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('woman', 'female', 'silhouette', 'person', 'avatar', 'user', 'profile', 'lady')

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

        self.add_line('hair-left',(6,30),(6,24));self.add_arc('hair-top',(6,24),(42,24),radius_x=18)
        self.add_line('hair-right',(42,24),(42,30));self.add_contour('hair','hair-left','hair-top','hair-right')
        self.raw('left-shoulder',[(6,42),(6,40),(20,34),(20,32)])
        self.add_arc('left-cheek',(20,32),(16,26),radius_x=6)
        self.raw('face-top',[(16,26),(16,22),(24,16),(32,22),(32,26)])
        self.add_arc('right-cheek',(32,26),(28,32),radius_x=6)
        self.raw('right-shoulder',[(28,32),(28,34),(42,40),(42,42)])
        self.add_contour('silhouette',*['left-shoulder-'+str(j) for j in range(1,4)],'left-cheek',*['face-top-'+str(j) for j in range(1,5)],'right-cheek',*['right-shoulder-'+str(j) for j in range(1,4)])
