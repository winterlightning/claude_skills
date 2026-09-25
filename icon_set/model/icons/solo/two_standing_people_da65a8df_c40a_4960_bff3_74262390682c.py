"""Two matched standing figures with round heads, broad torsos, and narrower legs. Shared figure dimensions preserve repetition. Lucide person-standing informs reduction; fingers and separate trouser seams are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da65a8df-c40a-4960-bff3-74262390682c'
SOURCE_PATH = 'pictographic-primitives/users/multiple man_da65a8df-c40a-4960-bff3-74262390682c.svg'
AUTHOR = 'gpt-6'


class TwoStandingPeople(Solo48):
    icon_id = 'two-standing-people'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    categories = ("users", "primitives")
    aliases = ()
    keywords = ('people', 'two', 'users', 'pair', 'men', 'figures', 'group', 'team', 'sub icon')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-a',top,bottom,radius_x=radius)
        self.add_arc(name+'-b',bottom,top,radius_x=radius)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def male_body(self, name, cx, cap_y=29, arm_y=33, base_y=44):
        radius=5
        self.add_arc(name+'-cap',(cx-radius,cap_y),(cx+radius,cap_y),radius_x=radius)
        pts=[(cx+radius,cap_y),(cx+radius,arm_y),(cx+4,arm_y),(cx+4,base_y),(cx-4,base_y),(cx-4,arm_y),(cx-radius,arm_y),(cx-radius,cap_y)]
        members=[name+'-cap']
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i); self.add_line(eid,a,b); members.append(eid)
        self.add_contour(name,*members,closed=True)


    def build(self) -> None:
        # Portrait centerline extremes (8,6)-(40,42).
        for index,cx in enumerate((13,35)):
            self.circle('head-'+str(index),cx,9,5)
            self.male_body('body-'+str(index),cx)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('5e8b621f-4f10-4323-943d-1337196c6e73', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_5e8b621f-4f10-4323-943d-1337196c6e73.svg')]
