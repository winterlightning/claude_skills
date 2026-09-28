"""Three people with central figure lower and in front. Lucide users-round informs head/shoulder hierarchy; all three heads retained and hidden shoulder portions omitted.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='67deb73a-b4c1-4eed-aa08-baa158ea343d'
SOURCE_PATH='pictographic-primitives/symbol/team_67deb73a-b4c1-4eed-aa08-baa158ea343d.svg'
AUTHOR = 'gpt-6'

class TeamThreePeople(Solo48):
    icon_id='team-three-people'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol",)
    aliases=()
    keywords = ('team', 'group', 'people', 'users', 'community', 'members', 'staff', 'crowd', 'sub icon')

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

        for n,x,y,r in [('left',10,12,4),('right',38,12,4),('front',24,21,4)]:self.oval(n+'-head',x,y,r)
        self.add_line('left-side',(4,31),(4,29))
        self.add_arc('left-shoulders',(4,29),(14,29),radius_x=5,radius_y=4)
        self.add_contour('left-body','left-side','left-shoulders')
        self.add_arc('right-shoulders',(34,29),(44,29),radius_x=5,radius_y=4)
        self.add_line('right-side',(44,29),(44,31))
        self.add_contour('right-body','right-shoulders','right-side')
        self.add_arc('front-shoulders',(14,40),(34,40),radius_x=10,radius_y=4)
        self.add_contour('front-body','front-shoulders')


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('e945361d-c5a9-4fd9-95aa-74d13dfd018c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/three persons_e945361d-c5a9-4fd9-95aa-74d13dfd018c.svg')]
