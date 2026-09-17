"""Irregular Microscopic Cell.
Plan: Uneven eight-arc membrane with six varied projections; off-center nucleus. Radial ends own (6,6)-(42,42); preserve intentional biological asymmetry.
References: supplied original source; no useful direct Lucide match; source lobes and projections.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '121b2f03-cf9b-5dd8-8676-3b12d6966e8b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/cancer cell_121b2f03-cf9b-5dd8-8676-3b12d6966e8b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'irregular-microscopic-cell-121b2f03'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('irregular-microscopic-cell',)
    keywords = ('irregular', 'microscopic', 'cell')

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
        vertices=[(24,11),(34,16),(37,24),(32,34),(24,37),(14,32),(11,24),(16,14)]
        radii=[10,8,10,8,10,8,10,8]
        stroke("cell",vertices[0],[(vertices[(j+1)%8],r,r,True) for j,r in enumerate(radii)],True)
        rays=[((24,11),(22,6)),((37,24),(42,25)),((24,37),(26,42)),
              ((11,24),(6,22)),((16,14),(10,8)),((32,34),(39,40))]
        for j,(a,b) in enumerate(rays):
            self.add_line(f"projection-{j}",a,b);self.relate("connect","cell",f"projection-{j}")
        circle("nucleus",23,24,3)

