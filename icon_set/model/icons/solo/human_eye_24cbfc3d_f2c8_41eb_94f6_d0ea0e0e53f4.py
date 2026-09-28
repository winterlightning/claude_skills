"""Human Eye.
Plan: Centerline extremes (4,10)-(44,38); symmetric pointed lids and circular iris; no extra pupil or eyelashes.
References: supplied original source; Lucide eye: paired lid arcs surrounding one circle.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24cbfc3d-f2c8-41eb-94f6-d0ea0e0e53f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/eye_24cbfc3d-f2c8-41eb-94f6-d0ea0e0e53f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'human-eye-24cbfc3d'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('human-eye',)
    keywords = ('human', 'eye')

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
        # rx=25, ry=35 yields exact 14-unit sagitta for a 40-unit chord.
        stroke("lids", (4,24), [((44,24),25,35,True), ((4,24),25,35,True)],True)
        circle("iris",24,24,5)

