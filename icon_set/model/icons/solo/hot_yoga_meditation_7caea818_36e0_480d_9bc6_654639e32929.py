"""Hot Yoga Meditation.
Plan: VRECT_L centerlines (8,4)-(40,44). Curved shoulders, full torso, broad
crossed legs and two repeated heat strokes; omit one heat stroke for legibility.
Head radius4 center(24,8), bottom12; actual torso junction(24,20), so
centerline gap8 and visible ink gap4. Vertical torso and head axes align.
References: supplied original source; human_ref/full_body_ref.png seated posture and user.svg circular head; no useful direct Lucide meditation match.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7caea818-36e0-480d-9bc6-654639e32929'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/hot yoga sit_7caea818-36e0-480d-9bc6-654639e32929.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hot-yoga-meditation-7caea818'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('hot-yoga-meditation',)
    keywords = ('hot', 'yoga', 'meditation')

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
        circle("head",24,8,4)
        self.add_line("torso",(24,20),(24,28))
        self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")
        stroke("arms",(10,30),[((14,24),),((24,20),10,4,True),((34,24),10,4,True),((38,30),)])
        self.relate("connect","torso","arms")
        stroke("legs",(10,30),[((8,36),2,6,False),((12,44),4,8,False),((36,44),),
            ((40,36),4,8,False),((38,30),2,6,False)])
        self.relate("connect","arms","legs")
        self.add_line("crossed-leg",(10,30),(36,44))
        self.relate("connect","legs","crossed-leg")
        self.relate("connect","arms","crossed-leg")
        for j,x in enumerate((9,39)):
            stroke(f"heat-{j}",(x,4),[((x,8),1,2,False),((x,12),1,2,True)])
