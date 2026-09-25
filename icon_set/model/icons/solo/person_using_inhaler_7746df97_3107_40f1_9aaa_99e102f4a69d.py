"""Person Using Inhaler.
Plan: (4,8)-(44,40). Left-facing open mouth beside an L-shaped inhaler. One cap seam identifies the upright canister; no tiny mouthpiece ring.
References: supplied original source; human_ref/user.svg: simplified head profile; source L-shaped inhaler and lip contour.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7746df97-3107-40f1-9aaa-99e102f4a69d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/inhaler mouth_7746df97-3107-40f1-9aaa-99e102f4a69d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-using-inhaler-7746df97'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('person-using-inhaler',)
    keywords = ('person', 'using', 'inhaler')

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
        stroke("inhaler",(4,8),[((14,8),),((14,16),),((14,26),),((22,26),),((22,36),),((10,36),),((4,30),6,6,True),((4,16),),((4,8),)],True)
        self.add_line("cap",(4,16),(14,16));self.relate("connect","inhaler","cap")
        stroke("profile",(44,8),[((36,12),12,12,False),((30,24),),((36,26),),((32,30),),((36,34),4,4,False),((36,40),)])

