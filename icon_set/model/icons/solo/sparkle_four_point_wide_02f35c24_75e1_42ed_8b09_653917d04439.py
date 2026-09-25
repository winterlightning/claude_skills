"""Four-point sparkle with four repeated concave arcs. Lucide sparkle informs a single symmetric contour; source points retained and tiny tip nubs omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='02f35c24-75e1-42ed-8b09-653917d04439'
SOURCE_PATH='pictographic-primitives/symbol/spark_02f35c24-75e1-42ed-8b09-653917d04439.svg'
AUTHOR='gpt-6'

class SparkleFourPointWide(Solo48):
    icon_id='sparkle-four-point-wide'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('sparkle', 'star', 'shine', 'magic', 'ai', 'new', 'twinkle', 'highlight')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        tips=[(24,6),(42,24),(24,42),(6,24)]
        for j in range(4):self.add_arc('side-'+str(j),tips[j],tips[(j+1)%4],radius_x=24,sweep=False)
        self.add_contour('sparkle',*['side-'+str(j) for j in range(4)],closed=True)
