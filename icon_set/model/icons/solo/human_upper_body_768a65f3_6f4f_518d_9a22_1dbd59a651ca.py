"""Human Upper Body.
Plan: Centerlines (8,4)-(40,44); mirrored shoulder outline; circular head radius 6 centered (24,10). Head bottom16 to shoulder24 is exactly8 centerline /4 ink units.
References: supplied original source; human_ref/user.svg: circular head above broad rounded shoulders; outlined upper body, not a stick figure.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '768a65f3-6f4f-518d-9a22-1dbd59a651ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage map body_768a65f3-6f4f-518d-9a22-1dbd59a651ca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'human-upper-body-768a65f3'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('human-upper-body',)
    keywords = ('human', 'upper', 'body')

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
        circle("head",24,10,6)
        stroke("body", (8,44), [((8,34),), ((18,24),10,10,True),
            ((30,24),), ((40,34),10,10,True), ((40,44),)])
        for x in (17,31):self.add_line(f"arm-{x}",(x,36),(x,44))

