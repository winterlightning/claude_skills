"""Side-view video camera with a flaring lens. Lucide video informs tangent body corners and integrated lens shape; no additional controls added.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='d11a7614-b4c2-4867-ade6-95766a51c002'
SOURCE_PATH='pictographic-primitives/symbol/video 1_d11a7614-b4c2-4867-ade6-95766a51c002.svg'
AUTHOR='gpt-6'

class VideoCamera(Solo48):
    icon_id='video-camera'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('video', 'camera', 'record', 'film', 'movie', 'call', 'meeting', 'camcorder')

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

        self.add_line('top',(10,8),(22,8));self.add_arc('tr',(22,8),(28,14),radius_x=6)
        self.raw('lens',[(28,14),(28,18),(44,10),(44,38),(28,30),(28,34)])
        self.add_arc('br',(28,34),(22,40),radius_x=6);self.add_line('base',(22,40),(10,40))
        self.add_arc('bl',(10,40),(4,34),radius_x=6);self.add_line('left',(4,34),(4,14))
        self.add_arc('tl',(4,14),(10,8),radius_x=6)
        self.add_contour('camera','top','tr',*['lens-'+str(j) for j in range(1,6)],'br','base','bl','left','tl',closed=True)
