"""Front-view train with windscreen divider, roof bar and splayed rails. Lucide train-front informs the car/rail hierarchy; no extra lights added.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='110050c0-02bc-446a-8b93-961566ce20f7'
SOURCE_PATH='pictographic-primitives/symbol/train_110050c0-02bc-446a-8b93-961566ce20f7.svg'
AUTHOR='gpt-6'

class TrainFront(Solo48):
    icon_id='train-front'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('train', 'railway', 'metro', 'subway', 'transport', 'tram', 'station', 'transit')

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

        self.add_line('roof-bar',(18,6),(30,6))
        self.add_line('roof',(16,16),(32,16));self.add_arc('tr',(32,16),(38,22),radius_x=6)
        self.raw('right',[(38,22),(38,26),(38,30)]);self.add_arc('br',(38,30),(32,36),radius_x=6)
        self.raw('base',[(32,36),(30,36),(18,36),(16,36)]);self.add_arc('bl',(16,36),(10,30),radius_x=6)
        self.raw('left',[(10,30),(10,26),(10,22)]);self.add_arc('tl',(10,22),(16,16),radius_x=6)
        self.add_contour('car','roof','tr','right-1','right-2','br','base-1','base-2','base-3','bl','left-1','left-2','tl',closed=True)
        self.add_line('divider',(10,26),(38,26));self.relate('connect','divider','car')
        for n,a,b in [('left',(18,36),(6,42)),('right',(30,36),(42,42))]:
            self.add_line(n+'-rail',a,b);self.relate('connect',n+'-rail','car')
