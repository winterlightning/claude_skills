"""Prenatal Massage.
Plan: (4,8)-(44,40). Therapist reaches toward a reclining pregnant abdomen, with patient head at right. Equal radius-4 heads and exact8 detached head gaps; table omitted.
References: supplied original source; human_ref/full_body_ref.png: shared figure vocabulary; source raised pregnant abdomen.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9058ef4c-f3a9-5176-829d-19a5d38d7add'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/prenatal massage_9058ef4c-f3a9-5176-829d-19a5d38d7add.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'prenatal-massage-9058ef4c'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('prenatal-massage',)
    keywords = ('prenatal', 'massage')

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
        circle("therapist-head",28,12,4)
        self.add_line("therapist-torso",(28,24),(28,28))
        self.add_line("arm",(28,24),(18,28));self.relate("connect","therapist-torso","arm")
        circle("patient-head",40,36,4)
        self.add_line("patient-torso",(28,36),(26,36))
        stroke("abdomen",(26,36),[((18,28),8,8,False),((10,36),8,8,False),((4,36),)])
        self.relate("connect","abdomen","patient-torso");self.relate("connect","abdomen","arm")
        self.mark_human_figure("therapist",head="therapist-head",torso="therapist-torso",torso_junction="start")
        self.mark_human_figure("patient",head="patient-head",torso="patient-torso",torso_junction="start")

