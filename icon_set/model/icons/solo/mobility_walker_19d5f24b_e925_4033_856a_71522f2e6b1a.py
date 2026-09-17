"""Mobility Walker.
Plan: (8,4)-(40,44). Sloping frame with broad foot, top grip, crossbar and one front wheel. Side-view asymmetry follows source.
References: supplied original source; no direct useful Lucide match; source frame, grip, wheel, and foot.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19d5f24b-e925-4033-856a-71522f2e6b1a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/instrument walking aid_19d5f24b-e925-4033-856a-71522f2e6b1a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mobility-walker-19d5f24b'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('mobility-walker',)
    keywords = ('mobility', 'walker')

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
        stroke("frame",(12,44),[((16,24),),((20,8),),((24,4),4,4,True),((32,4),)])
        self.add_polyline("foot",(8,44),(12,44),(16,44));self.relate("connect","frame","foot")
        stroke("brace",(16,24),[((28,24),),((35,31),7,7,True),((35,34),)])
        self.relate("connect","frame","brace")
        stroke("wheel",(35,34),[((40,39),5,5,True),((35,44),5,5,True),((30,39),5,5,True),((35,34),5,5,True)],True)
        self.relate("connect","brace","wheel")

