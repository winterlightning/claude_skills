"""Massage Recliner.
Plan: (4,8)-(44,40). Side-view reclined seat, shallow curved pedestal base, two massage waves. Cushion simplified into the back endpoint.
References: supplied original source; Lucide armchair: coherent seat and back construction; source recline and waves.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05442212-5df7-57df-9680-33e0b62caeee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage chair wave_05442212-5df7-57df-9680-33e0b62caeee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'massage-recliner-05442212'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('massage-recliner',)
    keywords = ('massage', 'recliner')

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
        stroke("seat",(4,8),[((10,22),),((20,28),10,10,False),((24,28),),((30,28),),((44,36),)])
        stroke("support",(14,40),[((24,38),10,2,True),((34,40),10,2,True)])
        self.add_line("pedestal",(24,28),(24,38));self.relate("connect","seat","pedestal");self.relate("connect","support","pedestal")
        for j,x in enumerate((24,36)):
            stroke(f"wave-{j}",(x,8),[((x+2,13),2,5,True),((x,18),2,5,False)])

