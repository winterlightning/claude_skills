"""Three people with central figure lower and in front. Lucide users-round informs head/shoulder hierarchy; all three heads retained and hidden shoulder portions omitted.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e945361d-c5a9-4fd9-95aa-74d13dfd018c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__team-three-people/20260927T094425Z-thuan-mac-1/reference/three persons_e945361d-c5a9-4fd9-95aa-74d13dfd018c.svg'
AUTHOR = "gpt-6"
REVISION_COMPARISON = 'The rejected arrangement put two heads high and one low, reversing the reference.'
REVISION_CHANGE = 'Placed the central head above two peers and aligned each with its shoulder arc.'


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
        # One person above two peers, following the three-head source hierarchy.
        self.oval('upper-head', 24, 12, 4)
        self.oval('left-head', 9, 25, 3)
        self.oval('right-head', 39, 25, 3)
        self.add_arc('upper-shoulders', (20, 28), (28, 28), radius_x=4, radius_y=4)
        self.add_arc('left-shoulders', (4, 40), (14, 40), radius_x=5, radius_y=4)
        self.add_arc('right-shoulders', (34, 40), (44, 40), radius_x=5, radius_y=4)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('e945361d-c5a9-4fd9-95aa-74d13dfd018c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/three persons_e945361d-c5a9-4fd9-95aa-74d13dfd018c.svg')]
