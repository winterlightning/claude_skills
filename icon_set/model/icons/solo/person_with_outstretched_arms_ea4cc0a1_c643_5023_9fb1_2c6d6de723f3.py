"""Person with Outstretched Arms.
Plan: (6,6)-(42,42). Round head, raised outstretched arms, narrow torso and spread legs. Outlined limb thickness reduced to coherent figure strokes; exact8 head gap.
References: supplied original source; human_ref/full_body_ref.png: articulated figure with equal limbs; Lucide accessibility: sparse human construction.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea4cc0a1-c643-5023-9fb1-2c6d6de723f3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/anatomical_ea4cc0a1-c643-5023-9fb1-2c6d6de723f3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-with-outstretched-arms-ea4cc0a1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('person-with-outstretched-arms',)
    keywords = ('person', 'with', 'outstretched', 'arms')

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
        circle("head",24,11,5)
        self.add_line("torso",(24,24),(24,28));self.add_line("hips",(24,28),(24,30));self.relate("connect","torso","hips")
        self.add_polyline("arms",(6,18),(24,28),(42,18));self.relate("connect","torso","arms");self.relate("connect","hips","arms")
        self.add_polyline("legs",(12,42),(24,30),(36,42));self.relate("connect","hips","legs")
        self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")

