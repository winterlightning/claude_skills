"""Open wallet with a back panel and slanted front flap. Lucide wallet informs coherent panel corners; the open lower-right back edge is retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='ab7383aa-5093-45dc-a4d7-eefbaaf8de70'
SOURCE_PATH='pictographic-primitives/symbol/wallet_ab7383aa-5093-45dc-a4d7-eefbaaf8de70.svg'
AUTHOR='gpt-6'

class WalletOpenFlap(Solo48):
    icon_id='wallet-open-flap'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('wallet', 'open', 'flap', 'folder', 'card-holder', 'money', 'purse', 'finance')

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

        self.add_line('back-top',(12,6),(36,6));self.add_arc('back-corner',(36,6),(42,12),radius_x=6)
        self.add_line('back-right',(42,12),(42,32));self.add_contour('back','back-top','back-corner','back-right')
        self.add_line('flap-top',(12,6),(28,18));self.add_arc('flap-tr',(28,18),(30,22),radius_x=2,radius_y=4)
        self.add_line('flap-right',(30,22),(30,36));self.add_arc('flap-bottom',(30,36),(24,42),radius_x=6)
        self.add_line('flap-diagonal',(24,42),(10,32));self.add_arc('flap-left',(10,32),(6,24),radius_x=4,radius_y=8)
        self.add_line('flap-side',(6,24),(6,12));self.add_arc('flap-tl',(6,12),(12,6),radius_x=6)
        self.add_contour('flap','flap-top','flap-tr','flap-right','flap-bottom','flap-diagonal','flap-left','flap-side','flap-tl',closed=True)
        self.relate('connect','back','flap')
