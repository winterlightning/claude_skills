"""Leg Massage Therapy.
Plan: (4,8)-(44,40). Equal radius-4 heads; vertical therapist torso, horizontal patient torso; both exact8 centerline head gaps. Raised knee and therapist hand share an endpoint.
References: supplied original source; human_ref/full_body_ref.png: equal circular heads and simple articulated limbs.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a608386-d726-47bd-b174-b25be1ff2bcc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/thai massage leg_4a608386-d726-47bd-b174-b25be1ff2bcc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'leg-massage-therapy-4a608386'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('leg-massage-therapy',)
    keywords = ('leg', 'massage', 'therapy')

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

