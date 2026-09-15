"""Film camera with unequal reels and a flaring right lens. Lucide video informs the body contour; both source reels retained with shared body contacts.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='9518f09e-6822-415c-9a66-f43eca8bd8d0'
SOURCE_PATH='pictographic-primitives/symbol/video_9518f09e-6822-415c-9a66-f43eca8bd8d0.svg'
AUTHOR='gpt-6'

class MovieCameraReels(Solo48):
    icon_id='movie-camera-reels'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('movie', 'camera', 'film', 'cinema', 'video', 'record', 'reels', 'production')

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

        self.oval('rear-reel',14,14,8);self.oval('front-reel',34,18,4)
        self.raw('top',[(12,22),(14,22),(34,22),(34,28),(42,24),(42,40),(34,36),(34,38)])
        self.add_arc('br',(34,38),(30,42),radius_x=4)
        self.add_line('base',(30,42),(12,42));self.add_arc('bl',(12,42),(6,36),radius_x=6)
        self.add_line('left',(6,36),(6,28));self.add_arc('tl',(6,28),(12,22),radius_x=6)
        self.add_contour('body',*['top-'+str(j) for j in range(1,8)],'br','base','bl','left','tl',closed=True)
        self.relate('connect','rear-reel','body');self.relate('connect','front-reel','body')
