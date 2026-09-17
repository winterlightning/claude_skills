"""Person Wearing Respirator.
Plan: (8,4)-(40,44). Front-facing head, two mask straps, large round respirator and circular filter. Hair and ear detail removed; no detached body.
References: supplied original source; human_ref/user.svg: circular head; Lucide venetian-mask: intrinsic face covering and straps.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '402da3d3-fb80-5361-a533-38a968345f77'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/air pollution mask_402da3d3-fb80-5361-a533-38a968345f77.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-wearing-respirator-402da3d3'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('person-wearing-respirator',)
    keywords = ('person', 'wearing', 'respirator')

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
        stroke("head",(8,20),[((24,4),16,16,True),((40,20),16,16,True)])
        stroke("mask",(11,31),[((24,18),13,13,True),((37,31),13,13,True),((24,44),13,13,True),((11,31),13,13,True)],True)
        circle("filter",24,31,4)
        for side in (-1,1):
            self.add_line(f"strap-{side}",(24+16*side,20),(24+13*side,31));self.relate("connect",f"strap-{side}","head");self.relate("connect",f"strap-{side}","mask")

