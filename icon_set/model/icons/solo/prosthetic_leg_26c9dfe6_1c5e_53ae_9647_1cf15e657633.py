"""Prosthetic Leg.
Plan: (8,4)-(40,44). Tapered socket, rounded knee, narrow shin and curved ankle to a right-pointing foot. Solid shin/foot removes crowded nested outlines.
References: supplied original source; Lucide bone: rounded joint and coherent limb segments; source socket and foot direction.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26c9dfe6-1c5e-53ae-9647-1cf15e657633'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/prosthetic leg_26c9dfe6-1c5e-53ae-9647-1cf15e657633.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'prosthetic-leg-26c9dfe6'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('prosthetic-leg',)
    keywords = ('prosthetic', 'leg')

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
        self.add_polyline("socket",(8,4),(32,4),(28,16),(20,18),(12,16),closed=True)
        stroke("knee",(20,18),[((26,24),6,6,True),((20,30),6,6,True),((14,24),6,6,True),((20,18),6,6,True)],True)
        self.relate("connect","socket","knee")
        stroke("shin-foot",(20,30),[((18,38),),((24,44),6,6,False),((40,44),)])
        self.relate("connect","knee","shin-foot")

