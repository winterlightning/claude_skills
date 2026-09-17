"""Nurse Cap.
Plan: (4,8)-(44,40). Broad trapezoid cap with raised crown and a sparse intrinsic cross. Cross is a mark on the cap, not a separate modifier.
References: supplied original source; Lucide hard-hat: raised crown and broad protective headwear silhouette.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc5b9837-8a4e-462f-a85a-2ee9910df149'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/personnel hat_cc5b9837-8a4e-462f-a85a-2ee9910df149.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'nurse-cap-cc5b9837'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('nurse-cap',)
    keywords = ('nurse', 'cap')

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
        stroke("cap",(4,16),[((12,16),),((16,8),),((32,8),),((36,16),),((44,16),),((40,34),),((34,40),6,6,True),((14,40),),((8,34),6,6,True),((4,16),)],True)
        self.add_polyline("cross-h",(20,26),(24,26),(28,26))
        self.add_polyline("cross-v",(24,22),(24,26),(24,30));self.relate("connect","cross-h","cross-v")

