"""Landscape ticket with opposing side notches and one lower-right line. Lucide ticket informs the notch/outer-corner distinction; source detail retained.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='9961750b-12c7-46ce-8f29-a1d66c155629'
SOURCE_PATH='pictographic-primitives/symbol/ticket or card_9961750b-12c7-46ce-8f29-a1d66c155629.svg'
AUTHOR='gpt-6'

class Ticket(Solo48):
    icon_id='ticket'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('ticket', 'admission', 'event', 'coupon', 'pass', 'entry', 'cinema', 'voucher')

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
        self.add_line('ru',(44,14),(44,18));self.add_arc('notch-r',(44,18),(44,30),radius_x=6,sweep=False)
        self.add_line('rl',(44,30),(44,34));self.add_arc('br',(44,34),(38,40),radius_x=6)
        self.add_line('base',(38,40),(10,40));self.add_arc('bl',(10,40),(4,34),radius_x=6)
        self.add_line('ll',(4,34),(4,30));self.add_arc('notch-l',(4,30),(4,18),radius_x=6,sweep=False)
        self.add_line('lu',(4,18),(4,14));self.add_arc('tl',(4,14),(10,8),radius_x=6)
        self.add_contour('ticket','top','tr','ru','notch-r','rl','br','base','bl','ll','notch-l','lu','tl',closed=True)
        self.add_line('detail',(23,30),(29,30))
