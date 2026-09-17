"""Medicine Capsule.
Plan: CIRCLE radius20. Diagonal capsule using matched round ends and parallel sides. Central transverse seam between two shared boundary vertices.
References: supplied original source; Lucide pill: two equal semicircular ends and one transverse seam.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11cb9f08-b025-4d80-9263-81694d1f2f6b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_11cb9f08-b025-4d80-9263-81694d1f2f6b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'medicine-capsule-11cb9f08'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('medicine-capsule',)
    keywords = ('medicine', 'capsule')

    def build(self):

        def stroke(name, start, segments, closed=False):
            members=[]
            for j,s in enumerate(segments):
                member=f"{name}-{j}"
                if len(s)==1: self.add_line(member,start,s[0])
                else: self.add_arc(member,start,s[0],radius_x=s[1],radius_y=s[2],sweep=s[3],large_arc=s[4] if len(s)>4 else False)
                members.append(member);start=s[0]
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            stroke(name,(cx-r,cy),[((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)],True)
        stroke("capsule",(10,26),[((16,18),),((22,10),),((38,22),10,10,True),((32,30),),((26,38),),((10,26),10,10,True)],True)
        self.add_line("seam",(16,18),(32,30));self.relate("connect","capsule","seam")

