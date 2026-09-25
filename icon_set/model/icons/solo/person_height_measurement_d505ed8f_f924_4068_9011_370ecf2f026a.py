"""Person Height Measurement.
Plan: (8,4)-(40,44). Tall measuring rule with four ticks beside circular-headed standing figure. Rule reduced to one edge; head bottom16 to torso24 gives exact8 centerline gap.
References: supplied original source; human_ref/full_body_ref.png; Lucide ruler and person-standing: ticks and minimal figure.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd505ed8f-f924-4068-9011-370ecf2f026a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/virtual measuring_d505ed8f-f924-4068-9011-370ecf2f026a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-height-measurement-d505ed8f'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('person-height-measurement',)
    keywords = ('person', 'height', 'measurement')

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
        self.add_polyline("rule",(8,4),(8,8),(8,18),(8,28),(8,38),(8,44))
        for y in (8,18,28,38):self.add_line(f"tick-{y}",(8,y),(14,y));self.relate("connect","rule",f"tick-{y}")
        circle("head",34,10,6)
        self.add_line("torso",(34,24),(34,28));self.add_line("hips",(34,28),(34,32));self.relate("connect","torso","hips")
        self.add_polyline("arms",(28,24),(34,28),(40,24));self.relate("connect","arms","torso");self.relate("connect","arms","hips")
        self.add_polyline("legs",(28,44),(34,32),(40,44));self.relate("connect","legs","hips")
        self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")

