"""Medicine Blister Pack.
Plan: (8,4)-(40,44). Rounded pack surrounding 2x3 repeated pill impressions. Solid short pill strokes retain six pockets without undersized enclosed holes.
References: supplied original source; Lucide pill: rounded capsule vocabulary, repeated in two columns.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2df496b-7f5e-576b-b6f5-a634d13aedd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/drugs sheet_a2df496b-7f5e-576b-b6f5-a634d13aedd5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'medicine-blister-pack-a2df496b'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('medicine-blister-pack',)
    keywords = ('medicine', 'blister', 'pack')

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
        stroke("pack",(14,4),[((34,4),),((40,10),6,6,True),((40,38),),((34,44),6,6,True),((14,44),),((8,38),6,6,True),((8,10),),((14,4),6,6,True)],True)
        for x in (18,28):
            for y in (14,24,34):self.add_line(f"pill-{x}-{y}",(x,y),(x+2,y))

