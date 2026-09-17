"""Round Microscopic Cell.
Plan: Center (24,24), radial envelope20. Circular membrane radius17 with eight attached rays; left curved organelle and two right solid bodies.
References: supplied original source; Lucide bean: curved internal organelle; source membrane, projections and three interior bodies.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7d53d99-6046-4adf-8845-1c1536e0d9ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/red blood cell strem_f7d53d99-6046-4adf-8845-1c1536e0d9ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-microscopic-cell-f7d53d99'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('round-microscopic-cell',)
    keywords = ('round', 'microscopic', 'cell')

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
        stroke("cell",(24,7),[((39,16),17,17,True),((41,24),17,17,True),((39,32),17,17,True),((24,41),17,17,True),((9,32),17,17,True),((7,24),17,17,True),((9,16),17,17,True),((24,7),17,17,True)],True)
        rays=[((24,7),(24,4)),((41,24),(44,24)),((24,41),(24,44)),((7,24),(4,24)),((39,16),(41,15)),((39,32),(41,33)),((9,32),(7,33)),((9,16),(7,15))]
        for j,(a,b) in enumerate(rays):self.add_line(f"ray-{j}",a,b);self.relate("connect","cell",f"ray-{j}")
        stroke("organelle",(20,20),[((16,24),4,4,False),((20,28),4,4,False)])
        self.add_dot("body-upper",(30,18));self.add_dot("body-lower",(30,30))

