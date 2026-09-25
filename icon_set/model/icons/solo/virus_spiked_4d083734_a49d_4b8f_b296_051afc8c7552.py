"""Round virus with a central dot and radial spikes. Lucide sun informs the ring-and-rays hierarchy. Ten source spikes reduced to eight for readable spacing.

SOLO48 CIRCLE; live visible envelope (2, 2, 46, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='4d083734-a49d-4b8f-b296-051afc8c7552'
SOURCE_PATH='pictographic-primitives/symbol/virus_4d083734-a49d-4b8f-b296-051afc8c7552.svg'
AUTHOR='gpt-6'

class VirusSpiked(Solo48):
    icon_id='virus-spiked'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('virus', 'germ', 'bacteria', 'infection', 'covid', 'pathogen', 'cell', 'disease')

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

        inner=[(24,9),(33,12),(39,24),(33,36),(24,39),(15,36),(9,24),(15,12)]
        outer=[(24,4),(36,8),(44,24),(36,40),(24,44),(12,40),(4,24),(12,8)]
        for j,a in enumerate(inner):self.add_arc('rim-'+str(j),a,inner[(j+1)%8],radius_x=15)
        self.add_contour('rim',*['rim-'+str(j) for j in range(8)],closed=True)
        for j,(a,b) in enumerate(zip(inner,outer)):
            self.add_line('spike-'+str(j),a,b);self.relate('connect','rim','spike-'+str(j))
        self.add_dot('centre',(24,24))
