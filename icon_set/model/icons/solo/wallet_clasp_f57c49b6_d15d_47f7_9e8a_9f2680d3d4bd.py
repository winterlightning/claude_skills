"""Rounded wallet with fold line and right clasp. Lucide wallet-cards informs panel and tab construction; tiny clasp snap omitted to preserve opening clearance.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd'
SOURCE_PATH='pictographic-primitives/symbol/wallet_f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd.svg'
AUTHOR='gpt-6'

class WalletClasp(Solo48):
    icon_id='wallet-clasp'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('wallet', 'money', 'payment', 'finance', 'cash', 'purse', 'billfold', 'savings')

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

        self.add_line('top',(10,8),(38,8));self.add_arc('tr',(38,8),(44,14),radius_x=6)
        self.raw('right',[(44,14),(44,20),(44,32),(44,34)]);self.add_arc('br',(44,34),(38,40),radius_x=6)
        self.add_line('base',(38,40),(10,40));self.add_arc('bl',(10,40),(4,34),radius_x=6)
        self.raw('left',[(4,34),(4,17),(4,14)]);self.add_arc('tl',(4,14),(10,8),radius_x=6)
        self.add_contour('wallet','top','tr','right-1','right-2','right-3','br','base','bl','left-1','left-2','tl',closed=True)
        self.add_line('fold',(4,17),(24,17));self.relate('connect','fold','wallet')
        self.add_line('tab-top',(44,20),(34,20));self.add_arc('tab-end',(34,20),(34,32),radius_x=6,sweep=False)
        self.add_line('tab-base',(34,32),(44,32));self.add_contour('tab','tab-top','tab-end','tab-base')
        self.relate('connect','tab','wallet')
