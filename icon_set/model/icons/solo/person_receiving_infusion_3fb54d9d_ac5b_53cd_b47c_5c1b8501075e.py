"""Person Receiving Infusion.
Plan: (4,8)-(44,40). Standing patient connected at hand to elevated IV bag and stand; exact8 head/torso centerline gap. Small hanger and liquid marks omitted.
References: supplied original source; human_ref/full_body_ref.png; Lucide stethoscope and syringe: sparse connected treatment device.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fb54d9d-ac5b-53cd-b47c-5c1b8501075e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/transfusion human_3fb54d9d-ac5b-53cd-b47c-5c1b8501075e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-receiving-infusion-3fb54d9d'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('person-receiving-infusion',)
    keywords = ('person', 'receiving', 'infusion')

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
        circle("head",12,12,4)
        self.add_line("torso",(12,24),(12,26));self.add_line("hips",(12,26),(12,30));self.relate("connect","torso","hips")
        self.add_polyline("legs",(4,40),(12,30),(20,40));self.relate("connect","hips","legs")
        self.add_line("arm",(12,26),(22,26));self.relate("connect","arm","torso");self.relate("connect","arm","hips")
        self.add_polyline("bag",(24,8),(29,8),(34,8),(34,18),(29,18),(24,18),closed=True)
        stroke("stand",(44,40),[((44,12),),((40,8),4,4,False),((29,8),)])
        self.relate("connect","stand","bag")
        self.add_line("foot",(36,40),(44,40));self.relate("connect","stand","foot")
        stroke("tube",(22,26),[((25,26),),((29,22),4,4,False),((29,18),)])
        self.relate("connect","arm","tube");self.relate("connect","tube","bag")
        self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")

