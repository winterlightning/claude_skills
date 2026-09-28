"""Mother Holding Baby.
Plan: (8,4)-(40,44). Large mother head over curved upper body, smaller baby cradled across chest. Mother head bottom16 to shoulder24; baby head bottom28 to torso36: both exact8 centerline gaps.
References: supplied original source; human_ref/user.svg and full_body_ref.png: round heads, curved shoulders and sparse held-child gesture.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d984011-ce10-4216-822d-ce30047b232d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/mother baby_7d984011-ce10-4216-822d-ce30047b232d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mother-holding-baby-7d984011'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('mother-holding-baby',)
    keywords = ('mother', 'holding', 'baby')

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
        circle("mother-head",16,10,6)
        stroke("mother-body",(16,24),[((8,32),8,8,False),((8,44),)])
        circle("baby-head",36,24,4)
        self.add_line("baby-torso",(36,36),(36,44))
        stroke("arm",(18,32),[((18,38),),((24,44),6,6,False),((36,44),)])
        self.relate("connect","arm","baby-torso")
        self.mark_human_figure("baby",head="baby-head",torso="baby-torso",torso_junction="start")

