"""Oxygen Mask in Profile.
Plan: (8,4)-(40,44). Left-facing head, broad nasal mask, one cheek strap and short hose. Continuous anatomical head/neck source.
References: supplied original source; human_ref/user.svg: coherent head silhouette; Lucide stethoscope: sparse tubing.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '271fffbf-c0f5-4271-aa4c-60ff67604b47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/oxygen mask head side_271fffbf-c0f5-4271-aa4c-60ff67604b47.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oxygen-mask-in-profile-271fffbf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('oxygen-mask-in-profile',)
    keywords = ('oxygen', 'mask', 'in', 'profile')

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
        stroke("head",(14,20),[((14,16),),((28,4),14,12,True),((40,16),12,12,True),((40,24),),((34,36),),((34,44),)])
        stroke("mask",(14,20),[((8,26),6,6,False),((8,30),),((14,36),6,6,False),((22,36),),((22,30),),((14,20),8,10,False)],True)
        self.relate("connect","head","mask")
        self.add_line("strap",(22,30),(30,22));self.relate("connect","strap","mask")
        stroke("hose",(14,36),[((14,40),),((18,44),4,4,False),((25,44),)])
        self.relate("connect","hose","mask")

