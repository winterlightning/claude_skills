"""Knee Joint.
Plan: Centerlines (10,4)-(38,44); open upper/lower shafts with broad uneven joint lobes and an enlarged joint space.
References: supplied original source; source joint anatomy; no direct useful Lucide match.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bae3cd4c-6954-5fed-9b94-9b4a7fbb195a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty knee_bae3cd4c-6954-5fed-9b94-9b4a7fbb195a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'knee-joint-bae3cd4c'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('knee-joint',)
    keywords = ('knee', 'joint')

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
        stroke("femur",(14,4),[((16,12),),((10,16),6,4,False),((16,20),6,4,False),
            ((24,18),8,4,False),((32,20),8,4,True),((38,14),6,6,False),((32,10),),((30,4),)])
        stroke("tibia",(14,44),[((14,40),),((10,34),4,6,False),((16,30),6,4,True),
            ((24,32),8,4,True),((32,30),8,4,False),((38,34),6,4,True),((32,40),6,6,True),((32,44),)])
