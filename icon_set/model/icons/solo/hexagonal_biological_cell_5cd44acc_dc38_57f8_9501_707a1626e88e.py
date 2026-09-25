"""Hexagonal Biological Cell.
Plan: Centerline extremes (6,6)-(42,42); mirrored hexagon and six attached radial projections; one off-center circular nucleus.
References: supplied original source; Lucide hexagon: coherent closed polygon.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cd44acc-dc38-57f8-9501-707a1626e88e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/bacteria_5cd44acc-dc38-57f8-9501-707a1626e88e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hexagonal-biological-cell-5cd44acc'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('hexagonal-biological-cell',)
    keywords = ('hexagonal', 'biological', 'cell')

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
        vertices=[(16,12),(32,12),(39,24),(32,36),(16,36),(9,24)]
        ends=[(12,6),(36,6),(42,24),(36,42),(12,42),(6,24)]
        self.add_polyline("cell",*vertices,closed=True)
        for j,(a,b) in enumerate(zip(vertices,ends)):
            self.add_line(f"projection-{j}",a,b)
            self.relate("connect","cell",f"projection-{j}")
        circle("nucleus",25,24,3)

