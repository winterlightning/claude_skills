"""Massage Roller Stick.
Plan: (8,4)-(40,44). Rounded central head with two paired side rollers and solid handle. Inner decorative circle removed for clearance.
References: supplied original source; no direct useful Lucide match; paired rounded rollers repeated from one definition.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cef2169e-484d-428d-a000-3cc3f6a2efc2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage stick balls_cef2169e-484d-428d-a000-3cc3f6a2efc2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'massage-roller-stick-cef2169e'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('massage-roller-stick',)
    keywords = ('massage', 'roller', 'stick')

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
        stroke("head",(20,4),[((28,4),),((32,8),4,4,True),((32,16),),((32,24),),((32,32),),((28,36),4,4,True),((24,36),),((20,36),),((16,32),4,4,True),((16,24),),((16,16),),((16,8),),((20,4),4,4,True)],True)
        for side in (-1,1):
            x=24+8*side
            for y in (12,28):
                stroke(f"roller-{side}-{y}",(x,y-4),[((24+16*side,y),8,4,side>0),((x,y+4),8,4,side>0)])
                self.relate("connect","head",f"roller-{side}-{y}")
        self.add_line("handle",(24,36),(24,44))
        self.relate("connect","head","handle")

