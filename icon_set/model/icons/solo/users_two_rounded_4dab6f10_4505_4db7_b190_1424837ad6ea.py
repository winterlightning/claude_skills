"""Two people with joined rounded closed torsos, the left person slightly larger. Lucide users-round informs repeated head/shoulder geometry; shared torso contacts match the source grouping.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='4dab6f10-4505-4db7-b190-1424837ad6ea'
SOURCE_PATH='pictographic-primitives/symbol/user group_4dab6f10-4505-4db7-b190-1424837ad6ea.svg'
AUTHOR='gpt-6'

class UsersTwoRounded(Solo48):
    icon_id='users-two-rounded'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('users', 'group', 'people', 'team', 'members', 'friends', 'contacts', 'community')

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

        self.oval('left-head',14,14,6);self.oval('right-head',36,14,5)
        for n,cx in [('left',14),('right',34)]:
            self.add_arc(n+'-shoulders',(cx-10,36),(cx+10,36),radius_x=10,radius_y=7)
            self.raw(n+'-base',[(cx+10,36),(cx+10,40),(cx-10,40),(cx-10,36)])
            self.add_contour(n+'-torso',n+'-shoulders',*[n+'-base-'+str(j) for j in range(1,4)],closed=True)
        self.relate('connect','left-torso','right-torso')
