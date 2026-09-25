"""Pair of Kidneys.
Plan: (4,8)-(44,40). Mirrored bean-shaped kidneys, inward notches and two short inward ducts. Long descending duct runs omitted for clearance. Shared side parameter preserves paired anatomy.
References: supplied original source; no useful direct Lucide organ match; supplied kidney contours and ducts.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0192e137-3839-40b4-9db9-abcc424e97fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/kidney 1_0192e137-3839-40b4-9db9-abcc424e97fe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pair-of-kidneys-0192e137'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('pair-of-kidneys',)
    keywords = ('pair', 'of', 'kidneys')

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
        for side in (-1,1):
            def p(x,y):return(24+side*x,y)
            stroke(f"kidney-{side}",p(10,8),[(p(20,24),10,16,side>0),(p(10,40),10,16,side>0),(p(10,24),4,8,side>0),(p(10,8),4,8,side>0)],True)
            self.add_line(f"duct-{side}",p(10,24),p(4,24))
            self.relate("connect",f"kidney-{side}",f"duct-{side}")

