"""Prosthetic Arm.
Plan: (8,4)-(40,44). Broad prosthetic socket, round elbow joint, angled forearm and two-jawed claw. Forearm reduced to a mechanical link.
References: supplied original source; Lucide bone: clear limb segments and rounded joint vocabulary; source mechanical claw.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ccd79db5-65d1-53e3-8c34-4923a686b9c8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/prosthetic arm_ccd79db5-65d1-53e3-8c34-4923a686b9c8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'prosthetic-arm-ccd79db5'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('prosthetic-arm',)
    keywords = ('prosthetic', 'arm')

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
        self.add_polyline("socket",(8,4),(28,4),(24,18),(18,18),(12,18),closed=True)
        stroke("elbow",(18,18),[((24,24),6,6,True),((18,30),6,6,True),((12,24),6,6,True),((18,18),6,6,True)],True)
        self.relate("connect","socket","elbow")
        self.add_line("forearm",(18,30),(26,38));self.relate("connect","elbow","forearm")
        self.add_polyline("claw",(40,32),(32,30),(26,38),(32,44),(40,42));self.relate("connect","claw","forearm")

