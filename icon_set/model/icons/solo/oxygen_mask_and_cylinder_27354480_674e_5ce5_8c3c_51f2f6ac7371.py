"""Oxygen Mask and Cylinder.
Plan: (6,6)-(42,42). Left shield mask connects by U-shaped hose to rounded right cylinder with raised valve. Small outlet rings removed.
References: supplied original source; Lucide stethoscope: functional paired components joined by one hose.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27354480-674e-5ce5-8c3c-51f2f6ac7371'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/oxygen tank_27354480-674e-5ce5-8c3c-51f2f6ac7371.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oxygen-mask-and-cylinder-27354480'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('oxygen-mask-and-cylinder',)
    keywords = ('oxygen', 'mask', 'and', 'cylinder')

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
        stroke("mask",(14,6),[((22,14),),((22,18),),((14,26),8,8,True),((6,18),8,8,True),((6,14),),((14,6),)],True)
        stroke("cylinder",(30,20),[((36,14),6,6,True),((42,20),6,6,True),((42,36),),((30,36),6,6,True),((30,34),),((30,20),)],True)
        self.add_line("valve",(36,6),(36,14));self.relate("connect","valve","cylinder")
        stroke("hose",(14,26),[((14,34),),((22,42),8,8,False),((30,34),8,8,False)])
        self.relate("connect","hose","mask");self.relate("connect","hose","cylinder")

