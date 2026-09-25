"""Rod Shaped Bacterium.
Plan: (6,6)-(42,42). Diagonal capsule-like bacterium with six paired outward projections. Sparse plump rod without extra internal marks.
References: supplied original source; Lucide bean: coherent biological contour; supplied rod and radial projections.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb2d6fc6-f43a-40b7-b206-3b9eb2889351'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/bacteria_bb2d6fc6-f43a-40b7-b206-3b9eb2889351.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rod-shaped-bacterium-bb2d6fc6'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('rod-shaped-bacterium',)
    keywords = ('rod', 'shaped', 'bacterium')

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
        stroke("body",(10,26),[((16,18),),((22,10),),((30,6),10,10,True),((40,16),10,10,True),((38,22),10,10,True),((32,30),),((26,38),),((18,42),10,10,True),((8,32),10,10,True),((10,26),10,10,True)],True)
        rays=[((8,32),(6,32)),((40,16),(42,16)),((16,18),(10,14)),((32,30),(38,34)),((22,10),(18,6)),((26,38),(30,42))]
        for j,(a,b) in enumerate(rays):self.add_line(f"projection-{j}",a,b);self.relate("connect","body",f"projection-{j}")

