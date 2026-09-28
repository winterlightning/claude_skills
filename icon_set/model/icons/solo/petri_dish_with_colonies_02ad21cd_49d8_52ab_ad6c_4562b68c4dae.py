"""Petri Dish with Colonies.
Plan: Outer radius20 at (24,24). Three colonies retain their staggered layout; two tiny colonies reduced to solid round marks.
References: supplied original source; Lucide microscope: sparse laboratory subject; original three-colony placement.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02ad21cd-49d8-52ab-ad6c-4562b68c4dae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/petri dish_02ad21cd-49d8-52ab-ad6c-4562b68c4dae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'petri-dish-with-colonies-02ad21cd'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('petri-dish-with-colonies',)
    keywords = ('petri', 'dish', 'with', 'colonies')

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
        circle("dish",24,24,20)
        circle("colony-large",18,20,4)
        self.add_dot("colony-right",(32,24));self.add_dot("colony-lower",(20,33))

