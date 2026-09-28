"""Physical Therapy Session.
Plan: (4,8)-(44,40). Therapist supports reclining patient with a raised knee. Equal radius-4 heads and exact8 centerline head gaps; treatment-table line omitted for clarity.
References: supplied original source; human_ref/full_body_ref.png: equal circular heads and articulated treatment pose.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '423dcab8-75b5-46fd-acba-3c2dc79a82f1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty rehabilitation_423dcab8-75b5-46fd-acba-3c2dc79a82f1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'physical-therapy-session-423dcab8'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('physical-therapy-session',)
    keywords = ('physical', 'therapy', 'session')

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
        circle("therapist-head",8,12,4)
        self.add_line("therapist-torso",(8,24),(8,30))
        self.add_line("therapist-leg",(8,30),(4,40));self.relate("connect","therapist-torso","therapist-leg")
        self.add_polyline("arm",(8,24),(16,28),(22,20));self.relate("connect","therapist-torso","arm")
        circle("patient-head",40,36,4)
        self.add_line("patient-torso",(28,36),(24,36))
        self.add_polyline("bent-leg",(24,36),(22,20),(18,20));self.relate("connect","patient-torso","bent-leg");self.relate("connect","arm","bent-leg")
        self.add_line("resting-leg",(24,36),(14,40));self.relate("connect","patient-torso","resting-leg");self.relate("connect","bent-leg","resting-leg")
        self.mark_human_figure("therapist",head="therapist-head",torso="therapist-torso",torso_junction="start")
        self.mark_human_figure("patient",head="patient-head",torso="patient-torso",torso_junction="start")

