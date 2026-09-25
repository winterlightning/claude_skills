"""Larger right/front person with smaller left/rear person. Lucide users-round informs separate heads and partial rear shoulders; hidden body portions omitted.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7'
SOURCE_PATH='pictographic-primitives/symbol/two persons_45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7.svg'
AUTHOR='gpt-6'

class UsersTwoOverlap(Solo48):
    icon_id='users-two-overlap'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('users', 'people', 'group', 'team', 'family', 'members', 'friends', 'contacts')

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

        self.oval('rear-head',10,12,4);self.oval('front-head',34,16,8)
        self.add_line('rear-side',(4,36),(4,34));self.add_arc('rear-shoulder',(4,34),(10,25),radius_x=6,radius_y=9)
        self.add_line('rear-top',(10,25),(14,25));self.add_contour('rear-body','rear-side','rear-shoulder','rear-top')
        self.add_arc('front-body',(20,40),(44,40),radius_x=12,radius_y=7)
